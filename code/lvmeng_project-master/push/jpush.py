"""
Jiguang Messaging
"""

import json
import requests
from . import common

try:
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    # Python 2 support
    from urllib2 import Request, urlopen
    from urllib import urlencode

from django.core.exceptions import ImproperlyConfigured
from . import NotificationError
from .settings import PUSH_NOTIFICATIONS_SETTINGS as SETTINGS
from .models import JPUSHDevice


class JPUSHError(NotificationError):
    pass


def _chunks(l, n):
    """
    Yield successive chunks from list \a l with a minimum size \a n
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]


def _jpush_send(data, content_type):
    key = SETTINGS.get("JPUSH_APP_KEY")
    secret = SETTINGS.get("JPUSH_MASTER_SECRET")
    session = requests.Session()
    session.auth = (key, secret)

    if not key or not secret:
        raise ImproperlyConfigured('You need to set PUSH_NOTIFICATIONS_SETTINGS["JPUSH_APP_KEY"] and \
        PUSH_NOTIFICATIONS_SETTINGS["JPUSH_MASTER_SECRET"] to send messages through JPUSH.')

    headers = {
        "Content-Type": content_type,
        "user-agent": 'jpush-api-python-client',
        "connection": 'keep-alive',
    }

    url = SETTINGS.get("JPUSH_POST_URL")
    try:
        response = session.request("POST", url, data=data, params=None, headers=headers, timeout=30)
    except requests.exceptions.ConnectTimeout:
        raise common.APIConnectionException("Connection to api.jpush.cn timed out.")
    except:
        raise common.APIConnectionException("Connection to api.jpush.cn error.")

    if response.status_code == 401:
        raise common.Unauthorized("Please check your AppKey and Master Secret")
    elif not (200 <= response.status_code < 300):
        raise common.JPushFailure.from_response(response)
    return response

    # request = Request(SETTINGS["JPUSH_POST_URL"], data, headers)
    # return urlopen(request).read().decode("utf-8")


def _jpush_send_plain(registration_id, data, **kwargs):
    """
    Sends a JPUSH notification to a single registration_id.
    This will send the notification as form data.
    If sending multiple notifications, it is more efficient to use
    jpush_send_bulk_message() with a list of registration_ids
    """

    values = {"registration_id": registration_id}

    for k, v in data.items():
        values["data.%s" % (k)] = v.encode("utf-8")

    for k, v in kwargs.items():
        if v:
            if isinstance(v, bool):
                # Encode bools into ints
                v = 1
            values[k] = v

    data = urlencode(sorted(values.items())).encode("utf-8")  # sorted items for tests

    result = _jpush_send(data, "application/x-www-form-urlencoded;charset=UTF-8")

    # Information about handling response from Google docs (https://developers.google.com/cloud-messaging/http):
    # If first line starts with id, check second line:
    # If second line starts with registration_id, gets its value and replace the registration tokens in your
    # server database. Otherwise, get the value of Error

    if result.startswith("id"):
        lines = result.split("\n")
        if len(lines) > 1 and lines[1].startswith("registration_id"):
            new_id = lines[1].split("=")[-1]
            _jpush_handle_canonical_id(new_id, registration_id)

    elif result.startswith("Error="):
        if result in ("Error=NotRegistered", "Error=InvalidRegistration"):
            # Deactivate the problematic device
            device = JPUSHDevice.objects.filter(registration_id=values["registration_id"])
            device.update(active=0)
            return result

        raise JPUSHError(result)

    return result


def payload(registration_ids, message, **kwargs):
    values = {
        "platform": SETTINGS.get("JPUSH_PLATFORM"),
        "audience": {"registration_id":registration_ids},
        "notification": {
            "android":{"alert":message}
        },
    }

    title = kwargs.pop("title", None)
    builder_id = kwargs.pop("builder_id", None)
    extras = kwargs.pop("extras", {})
    message = kwargs.pop("message", {})
    sms_message = kwargs.pop("sms_message", {})
    options = kwargs.pop("options", {})

    if title:
        values["notification"]["android"]["title"] = title
    if builder_id:
        values["notification"]["android"]["builder_id"] = builder_id
    if extras:
        values["notification"]["android"]["extras"] = extras
    if message:
        values["message"] = message
    if sms_message:
        values["sms_message"] = sms_message
    if options:
        values["options"] = options


    return values


def _jpush_send_json(registration_ids, message, **kwargs):
    """
    Sends a JPUSH notification to one or more registration_ids. The registration_ids
    needs to be a list.
    This will send the notification as json data.
    """

    values = payload(registration_ids, message, **kwargs)

    data = json.dumps(values).encode("utf-8")

    response = _jpush_send(data, "application/json;charset:utf-8")
    # response = json.loads(response)
    # response = json.loads(_jpush_send(data, "application/json;charset:utf-8"))
    return response
    # if response["failure"] or response["canonical_ids"]:
    #     ids_to_remove, old_new_ids = [], []
    #     throw_error = False
    #     for index, result in enumerate(response["results"]):
    #         error = result.get("error")
    #         if error:
    #             # Information from Google docs (https://developers.google.com/cloud-messaging/http)
    #             # If error is NotRegistered or InvalidRegistration, then we will deactivate devices because this
    #             # registration ID is no more valid and can't be used to send messages, otherwise raise error
    #             if error in ("NotRegistered", "InvalidRegistration"):
    #                 ids_to_remove.append(registration_ids[index])
    #             else:
    #                 throw_error = True
    #
    #         # If registration_id is set, replace the original ID with the new value (canonical ID) in your
    #         # server database. Note that the original ID is not part of the result, so you need to obtain it
    #         # from the list of registration_ids passed in the request (using the same index).
    #         new_id = result.get("registration_id")
    #         if new_id:
    #             old_new_ids.append((registration_ids[index], new_id))
    #
    #     if ids_to_remove:
    #         removed = JPUSHDevice.objects.filter(registration_id__in=ids_to_remove)
    #         removed.update(active=0)
    #
    #     for old_id, new_id in old_new_ids:
    #         _jpush_handle_canonical_id(new_id, old_id)
    #
    #     if throw_error:
    #         raise JPUSHError(response)
    # return response


def _jpush_handle_canonical_id(canonical_id, current_id):
    """
    Handle situation when JPUSH server response contains canonical ID
    """
    if JPUSHDevice.objects.filter(registration_id=canonical_id, active=True).exists():
        JPUSHDevice.objects.filter(registration_id=current_id).update(active=False)
    else:
        JPUSHDevice.objects.filter(registration_id=current_id).update(registration_id=canonical_id)


def jpush_send_message(registration_id, data, **kwargs):
    """
    Sends a JPUSH notification to a single registration_id.

    If sending multiple notifications, it is more efficient to use
    jpush_send_bulk_message() with a list of registration_ids

    A reference of extra keyword arguments sent to the server is available here:
    https://developers.google.com/cloud-messaging/server-ref#downstream
    """

    return _jpush_send_plain(registration_id, data, **kwargs)


def jpush_send_bulk_message(registration_ids, message, **kwargs):
    """
    Sends a JPUSH notification to one or more registration_ids. The registration_ids
    needs to be a list.
    This will send the notification as json data.

    A reference of extra keyword arguments sent to the server is available here:
    https://developers.google.com/cloud-messaging/server-ref#downstream
    """

    # JPUSH only allows up to 1000 reg ids per bulk message
    # https://www.jpush.cn#request
    max_recipients = SETTINGS.get("JPUSH_MAX_RECIPIENTS")
    if len(registration_ids) > max_recipients:
        ret = []
        for chunk in _chunks(registration_ids, max_recipients):
            ret.append(_jpush_send_json(chunk, message, **kwargs))
        return ret

    return _jpush_send_json(registration_ids, message, **kwargs)

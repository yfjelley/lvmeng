from django.shortcuts import render

from celery_push.run import run
from .models import APNSDevice, JPUSHDevice

# Create your views here.


#push to users by user list
def push_to_ios(user_list, message, **kwargs):
    for user in user_list:
        apns = APNSDevice.objects.filter(user=user)
        if apns:
            run(apns, message, **kwargs)
            
def push_to_android(user_list, message, **kwargs):
    for user in user_list:
        jpush = JPUSHDevice.objects.filter(user=user)
        if jpush:
            run(jpush, message, **kwargs)
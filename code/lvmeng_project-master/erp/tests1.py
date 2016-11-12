#coding:utf-8
from django.contrib.auth.models import User,Permission
from django.http import JsonResponse
from erp.forms import Position_permission
from django.shortcuts import render_to_response
from django.template import RequestContext
from erp.models import Position
from erp.models import Agent,Online_chat
from erp.views import get_business
from api.models import VerificationCode

def valid_phone(request):
    phone = request.GET.get("str")
    data = User.objects.filter(username=phone).count()
    if data:
        return JsonResponse({"result":"false"})
    else:
        return JsonResponse({"result":"true"})

def valid_email(request):
    email = request.GET.get("str")
    data = User.objects.filter(username=email).count()
    if data:
        return JsonResponse({"result":"false"})
    else:
        return JsonResponse({"result":"true"})

def valid_code(request):
    phoneNum = request.POST.get("phoneNum")
    verification_code = request.POST.get("verification_code")
    codes = VerificationCode.objects.filter(phoneNum=phoneNum,purpose=0)
    if not codes or codes[0].code != verification_code:
        return JsonResponse({"result":"false"})
    else:
        return JsonResponse({"result":"true"})

def get_position_permission(request):
    position_id = request.GET.get("position_id","")
    if position_id:
        form = Position_permission(instance=Position.objects.get(pk=position_id))
    else:
        form = Position_permission()
    form.fields['permissions'].queryset = Permission.objects.filter(id__gt=40,content_type_id=2)
    return render_to_response("erp/position_permission.html",locals(),context_instance=RequestContext(request))


#检测是否有新消息
def check_new_message(request):
    business = get_business(request)
    talk_user = Agent.objects.get(id=request.GET.get("talk_user"))
    data = Online_chat.objects.filter(sender=talk_user.user,recipient=request.user,business=business,read=False)
    # print talk_user.user.id,request.user.id,business.id
    if data:
        return JsonResponse({"result":"true"})
    else:
        return JsonResponse({"result":"false"})




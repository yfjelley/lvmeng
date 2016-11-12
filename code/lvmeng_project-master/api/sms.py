#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import json
import datetime

from api.models import *
import top.api


def get_verification_code(cell_number):
    appkey = "23343212"
    secret = "0ff32a0b55184e84aff800c17fd81e56"

    req=top.api.AlibabaAliqinFcSmsNumSendRequest() # 使用默认参数即可
    req.set_app_info(top.appinfo(appkey,secret))

    # req.extend="123456"
    req.sms_type="normal"
    req.sms_free_sign_name="注册验证"
    code = random.randint(100000, 999999)
    sms_param={"code":str(code),"product":"牛基队"}
    req.sms_param=json.dumps(sms_param)
    req.rec_num=cell_number
    req.sms_template_code="SMS_7360337"
    try:
        resp= req.getResponse()
        success = resp[u'alibaba_aliqin_fc_sms_num_send_response'][u'result'][u'success']
        if success:
            now = datetime.datetime.now()
            verification_code = VerificationCode(phoneNum=cell_number, code=code, register_date=now, purpose=u'0')
            verification_code.save()
            return True
        else:
            return False
        # return {"code":str(code), "response":resp}
    except Exception,e:
        return False

def forget_password_code(cell_number):
    appkey = "23343212"
    secret = "0ff32a0b55184e84aff800c17fd81e56"

    req=top.api.AlibabaAliqinFcSmsNumSendRequest() # 使用默认参数即可
    req.set_app_info(top.appinfo(appkey,secret))

    # req.extend="123456"
    req.sms_type="normal"
    req.sms_free_sign_name="身份验证"
    code = random.randint(100000, 999999)
    sms_param={"code":str(code),"product":"牛基队"}
    req.sms_param=json.dumps(sms_param)
    req.rec_num=cell_number
    req.sms_template_code="SMS_7360335"
    try:
        resp= req.getResponse()
        success = resp[u'alibaba_aliqin_fc_sms_num_send_response'][u'result'][u'success']
        if success:
            now = datetime.datetime.now()
            verification_code = VerificationCode(phoneNum=cell_number, code=code, register_date=now, purpose=u'1')
            verification_code.save()
            return True
        else:
            return False
        # return {"code":str(code), "response":resp}
    except Exception,e:
        return False

def data_update_code(cell_number):
    appkey = "23343212"
    secret = "0ff32a0b55184e84aff800c17fd81e56"

    req=top.api.AlibabaAliqinFcSmsNumSendRequest() # 使用默认参数即可
    req.set_app_info(top.appinfo(appkey,secret))

    # req.extend="123456"
    req.sms_type="normal"
    req.sms_free_sign_name="变更验证"
    code = random.randint(100000, 999999)
    sms_param={"code":str(code),"product":"牛基队"}
    req.sms_param=json.dumps(sms_param)
    req.rec_num=cell_number
    req.sms_template_code="SMS_7360334"
    try:
        resp= req.getResponse()
        success = resp[u'alibaba_aliqin_fc_sms_num_send_response'][u'result'][u'success']
        if success:
            now = datetime.datetime.now()
            verification_code = VerificationCode(phoneNum=cell_number, code=code, register_date=now, purpose=u'2')
            verification_code.save()
            return True
        else:
            return False
        # return {"code":str(code), "response":resp}
    except Exception,e:
        return False

if __name__ == '__main__':
    print get_verification_code("13520404512")
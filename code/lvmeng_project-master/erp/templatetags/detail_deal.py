#! /usr/bin/env python
#coding:utf-8

from django import template
from PIL import Image

register = template.Library()

@register.filter
def idnum_hide(customer):
    if customer.customer_type=='2':#pending customer
        return customer.idCard_num
    elif customer.customer_type=='1':#real customer
        idnum = customer.idCard_num
        if idnum and (len(idnum)==15 or len(idnum)==18):
            idnum = idnum[0:6] + '******' + idnum[-4:]
        return idnum
    else:
        return None

@register.filter
def yuan_convert(yuan):
    if yuan:
        if yuan<0:
            return ''
        elif yuan<10000:
            return str(yuan) + u'元'
        elif yuan<100000000:
            return str(float(yuan)/10000) + u'万元'
        else:
            return str(float(yuan)/100000000) + u'亿元'
    else:
        return yuan

@register.filter
def check_picture(url):
    if url:
        return '/media/'+str(url)
    else:
        return '/static/img/default_blue.png'

@register.filter
def check_device(obj):
    if obj.device_id:
        return u"解除[已绑定]"
    else:
        return u"未绑定"

@register.filter
def move_zero(obj):
    flag = True
    try:
        expected = obj.split(".")
        if len(expected)>1:
            sec = expected[1]
            while flag:
                if sec:
                    if sec[len(sec)-1] == "0":
                        sec = sec[:len(sec)-1]
                    else:
                        return expected[0]+"."+sec
                else:
                    flag = False
    except:
        return obj

    return expected[0]
    #  return ("%.2f" % (float(obj)))

@register.filter
def date_str(obj):
    return str(obj).split(".")[0]

import re
@register.filter
def lv_announce_cut(obj):
    if len(obj)>30:
        chars = obj[::-1][:30][::-1].decode('utf8')
        chinese=u"([\u4e00-\u9fa5]+)"
        return ''.join(re.compile(chinese).findall(chars))+'...'
    return obj

@register.simple_tag
def get_verbose_field_name(instance, field_name):

    return instance._meta.get_field(field_name).verbose_name.title()
#! /usr/bin/env python
#coding:utf-8

from __future__ import absolute_import
#局部的包将不能覆盖全局的包, 本地的包必须使用相对引用了

from celery_push.celery import push
# from push.models import *

#ios push
@push.task
def APNSPush(objects, message, **kwargs):
    objects.send_message(message, **kwargs)

#test
@push.task
def add(x, y):
    return x + y

#example
# from celery_push.push import APNSPush
# from push.models import *
# device = APNSDevice.objects.all()
# APNSPush.apply_async((device, "celery"),kwargs={"badge":0}, queue='push')
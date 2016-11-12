#! /usr/bin/env python
#coding:utf-8

from __future__ import absolute_import
#局部的包将不能覆盖全局的包, 本地的包必须使用相对引用

import os, sys
sys.path.append("../lvmeng")

import django
from django.conf import settings
from lvmeng import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lvmeng.settings")
django.setup()

from celery import Celery

push = Celery("push",
             broker="amqp://guest@localhost//",
             backend="amqp",
             include=["celery_push.push"]
    )

push.conf.update(
    CELERY_ROUTES={
        "celery_push.push.apnspush":{"queue":"push"},
        "celery_push.push.add":{"queue":"push"},# 把add任务放入push队列
        # 需要执行时指定队列 add.apply_async((2, 2), queue='push')
        #执行指令为celery -A celery_push worker -Q push --loglevel=info
        },

    )

if __name__ == "__main__":
    push.start()
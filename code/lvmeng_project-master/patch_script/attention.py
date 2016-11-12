#coding:utf-8
"""每天推送提醒企业版用户上下班时间
"""

import os, sys
sys.path.append("../lvmeng")

import django
from django.conf import settings
from lvmeng import settings
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lvmeng.settings")
# django.setup()
# from erp.models import Business, Agent
# from django.contrib.auth.models import User
# from oa.models import Check_Time_Setting
# from push.views import push_to_ios, push_to_android

import datetime
from threading import Timer

from apscheduler.schedulers.blocking import BlockingScheduler

scheduler_cron = BlockingScheduler()


def django_setup():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lvmeng.settings")
    django.setup()


def push_attention():
    django_setup()
    from django.contrib.auth.models import User
    from oa.models import Check_Time_Setting
    from push.views import push_to_ios, push_to_android

    allCheckTime = Check_Time_Setting.objects.all()

    for checkTime in allCheckTime:
        now = datetime.datetime.now()
        today = datetime.date.today()

        if now.hour<12:
            td = (datetime.datetime.combine(today, checkTime.check_in_remind)-now).seconds #距离上班推送时间的秒数
            message = u"距离上班时间还有%s分钟!" % ((datetime.datetime.combine(today, checkTime.check_in_time)-datetime.datetime.combine(today, checkTime.check_in_remind)).seconds/60)
        else:
            td = (datetime.datetime.combine(today, checkTime.check_out_remind)-now).seconds #距离下班推送时间的秒数
            message = u"距离下班时间还有%s分钟!" % ((datetime.datetime.combine(today, checkTime.check_out_time)-datetime.datetime.combine(today, checkTime.check_out_remind)).seconds/60)
        user = list(User.objects.filter(agent__business=checkTime.business))

        Timer(td, push_to_android, kwargs={"user_list": user, "message": message}).start()
        Timer(td, push_to_ios, kwargs={"user_list": user, "message": message}).start()


scheduler_cron.add_job(push_attention, 'cron', day_of_week='0-6', hour='8,16', minute='0')
scheduler_cron.start()
# push_attention()
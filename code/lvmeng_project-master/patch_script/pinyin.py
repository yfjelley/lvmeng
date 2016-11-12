#! /usr/bin/env python
#coding:utf-8

import os, sys
sys.path.append("../lvmeng")

import django
from django.conf import settings
from lvmeng import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lvmeng.settings")
django.setup()

from erp.models import Agent, Customer

if __name__=="__main__":
    '''
    生成所有的员工和客户名字的拼音
    '''
    agents = Agent.objects.all()
    customers = Customer.objects.all()

    for agent in agents:
        agent.save()

    for customer in customers:
        customer.save()
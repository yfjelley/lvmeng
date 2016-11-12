#! /usr/bin/env python
#coding:utf-8

import os, sys
sys.path.append("../lvmeng")

import django
from django.conf import settings
from lvmeng import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lvmeng.settings")
django.setup()

from erp.models import Agent, Business
from django.contrib.auth.models import Permission

if __name__=="__main__":
    '''给所有员工和所有机构所有的权限
    '''
    agents = Agent.objects.filter(is_active=True)
    businesses = Business.objects.all()
    permissions = Permission.objects.filter(id__gte=218, id__lte=226) | Permission.objects.filter(id=251) #合并所有权限
    for permission in permissions:
        for agent in agents:
            if permission not in agent.permissions.all():
                agent.permissions.add(permission)
                agent.save()

        for business in businesses:
            user = business.user
            if permission not in user.user_permissions.all():
                user.user_permissions.add(permission)
                user.save()
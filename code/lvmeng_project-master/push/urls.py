#! /usr/bin/env python
#coding:utf-8

from django.conf.urls import url, include
from api.rest_framework import APNSDeviceAuthorizedViewSet, GCMDeviceAuthorizedViewSet, JPUSHDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'device/apns', APNSDeviceAuthorizedViewSet)
router.register(r'device/gcm', GCMDeviceAuthorizedViewSet)
router.register(r'device/jpush', JPUSHDeviceAuthorizedViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

]
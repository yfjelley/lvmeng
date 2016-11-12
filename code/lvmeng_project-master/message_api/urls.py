#! /usr/bin/env python
#coding:utf-8
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from rest_framework import routers

from . import views

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^', include(router.urls)),

]
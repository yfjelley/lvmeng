#coding:utf-8
from django.conf.urls import url
from investment.views import *
urlpatterns = [
    url(r'^invest_index/$', invest_index),#
]
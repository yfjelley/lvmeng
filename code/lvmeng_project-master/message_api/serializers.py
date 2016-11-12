#! /usr/bin/env python
#coding:utf-8

import datetime


from django.db.models.fields import DateField
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
# from pinax.messages.models import *


from models import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        # fields = ['thread']

class UserThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserThread

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
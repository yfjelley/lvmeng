from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import Http404
import django_filters
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from rest_framework.authentication import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from pinax.messages.models import *

from serializers import *
from models import *
# Create your views here.


class AuthorizedMixin(object):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

class ThreadViewSet(AuthorizedMixin, viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    def get_queryset(self):
        return Thread.objects.filter(users=self.request.user)#only get self

class UserThreadViewSet(AuthorizedMixin, viewsets.ModelViewSet):
    queryset = UserThread.objects.all()
    serializer_class = UserThreadSerializer

    def get_queryset(self):
        return UserThread.objects.filter(user=self.request.user)#only get self

class MessageViewSet(AuthorizedMixin, viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
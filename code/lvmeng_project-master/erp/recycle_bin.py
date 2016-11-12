#coding:utf-8
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.shortcuts import render,render_to_response,redirect
import time, json, os
from models import *
from forms import *
import datetime
import time
from django.forms.models import formset_factory,modelformset_factory
from erp.views2 import get_permissions,send_email

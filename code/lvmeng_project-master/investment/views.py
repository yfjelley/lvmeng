#coding:utf-8
from django.shortcuts import render,render_to_response,redirect
from django.template import RequestContext

# Create your views here.

#融资企业登录首页
def invest_index(request):

    return render_to_response("investment/index.html",locals(),context_instance=RequestContext(request))
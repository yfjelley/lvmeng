#! /usr/bin/env python
#coding:utf-8
import json
import time
import logging
import datetime
import os
import random
from email.mime.text import MIMEText
from email.header import Header

from django.shortcuts import render
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
from django.db.models import F
import numpy as np
# import pandas as pd
# from django_pandas.io import read_frame
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
from PIL import Image
from localflavor.cn.forms import CNIDCardField, CNCellNumberField
import smtplib

from models import *
import sms
from serializers import *
from forms import *
from api.models import *
from erp.forms import *
from erp.models import *
from lvmeng.settings import *

import logging
logger = logging.getLogger(__name__)

#检查身份证号码是否有效
def check_IDCardNumber(number):
    IDCard = CNIDCardField()#用来判断身份证号是否有效
    try:
        IDCard.clean(number)
        if IDCard.has_valid_location(number) and IDCard.has_valid_birthday(number) and IDCard.has_valid_checksum(number):
            return 1
        return 0
    except:
        return 0

#检查手机号码是否有效
def check_CellNumber(number):
    CellNumber = CNCellNumberField()#用来检查手机号是否有效
    try:
        CellNumber.clean(number)
        return 1
    except:
        return 0

#根据邀请码获取agent,存在返回agent,不存在返回False
def get_agent(code):
    if len(str(code))<6:
        return False
    business_num = code[0:5]
    try:
        agent_num = int(code[5:])
    except:
        return False
    try:
        agent = Agent.objects.get(business__business_num=business_num, agent_num=agent_num, is_active=True)
        return agent
    except:
        return False

#captcha获取三个数字的验证码
def random_digit_challenge():
    ret = u''
    for i in range(3):
        ret += str(random.randint(0,9))
    return ret, ret

#压缩图片像素(大小),尺寸不变
def set_picture_pixel(path, x=128, y=128):
    size = os.path.getsize(path)/1024
    if size>300:
        image = Image.open(path)
        image.resize((x,y),Image.ANTIALIAS)
        image.save(path, quality=20)

#从request.data中获取数据,没有返回空
def get_request_data(request, value, default=None):
    return request.data[value] if value in request.data else default


#用户积分处理
def points_deal(user, type, **kwargs):
    try:
        point = Point.objects.get(type=type)
    except Point.DoesNotExist:
        return {"status":0, "message":u"积分类型不存在!"}
    checkin, created = Checkin.objects.get_or_create(user=user, defaults={"user":user, "points":0, "continuous_days":0})

    if '3'==str(type):
        #每日签到
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        abscissa = kwargs.get('abscissa', 0)#经度
        ordinate = kwargs.get('ordinate', 0)#纬度
        #判断今天是否签到过
        if str(checkin.latest_date)==today:
            return {"status":0, "message":u"今天已签到!"}
        #根据昨天是否签到以及昨天连续签到的天数计算今天的连续签到天数
        elif str(checkin.latest_date)==yesterday:
            checkin.continuous_days += 1
        else:
            checkin.continuous_days = 1
        checkin.latest_date = today
        checkin.points += point.points
        checkin.abscissa = abscissa
        checkin.ordinate = ordinate
        checkin.save()
        History_Checkin.objects.create(user=user, abscissa=abscissa, ordinate=ordinate)

        #是否连续签到7天
        if checkin.continuous_days>=7 and checkin.continuous_days%7==0:
            points_deal(user, '4')

        return {"status":1}
    else:
        #其他情况积分直接添加,OA和转发有上限,还没有处理
        checkin.points += point.points
        checkin.save()
        return {"status":1}


#根据用户提交的信息进行用户注册
def register(data):
    name = data["name"]#姓名
    last_name=u"客户"#admin中user的last_name
    phoneNum = data["phoneNum"]#手机号码
    # idCard_num = data["idCard_num"]#身份证号码
    invitation_code = data["invitation_code"] if "invitation_code" in data else None#邀请码,有则通过邀请码注册,反之
    verification_code = data["verification_code"]#验证码
    password1 = data["password1"]#密码
    password2 = data["password2"]#重复密码

    agent = get_agent(invitation_code) if invitation_code else None

    #检查用户是否存在
    if len(Customer.objects.filter(phoneNum=phoneNum, customer_type='1'))!=0 or len(User.objects.filter(username=phoneNum))!=0:
        return {"status":0, "message":u'该手机号已经存在,请换一个手机号码注册或者登陆后添加机构,谢谢!'}
    #检查邀请码
    if invitation_code and not agent:
        return {"status":0, "message":u'邀请码不正确,请重新输入或者重新获取,谢谢!'}
    #检查手机号格式
    if not check_CellNumber(phoneNum):
        return {"status":0, "message":u'手机号码格式不正确,请重新输入,谢谢!'}
    #检查身份证号码格式
    # if not check_IDCardNumber(idCard_num):
    #     return {"status":0, "message":u'身份证号码无效,请重新输入,谢谢!'}
    #检查两次密码输入是否一致
    if password1!=password2:
        return {"status":0, "message":u'两次密码输入不一致,请检查后重新输入,谢谢!'}

    valid_second = ValidSecond.objects.get(id=1).seconds
    codes = VerificationCode.objects.filter(phoneNum=phoneNum, purpose='0')
    now = datetime.datetime.now()
    #检查验证码是否正确
    if not ( len(codes)>0 and (now-codes[0].register_date).seconds <= valid_second and verification_code==codes[0].code ):
        return {"status":0, "message":u'手机验证码无效,请重新输入或者重新获取,谢谢!'}

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    user = User.objects.create_user(username=phoneNum,first_name=name,last_name=last_name,password=password1)#新增用户名和密码
    user.save()
    #customer = Customer(user=user, name=name, phoneNum=phoneNum, idCard_num=idCard_num, register_date=today, customer_type='1')
    customer = Customer(user=user, name=name, phoneNum=phoneNum, register_date=today, customer_type='1')
    customer.save()

    if invitation_code:#如果是通过客户经理邀请码注册,添加客户经理到客户
        customer.agents.add(agent)
        customer.save()
        #添加客户经理积分
        points_deal(agent.user, '5')

    #意向客户的is_active置为False
    customerpendings = Customer.objects.filter(phoneNum=phoneNum, agents=agent, customer_type='2')
    if customerpendings.exists():
        for customerpending in customerpendings:
            customerpending.is_active=False
            customerpending.save()
    return {"status":1, "message":u'恭喜注册成功!感谢使用!'}


# Create your views here.
#product filters for rest api
class ProductFilter(filters.FilterSet):
    min_return_expected = django_filters.NumberFilter(name="return_expected", lookup_type='gte')
    max_return_expected = django_filters.NumberFilter(name="return_expected", lookup_type='lte')
    min_period = django_filters.NumberFilter(name="period", lookup_type='gte')
    max_period = django_filters.NumberFilter(name="period", lookup_type='lte')

    class Meta:
        model = Product
        fields = ['business_id','product_type', 'return_expected', 'period', 'min_return_expected', 'max_return_expected', 'min_period', 'max_period']

#product view for rest api
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('business_id','product_type', 'return_expected', 'period')
    filter_class = ProductFilter

    def get_queryset(self):
        return Product.objects.filter(is_active=True)

    #todo: add get_queryset later to limit query
#
# class ProductDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ProductSerializer(snippet)
#         return Response(serializer.data)

class BusinessViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    #获取和该customer相关的所有business
    def get_queryset(self):
        #使用foreign key反向查询实现
        return Business.objects.filter(agent__customer__user=self.request.user, is_active=True)
        # businesses = Business.objects.filter(agent__customer__user=self.request.user)
        # return list(set(businesses))

        #普通方法实现
        # try:
        #     customer = Customer.objects.get(user=self.request.user)
        #     agents = customer.agents.all()
        #     businesses = []
        #     for agent in agents:
        #         businesses.append(agent.business)
        #     #由于一个机构包含多个客户经理,所以使用list(set())去掉list的重复项
        #     return list(set(businesses))
        # except Customer.DoesNotExist:
        #     return None

    #todo: add get_queryset later to limit query

class AgentViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    #获取与该customer相关的agents
    def get_queryset(self):
        return Agent.objects.filter(customer__user=self.request.user, is_active=True)

        # try:
        #     customer = Customer.objects.get(user=self.request.user)
        #     agents = customer.agents.all()
        #     return agents
        # except Customer.DoesNotExist:
        #     return None


    #todo: add get_queryset later to limit query

class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    #this limits it only get objects related with itself
    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user, is_active=True)#only get self user

#用户基本信息修改,只能修改除了手机号码,关联的user,是否有效,注册日期和客户经理之外的其他信息
class CustomerupdateDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def get(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user, is_active=True)
        except Customer.DoesNotExist:
            return Response(None)
        serializer = CustomerSerializer(customer, context={'request':request})
        return Response(serializer.data)

    def put(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user, is_active=True)
        except Customer.DoesNotExist:
            return Response(None)
            # serializer = CustomerSerializer(customer, data=request.data)
            # if serializer.is_valid():

        user = request.user
        if "name" in request.data:
            customer.name = request.data["name"]
            user.first_name = request.data["name"]
        if "sex" in request.data:
            customer.sex = request.data["sex"]
        if "address" in request.data:
            customer.address = request.data["address"]
        # if "idCard_num" in request.data:
        #     if check_IDCardNumber(str(request.data["idCard_num"])):
        #         customer.idCard_num = request.data["idCard_num"]
        #     else:
        #         return Response({"status":0,"message":u"身份证号码无效!"})
        if "note" in request.data:
            customer.note = request.data["note"]
        if "industry" in request.data:
            customer.industry = request.data["industry"]
        if "city" in request.data:
            customer.city = request.data["city"]
        if "company" in request.data:
            customer.company = request.data["company"]
        if "risk_preference" in request.data:
            customer.risk_preference = request.data["risk_preference"]
        # if "email" in request.data:
        #     customer.email = request.data["email"]
            # customer.calling_card = request.data["calling_card"]
        customer.save()
        user.save()
        # serializer = CustomerSerializer(customer)
        return Response({"status":1,"message":u"修改成功!"})

            # return Response({"status":0,"message":serializer.errors})

#用户身份证号码认证
class IdCardUpdate(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def post(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user, is_active=True)
        except Customer.DoesNotExist:
            return Response(None)

        if "idCard_num" in request.data:
            if check_IDCardNumber(str(request.data["idCard_num"])):
                if not customer.idCard_num:
                    #添加积分
                    points_deal(request.user, '1')
                customer.idCard_num = request.data["idCard_num"]
                customer.save()
                return Response({"status":1,"message":u"身份认证成功!"})
        return Response({"status":0,"message":u"身份证号码无效!"})

#用户邮箱认证
class EamilUpdate(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def post(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user, is_active=True)
        except Customer.DoesNotExist:
            return Response(None)

        if "email" in request.data and "code" in request.data:
            email = request.data["email"]
            code = request.data["code"]
            email_code = EmailCode.objects.filter(email=email)
            now = datetime.datetime.now()
            valid_second = EmailValidSecond.objects.all()[0].seconds
            if email_code and email_code[0].code == code and (now-email_code[0].register_date).seconds<=valid_second:
                if not customer.email:
                    #积分添加
                    points_deal(request.user, '2')
                customer.email = email
                customer.save()
                return Response({"status":1,"message":u"认证成功!"})
            return Response({"status":0,"message":u"验证码错误,请重新输入或者重新获取!"})
        return Response({"status":0,"message":u"字段错误!"})

#用户邮箱验证码发送
class EamilVerify(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def post(self, request, format=None):
        if "email" in request.data:
            email = request.data["email"]
        else:
            return Response({"status":0,"message":u"字段错误!"})
        try:
            business_id = request.data["business_id"]
            business = Business.objects.get(id=business_id, agent__customer__user=request.user)
            business_name = business.name
        except:
            try:
                business = Business.objects.filter(agent__customer__user=request.user)[0]
                business_name = business.name
            except:
                business_name = ''

        #sender为在收件人邮件中显示的发件人
        sender = u'niujidui@niujidui.com'
        receivers = []
        receivers.append(email)
        code = random.randint(100000, 999999)
        mail_msg = u'''
        您好:<br/>
        您正在使用%s邮箱验证,您的验证码为:%s,该验证码一个小时内有效!<br/>
        网页登录地址为:http://niujidui.com/customer_login/<br/><br/>
        感谢您的使用与支持!<br/><br/>
        ''' % (business_name, code)
        message = MIMEText(mail_msg, 'html', 'utf-8')
        message['subject'] = u'%s邮箱验证' % business_name
        message['from'] = sender
        message['to'] = ", ".join(receivers)
        try:
            smtp = smtplib.SMTP(MAIL_HOST)
            smtp.sendmail(sender, receivers, message.as_string())
            smtp.close()
            EmailCode(email=email, code=code, register_date=datetime.datetime.now()).save()
            return Response({"status":1, "message":u"验证码已发送,请及时查收!"})
        except:
            return Response({"status":0,"message":u"发送失败,请重新发送!"})

#手机号修改
class PhoneUpdate(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def post(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user, is_active=True)
        except Customer.DoesNotExist:
            return Response(None)
        user = request.user
        if "phoneNum" in request.data and "code" in request.data:
            phoneNum = request.data["phoneNum"]
            code = request.data["code"]
            try:
                User.objects.get(username=phoneNum)
                return Response({"status":0,"message":u"该手机号已存在!"})
            except:
                pass
            valid_code = VerificationCode.objects.filter(phoneNum=phoneNum, purpose='2')
            now = datetime.datetime.now()
            valid_second = ValidSecond.objects.all()[0].seconds
            if valid_code and valid_code[0].code == code and (now-valid_code[0].register_date).seconds<=valid_second:
                customer.phoneNum = phoneNum
                customer.save()
                user.username = phoneNum
                user.save()
                return Response({"status":1,"message":u"修改成功!"})
            return Response({"status":0,"message":u"验证码错误,请重新输入或者重新获取!"})
        return Response({"status":0,"message":u"字段错误!"})

#用户名片更改
class CallingCardUpdate(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def post(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            return Response({"status":0, "message":u"修改失败!"})
        customer.calling_card = request.data["calling_card"]#名片更改
        customer.save()
        image_path = MEDIA_ROOT+str(customer.calling_card)
        set_picture_pixel(image_path)
        return Response({"status":1, "message":u"修改成功!"})


#用户头像更改
class CustomerAvatarUpdate(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def post(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            return Response({"status":0, "message":u"修改失败!"})
        customer.portrait = request.data["avatar"]#名片更改
        customer.save()
        image_path = MEDIA_ROOT+str(customer.portrait)
        set_picture_pixel(image_path)
        return Response({"status":1, "message":u"修改成功!"})


#检查是否最新版本
class VersionList(APIView):
    def get(self, request, format=None):
        version = Version.objects.all()
        serializer = VersionSerializer(version, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #数据库中只有一组版本数据
        version_latest = Version.objects.all()[0]
        #如果没有更新返回0
        no_update = {'update':0, 'url':'', 'context':''}
        #如果有更新返回1和下载更新的url
        update = {'update':1, 'url':version_latest.url, 'context':version_latest.context}
        if request.data['version']>= version_latest.version:
            return Response(no_update)
        return Response(update)

#根据business_id获取首页中的企业公告以及企业热销产品
class HomePageList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        #如果该用户没有添加客户经理,返回空,以后返回需要返回的内容
        if not request.user.customer.agents.exists():
            return Response(None)

        business_id = request.GET.get("business_id",-1) #如果不传business_id参数,置为-1,返回该用户对应的第一个机构
        try:
            business = Business.objects.get(id=int(business_id))
        except:
            business = Business.objects.filter(agent__customer__user=request.user)[0]
        #首页公告
        announcements = Announcement.objects.filter(announce_business=business, is_active=True)
        announcements_serializer = AnnouncementSerializer(announcements, context={'request':request}, many=True)
        #热销产品
        products = Product.objects.filter(business=business, on_top=True, is_active=True)
        products_serializer = ProductSerializer(products, many=True)
        return Response({'announcements':announcements_serializer.data,
                         'products':products_serializer.data})

#根据business_id获取该企业的所有产品
class AllProductsList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        business_id = request.GET.get("business_id",0)
        if business_id:
            #该企业所有产品
            products = Product.objects.filter(business=int(business_id), is_active=True)
            products_serializer = ProductSerializer(products, many=True)
            return Response(products_serializer.data)
        return Response(None)

#viewset 分页获取头条信息
class HeadlineViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer
    pagination_class = StandardResultsSetPagination

#获取头条详细信息
class HeadlineDetailViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Headline.objects.all()
    serializer_class = HeadlineDetailSerializer
    pagination_class = StandardResultsSetPagination


#如果存在user,将user保存为request.user
class CommentViewSetMixin(object):

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            serializer.save(user=self.request.user, praise=[])

#金融头条评论
class CommentViewSet(CommentViewSetMixin, viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user in instance.praise.all():
            return Response({"status":0, "message":u"已经赞过!"})
        else:
            instance.praise.add(request.user)
            instance.save()
            return Response({"status":1, "message":u"点赞成功!"})

    def list(self, request, *args, **kwargs):
        return Response(None)

    def retrieve(self, request, *args, **kwargs):
        return Response(None)

    #只能删除自己
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user==request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(None)

#分页获取头条信息
# class HeadlineListView(generics.ListAPIView):
#     authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
#     permission_classes = (IsAuthenticated,)
#
#     queryset = Headline.objects.all()
#     serializer_class = HeadlineSerializer
#     pagination_class = StandardResultsSetPagination

# #获取头条信息
# class HeadlineList(APIView):
#     authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request, format=None):
#         headlines = Headline.objects.all()
#         serializers = HeadlineSerializer(headlines, many=True)
#         return Response(serializers.data)

#根据customer_id签到信息处理,每个用户每天只能签到一次,用户可随时查看总的签到数
class CheckinList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # checkins = Checkin.objects.filter(customer__user=request.user).count()
        try:
            checkin = Checkin.objects.get(user=request.user)
        except:
            return Response({'checkin':None})

        today = datetime.datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        #如果今天和昨天都没有签到,连续签到天数为0
        if str(checkin.latest_date)!=today and str(checkin.latest_date)!=yesterday:
            checkin.continuous_days = 0
            checkin.save()
        serializer = CheckinSerializer(checkin)
        return Response({'checkin':serializer.data})


    def post(self, request, format=None):
        abscissa = get_request_data(request, 'abscissa', 0)#经度
        ordinate = get_request_data(request, 'ordinate', 0)#纬度

        result = points_deal(request.user, '3', abscissa=abscissa, ordinate=ordinate)
        if result["status"]:
            return Response({'checkin':1})
        else:
            return Response({'checkin':0, 'message':result["message"]})


#转发添加积分api
class SharePoints(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        points_deal(request.user, '6')
        return Response({'status':1})



#用户密码修改,需要输入旧密码和两次新密码
class PasswordchangeList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        data = request.data
        username = request.user.username
        user = authenticate(username=username, password=data["old_password"])
        if user is not None and user.is_active :
            if data["new_password1"]==data["new_password2"]:
                user.set_password(data["new_password1"])
                user.save()
                return Response({'password_change':1, 'message':u"密码修改成功!"})
            return Response({'password_change':0, 'message':u"两次输入不匹配!"})
        return Response({'password_change':0, 'message':u"旧密码输入错误!"})

class PurchaseViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    #获取与该customer相关的agents
    def get_queryset(self):
        return Purchase.objects.filter(customer__user=self.request.user)

    #重写modelviewset的post方法
    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     data["customer"] = Customer.objects.get(user=request.user).id
    #     serializer = PurchaseSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#用户购买获取和新建
class PurchaseList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        purchases = Purchase.objects.filter(customer__user=request.user)
        serializers = PurchaseSerializer(purchases, many=True)
        return Response(serializers.data)

        # try:
        #     customer = Customer.objects.get(user=request.user)
        #     purchase = Purchase.objects.filter(customer=customer)
        #     serializers = PurchaseSerializer(purchase, many=True)
        #     return Response(serializers.data)
        # except Customer.DoesNotExist:
        #     return Response(None)

    def post(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            return Response(None)
        time = datetime.datetime.now()
        purchase = Purchase(customer=customer, register_time=time)
        serializer = PurchaseSerializer(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

#反馈信息接收,发送邮件
class FeedbackDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            return Response(None)
        id = customer.id
        name = customer.name
        number = customer.phoneNum
        subject = request.data["subject"]
        content = request.data["content"]
        #sender为在收件人邮件中显示的发件人
        sender = 'feedback@niujidui.com'
        #reveivers为收件人的列表，可以发送给多个人
        receivers = ['niujidui@qq.com']
        mail_msg = u'\
        用户编号:%s, 用户姓名:%s, 用户手机号:%s.<br/>\
        反馈内容:%s' % (id, name, number, str(content))
        message = MIMEText(mail_msg, 'html', 'utf-8')
        message['subject'] = str(subject)
        message['from'] = sender
        message['to'] = ", ".join(receivers)
        try:
            smtp = smtplib.SMTP(MAIL_HOST)
            smtp.sendmail(sender, receivers, message.as_string())
            smtp.close()
            return Response("反馈已发送,谢谢您的支持!")
        except:
            return Response("发送失败,请重新发送!")

#验证码获取
class Verification(APIView):
    def get(self, request, format=None):
        phone_number = request.GET.get("phone_number",0)
        #获取验证码的用途,值为"register"或者"forget"
        purpose = request.GET.get("purpose",0)
        if check_CellNumber(phone_number):
            valid_second = ValidSecond.objects.get(id=1).seconds
            codes = VerificationCode.objects.filter(phoneNum=phone_number)
            now = datetime.datetime.now()
            if len(codes)==0 or (time.mktime(now.timetuple())-time.mktime(codes[0].register_date.timetuple())) > valid_second:
                if purpose == "register":
                    result = sms.get_verification_code(phone_number)
                elif purpose == "forget":
                    result = sms.forget_password_code(phone_number)
                elif purpose == "update":
                    result = sms.data_update_code(phone_number)
                else:
                    result = 0

                if result:
                    return Response({"status":1, "message":u'获取成功!'})
                return Response({"status":0, "message":u'获取失败,请重新获取!'})
            return Response({"status":0, "message":u'您已经获取过了,请两分钟分钟后再获取!'})
        return Response({"status":0, "message":u'手机号码格式不正确,请重新输入!'})

#用户app注册
class Register(APIView):
    def post(self, request, format=None):
        data = request.data

        #用户注册
        response = register(data)
        return Response(response)

    
#忘记密码
class ForgetPassword(APIView):
    def post(self, request, format=None):
        data = request.data
        phoneNum = data["phoneNum"]#手机号码
        verification_code = data["verification_code"]#验证码
        password1 = data["password1"]#密码
        password2 = data["password2"]#重复密码
        
        #检查手机号格式
        if check_CellNumber(phoneNum):
            #通过检查手机号查看用户是否存在
            if Customer.objects.filter(phoneNum=phoneNum, customer_type='1') and User.objects.filter(username=phoneNum):
                valid_second = ValidSecond.objects.get(id=1).seconds
                codes = VerificationCode.objects.filter(phoneNum=phoneNum, purpose='1')
                now = datetime.datetime.now()                
                #检查验证码是否正确
                if len(codes)>0 and (now-codes[0].register_date).seconds <= valid_second and verification_code==codes[0].code:
                    #检查两次密码输入是否一致
                    if password1==password2:
                        user = User.objects.get(username=phoneNum)
                        user.set_password(password1)
                        user.save()
                        return Response({"status":1, "message":u'密码修改成功,感谢使用!'})
                    return Response({"status":0, "message":u'两次密码输入不一致,请检查后重新输入,谢谢!'})
                return Response({"status":0, "message":u'验证码无效,请重新输入或者重新获取,谢谢!'})
            return Response({"status":0, "message":u'该手机号不存在,请输入正确的手机号码,谢谢!'})
        return Response({"status":0, "message":u'手机号码格式不正确,请重新输入,谢谢!'})

#通过邀请码获取机构和客户经理信息
class InvitationDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        invitation_code = request.GET.get("invitation_code",0)
        agent = get_agent(invitation_code)
        if agent:
            agent_serializer = AgentSerializer(agent)
            business_serializer = BusinessSerializer(agent.business, context={'request':request})
            return Response({"status":1, "message":{"agent":agent_serializer.data, "business":business_serializer.data}})
        return Response({"status":0, "message":u'邀请码输入错误,请重新输入或者重新获取,谢谢!'})

#机构添加
class AddAgent(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        data = request.data
        agent = Agent.objects.get(id=data["agent_id"])#客户经理

        #检查该机构是否已存在于该用户中
        try:
            customer = Customer.objects.get(user=request.user, agents__business__id=agent.business_id, customer_type='1')
            #如果已经存在
            return Response({"status":0, "message":u'该机构已存在于你的账户中，请检查后重新添加，谢谢!'})
        except:
            #如果不存在，将该客户经理添加到customer中
            customer = Customer.objects.get(user=request.user)
            customer.agents.add(agent)
            customer.save()
            #意向客户的is_active置为False
            customerpendings = Customer.objects.filter(phoneNum=request.user.username, agents=agent, customer_type='2')
            if customerpendings:
                for customerpending in customerpendings:
                    customerpending.is_active=False
                    customerpending.save()
            return Response({"status":1, "message":u'机构添加成功!'})
        
#机构删除
class DeleteAgent(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        data = request.data
        try:
            customer = Customer.objects.get(user=request.user)
            agent = Agent.objects.get(customer=customer, business=data["business_id"])#客户经理
        except:
            return Response({"status":0, "message":u'删除失败，请重新删除!'})
        if len(customer.agents.all()) == 1:
            return Response({"status":0, "message":u'用户至少需要保留一个机构,谢谢!'})
        customer.agents.remove(agent)
        customer.save()
        return Response({"status":1, "message":u'机构删除成功!'})


#url客户经理信息确认
def UrlAgent(request):
    if request.method == "GET":
        invitation_code = request.GET.get("invitation_code", 0)
        agent = get_agent(invitation_code)
        return render_to_response("api/agent_verify.html",locals())

    if request.method == "POST":
        invitation_code = request.GET.get("invitation_code", 0)
        if "register" in request.POST:
            return redirect("/api/url_register/?invitation_code="+invitation_code)
        if "exist" in request.POST:
            return redirect("/api/url_add_agent/?invitation_code="+invitation_code)

#用户url注册
def UrlRegister(request):
    if request.method == "GET":
        invitation_code = request.GET.get("invitation_code",0)
        agent = get_agent(invitation_code)
        form = CaptchaForm()
        # form = CustomerForm()
        # today = datetime.datetime.now().strftime("%Y-%m-%d")
        # form.fields['register_date'].initial = today
        return render_to_response("api/url_register.html",locals(), context_instance=RequestContext(request))

    if request.method == "POST":
        invitation_code = request.GET.get("invitation_code",0)
        form = CaptchaForm(request.POST)
        data = request.POST.copy()
        if form.is_valid():
            data["invitation_code"] = invitation_code
            response = register(data)
            if response["status"]:
                return render_to_response("api/register_success.html", locals())
            else:
                error = "*" + response["message"]
                return render_to_response("api/url_register.html",locals(), context_instance=RequestContext(request))
        error = u'*图中验证码输入错误,请检查后重新输入,谢谢!'
        return render_to_response("api/url_register.html",locals(), context_instance=RequestContext(request))

#用户通过url添加机构
def UrlAddAgent(request):
    if request.method == "GET":
        invitation_code = request.GET.get("invitation_code", 0)
        agent = get_agent(invitation_code)
        form = CaptchaForm()
        if agent:
            return render_to_response("api/url_add_agent.html",locals())
        error = u'*该客户经理不存在'
        return render_to_response("api/url_add_agent.html",locals())

    if request.method == "POST":
        invitation_code = request.GET.get("invitation_code", 0)
        agent = get_agent(invitation_code)
        phoneNum = request.POST["phoneNum"]
        form = CaptchaForm(request.POST)
        if form.is_valid():
            if agent:
                try:
                    #检查该customer是否存在
                    customer = Customer.objects.get(phoneNum=phoneNum, customer_type='1')
                    password = request.POST["password"]
                    user = authenticate(username=phoneNum, password=password)
                    if user is not None and user.is_active :
                        #检查该机构是否已存在于该用户中
                        try:
                            customer = Customer.objects.get(phoneNum=phoneNum, agents__business__id=agent.business_id, customer_type='1')
                            error = u'*该机构已存在于您的账户，请检查后重新添加，谢谢！'
                            return render_to_response("api/url_add_agent.html",locals())
                        except:
                            customer.agents.add(agent)
                            customer.save()
                            #意向客户的is_active置为False
                            customerpendings = Customer.objects.filter(phoneNum=phoneNum, agents=agent, customer_type='2')
                            if customerpendings:
                                for customerpending in customerpendings:
                                    customerpending.is_active=False
                                    customerpending.save()
                            return render_to_response("api/add_success.html")
                except Customer.DoesNotExist:
                    pass

                #如果用户验证不通过或者用户不存在
                error = u'*手机号或密码错误，请检查后重新输入，谢谢！'
                return render_to_response("api/url_add_agent.html",locals())
            error = u'*该客户经理不存在，请确认后重新添加，谢谢！'
            return render_to_response("api/url_add_agent.html",locals())
        error = u'*图中验证码输入错误,请检查后重新输入,谢谢!'
        return render_to_response("api/url_add_agent.html",locals())

#跳转到相应链接进行app下载
def APPDownload(request):
    if request.method == "GET":
        return render_to_response("api/app_download.html")

#登录验证,只有customer可以登录
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if "username" not in request.data:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message":u'请输入手机号!'})
        if "password" not in request.data:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message":u'请输入密码!'})
        customer = Customer.objects.filter(phoneNum=request.data["username"], is_active=True)
        if customer.exists():
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


#客户收藏或者关注时绑定对应客户
class CustomerViewSetMixin(object):

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            try:
                serializer.save(customer=Customer.objects.get(user=self.request.user))
            except Exception, err:
                logger.error(err)

    def update(self, request, *args, **kwargs):
        return Response(None)

#用户收藏viewset
class CollectionViewSet(CustomerViewSetMixin, viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filter_fields = ('product_id',)

    #获取与该customer相关的收藏
    def get_queryset(self):
        return Collection.objects.filter(customer__user=self.request.user)

#用户关注viewset
class AttentionViewSet(CustomerViewSetMixin, viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Attention.objects.all()
    serializer_class = AttentionSerializer
    filter_fields = ('product_id',)

    #获取与该customer相关的关注
    def get_queryset(self):
        return Attention.objects.filter(customer__user=self.request.user)
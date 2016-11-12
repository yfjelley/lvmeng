#! /usr/bin/env python
#coding:utf-8
from django.shortcuts import render
from erp.models import *
from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from models import *
import json, time, logging
import datetime
# import pandas as pd
import numpy as np
# from django_pandas.io import read_frame
from lvmeng.settings import *
from rest_framework import viewsets
from serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
import django_filters
from rest_framework import filters
from rest_framework import generics
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from rest_framework.authentication import *
from rest_framework.permissions import IsAuthenticated
from api.models import *
from localflavor.cn.forms import CNIDCardField, CNCellNumberField
import smtplib
import sms
from erp.forms import *
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from forms import *
import random

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
    if len(code)<6:
        return False
    business_num = code[0:4]
    agent_num = code[4:]
    try:
        agent = Agent.objects.get(business__business_num=business_num, agent_num=agent_num)
        return agent
    except:
        return False

#captcha获取三个数字的验证码
def random_digit_challenge():
    ret = u''
    for i in range(3):
        ret += str(random.randint(0,9))
    return ret, ret

#根据用户提交的信息进行用户注册
def register(data):
    name = data["name"]#姓名
    last_name=u"客户"#admin中user的last_name
    phoneNum = data["phoneNum"]#手机号码
    idCard_num = data["idCard_num"]#身份证号码
    invitation_code = data["invitation_code"]#邀请码
    verification_code = data["verification_code"]#验证码
    password1 = data["password1"]#密码
    # password2 = data["password2"]#重复密码
    agent = get_agent(invitation_code)

    #通过检查手机号查看用户是否存在
    if len(Customer.objects.filter(phoneNum=phoneNum))==0 and len(User.objects.filter(username=phoneNum))==0:
        #检查邀请码
        if agent:
            #检查手机号格式
            if check_CellNumber(phoneNum):
                #检查身份证号码格式
                if check_IDCardNumber(idCard_num):
                    #检查两次密码输入是否一致
                    # if password1==password2:
                    valid_second = ValidSecond.objects.get(id=1).seconds
                    codes = VerificationCode.objects.filter(phoneNum=phoneNum)
                    now = datetime.datetime.now()
                    #检查验证码是否正确
                    if len(codes)>0 and (now-codes[0].register_date).seconds <= valid_second and verification_code==codes[0].code:
                        today = datetime.datetime.now().strftime("%Y-%m-%d")
                        user = User.objects.create_user(username=phoneNum,first_name=name,last_name=last_name,password=password1)#新增用户名和密码
                        user.save()
                        customer = Customer(user=user, name=name, phoneNum=phoneNum, idCard_num=idCard_num, register_date=today)
                        customer.save()
                        customer.agents.add(agent)
                        customer.save()
                        #意向客户的is_active置为False
                        customerpendings = Customer_Pending.objects.filter(phoneNum=phoneNum, agents=agent)
                        if customerpendings:
                            for customerpending in customerpendings:
                                customerpending.is_active=False
                                customerpending.save()
                        return {"status":1, "message":u'恭喜注册成功!感谢使用!'}
                    return {"status":0, "message":u'手机验证码无效,请重新输入或者重新获取,谢谢!'}
                    # return {"status":0, "message":u'两次密码输入不一致,请检查后重新输入,谢谢!'}
                return {"status":0, "message":u'身份证号码无效,请重新输入,谢谢!'}
            return {"status":0, "message":u'手机号码格式不正确,请重新输入,谢谢!'}
        return {"status":0, "message":u'邀请码不正确,请重新输入或者重新获取,谢谢!'}
    return {"status":0, "message":u'该手机号已经存在,请换一个手机号码注册或者登陆后添加机构,谢谢!'}

# Create your views here.
#product view for rest api
class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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

class BusinessViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    #获取和该customer相关的所有business
    def get_queryset(self):
        #使用foreign key反向查询实现
        return Business.objects.filter(agent__customer__user=self.request.user)
        # businesses = Business.objects.filter(agent__customer__user=self.request.user)
        # return list(set(businesses))

        #普通方法实现
        # try:
        #     customer = Customer.objects.get(user=self.request.user)
        #     agents = customer.agents.all()
        #     businesses = []
        #     for agent in agents:
        #         businesses.append(agent.business)
        #     #由于一个机构包含多个理财师,所以使用list(set())去掉list的重复项
        #     return list(set(businesses))
        # except Customer.DoesNotExist:
        #     return None

    #todo: add get_queryset later to limit query

class AgentViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    #获取与该customer相关的agents
    def get_queryset(self):
        return Agent.objects.filter(customer__user=self.request.user)

        # try:
        #     customer = Customer.objects.get(user=self.request.user)
        #     agents = customer.agents.all()
        #     return agents
        # except Customer.DoesNotExist:
        #     return None


    #todo: add get_queryset later to limit query

class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    #this limits it only get objects related with itself
    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)#only get self user

#用户基本信息修改,只能修改除了手机号码,关联的user,是否有效,注册日期和理财师之外的其他信息
class CustomerupdateDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def get(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response(None)

    def put(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user)
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                if check_IDCardNumber(str(request.data["idCard_num"])):
                    customer.name = request.data["name"]
                    customer.sex = request.data["sex"]
                    customer.address = request.data["address"]
                    customer.idCard_num = request.data["idCard_num"]
                    customer.note = request.data["note"]
                    customer.industry = request.data["industry"]
                    customer.city = request.data["city"]
                    customer.company = request.data["company"]
                    customer.risk_preference = request.data["risk_preference"]
                    customer.email = request.data["email"]
                    customer.calling_card = request.data["calling_card"]
                    customer.save()
                    user = request.user
                    user.first_name = request.data["name"]
                    user.save()
                    # serializer = CustomerSerializer(customer)
                    return Response({"status":1,"message":u"修改成功!"})
                return Response({"status":0,"message":u"身份证号码无效!"})
            return Response({"status":0,"message":serializer.errors})
        except Customer.DoesNotExist:
            return Response(None)

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
        business_id = request.GET.get("business_id")
        if business_id:
            #首页公告
            announcements = Announcement.objects.filter(announce_business=int(business_id))
            announcements_serializer = AnnouncementSerializer(announcements, context={'request':request}, many=True)
            #热销产品
            products = Product.objects.filter(business=int(business_id), on_top=True)
            products_serializer = ProductSerializer(products, many=True)
            return Response({'announcements':announcements_serializer.data,
                             'products':products_serializer.data})
        return Response(None)

#根据business_id获取该企业的所有产品
class AllProductsList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        business_id = request.GET.get("business_id")
        if business_id:
            #该企业所有产品
            products = Product.objects.filter(business=int(business_id))
            products_serializer = ProductSerializer(products, many=True)
            return Response(products_serializer.data)
        return Response(None)

#viewset 分页获取头条信息
class HeadlineViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer
    pagination_class = StandardResultsSetPagination

#分页获取头条信息
class HeadlineListView(generics.ListAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer
    pagination_class = StandardResultsSetPagination

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
        checkins = Checkin.objects.filter(customer__user=request.user).count()
        return Response({'checkin_all':checkins})

        # try:
        #     customer = Customer.objects.get(user=request.user)
        #     #该用户所有签到
        #     checkins = Checkin.objects.filter(customer=customer).count()
        #     return Response({'checkin_all':checkins})
        # except Customer.DoesNotExist:
        #     return Response(None)

    def post(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user)
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            #判断今天是否签到过
            try:
                checkin = Checkin.objects.get(customer=customer, register_date=today)
                return Response({'checkin':0})
            except:
                checkin = Checkin(customer=customer, register_date=today)
                checkin.save()
                return Response({'checkin':1})
        except Customer.DoesNotExist:
            return Response(None)

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
            time = datetime.datetime.now()
            purchase = Purchase(customer=customer, register_time=time)
            serializer = PurchaseSerializer(purchase, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Customer.DoesNotExist:
            return Response(None)

#反馈信息接收,发送邮件
class FeedbackDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        try:
            customer = Customer.objects.get(user=request.user)
            id = customer.id
            name = customer.name
            number = customer.phoneNum
            subject = request.data["subject"]
            content = request.data["content"]
            #sender为在收件人邮件中显示的发件人
            sender = 'feedback@niujidui.com'
            #reveivers为收件人的列表，可以发送给多个人
            receivers = ['feedback@niujidui.com']

            #message为发送邮件的主题和正文
            message = """From: lvmeng <feedback@niujidui.com>
To: To lvmeng <feedback@niujidui.com>
Subject: %s

用户编号:%s, 用户姓名:%s, 用户手机号:%s.
反馈内容:%s
""" % (subject,id, name, number, content)
            #发件人服务器
            username = 'feedback@niujidui.com'
            password = 'Lvmeng1234'
            smtp = smtplib.SMTP()
            smtp.connect('smtp.niujidui.com')
            smtp.login(username, password)
            smtp.sendmail(sender, receivers, message)
            return Response("反馈已发送,谢谢您的支持!")
        except Customer.DoesNotExist:
            return Response(None)

#验证码获取
class Verification(APIView):
    def get(self, request, format=None):
        phone_number = request.GET.get("phone_number")
        #获取验证码的用途,值为"register"或者"forget"
        purpose = request.GET.get("purpose")
        if check_CellNumber(phone_number):
            valid_second = ValidSecond.objects.get(id=1).seconds
            codes = VerificationCode.objects.filter(phoneNum=phone_number)
            now = datetime.datetime.now()
            if len(codes)==0 or (time.mktime(now.timetuple())-time.mktime(codes[0].register_date.timetuple())) > valid_second:
                if purpose == "register":
                    result = sms.get_verification_code(phone_number)
                elif purpose == "forget":
                    result = sms.forget_password_code(phone_number)
                else:
                    result = 0

                if result:
                    return Response({"status":1, "message":u'获取成功!'})
                return Response({"status":0, "message":u'获取失败,请重新获取!'})
            return Response({"status":0, "message":u'您已经获取过了,请五分钟后再获取!'})
        return Response({"status":0, "message":u'手机号码格式不正确,请重新输入!'})

#用户app注册
class Register(APIView):
    def post(self, request, format=None):
        data = request.data
        # name = data["name"]#姓名
        # last_name=u"客户"#admin中user的last_name
        # phoneNum = data["phoneNum"]#手机号码
        # idCard_num = data["idCard_num"]#身份证号码
        # invitation_code = data["invitation_code"]#邀请码
        # verification_code = data["verification_code"]#验证码
        # password1 = data["password1"]#密码
        # password2 = data["password2"]#重复密码
        # agent = get_agent(invitation_code)

        #用户注册
        response = register(data)
        return Response(response)

        # #通过检查手机号查看用户是否存在
        # if len(Customer.objects.filter(phoneNum=phoneNum))==0 and len(User.objects.filter(username=phoneNum))==0:
        #     #检查邀请码
        #     if agent:
        #         #检查手机号格式
        #         if check_CellNumber(phoneNum):
        #             #检查身份证号码格式
        #             if check_IDCardNumber(idCard_num):
        #                 #检查两次密码输入是否一致
        #                 if password1==password2:
        #                     valid_second = ValidSecond.objects.get(id=1).seconds
        #                     codes = VerificationCode.objects.filter(phoneNum=phoneNum)
        #                     now = datetime.datetime.now()
        #                     #检查验证码是否正确
        #                     if len(codes)>0 and (now-codes[0].register_date).seconds <= valid_second and verification_code==codes[0].code:
        #                         today = datetime.datetime.now().strftime("%Y-%m-%d")
        #                         user = User.objects.create_user(username=phoneNum,first_name=name,last_name=last_name,password=password1)#新增用户名和密码
        #                         user.save()
        #                         customer = Customer(user=user, name=name, phoneNum=phoneNum, idCard_num=idCard_num, register_date=today)
        #                         customer.save()
        #                         customer.agents.add(agent)
        #                         customer.save()
        #                         return Response({"status":1, "message":u'恭喜注册成功!感谢使用!'})
        #                     return Response({"status":0, "message":u'验证码无效,请重新输入或者重新获取,谢谢!'})
        #                 return Response({"status":0, "message":u'两次密码输入不一致,请检查后重新输入,谢谢!'})
        #             return Response({"status":0, "message":u'身份证号码无效,请重新输入,谢谢!'})
        #         return Response({"status":0, "message":u'手机号码格式不正确,请重新输入,谢谢!'})
        #     return Response({"status":0, "message":u'邀请码不正确,请重新输入或者重新获取,谢谢!'})
        # return Response({"status":0, "message":u'该手机号已经存在,请换一个手机号码注册或者登陆后添加机构,谢谢!'})
    
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
            if Customer.objects.filter(phoneNum=phoneNum) and User.objects.filter(username=phoneNum):
                valid_second = ValidSecond.objects.get(id=1).seconds
                codes = VerificationCode.objects.filter(phoneNum=phoneNum)
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

#通过邀请码获取机构和理财师信息
class InvitationDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        invitation_code = request.GET.get("invitation_code")
        agent = get_agent(invitation_code)
        if agent:
            agent_serializer = AgentSerializer(agent)
            business_serializer = BusinessSerializer(agent.business)
            return Response({"status":1, "message":{"agent":agent_serializer.data, "business":business_serializer.data}})
        return Response({"status":0, "message":u'邀请码输入错误,请重新输入或者重新获取,谢谢!'})

#机构添加
class AddAgent(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        data = request.data
        agent = Agent.objects.get(id=data["agent_id"])#理财师

        #检查该机构是否已存在于该用户中
        try:
            customer = Customer.objects.get(user=request.user, agents__business__id=agent.business_id)
            #如果已经存在
            return Response({"status":0, "message":u'该机构已存在于你的账户中，请检查后重新添加，谢谢!'})
        except:
            #如果不存在，将该理财师添加到customer中
            customer = Customer.objects.get(user=request.user)
            customer.agents.add(agent)
            customer.save()
            #意向客户的is_active置为False
            customerpendings = Customer_Pending.objects.filter(phoneNum=request.user.username, agents=agent)
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
            agent = Agent.objects.get(customer=customer, business=data["business_id"])#理财师
            customer.agents.remove(agent)
            customer.save()
            return Response({"status":1, "message":u'机构删除成功!'})
        except:
            return Response({"status":0, "message":u'删除失败，请重新删除!'})

#url理财师信息确认
def UrlAgent(request):
    if request.method == "GET":
        invitation_code = request.GET.get("invitation_code", "")
        agent = get_agent(invitation_code)
        return render_to_response("api/agent_verify.html",locals())

    if request.method == "POST":
        invitation_code = request.GET.get("invitation_code")
        if "register" in request.POST:
            return redirect("/api/url_register/?invitation_code="+invitation_code)
        if "exist" in request.POST:
            return redirect("/api/url_add_agent/?invitation_code="+invitation_code)

#用户url注册
def UrlRegister(request):
    if request.method == "GET":
        invitation_code = request.GET.get("invitation_code")
        agent = get_agent(invitation_code)
        form = CaptchaForm()
        # form = CustomerForm()
        # today = datetime.datetime.now().strftime("%Y-%m-%d")
        # form.fields['register_date'].initial = today
        return render_to_response("api/url_register.html",locals(), context_instance=RequestContext(request))

    if request.method == "POST":
        invitation_code = request.GET.get("invitation_code")
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
        invitation_code = request.GET.get("invitation_code", "")
        agent = get_agent(invitation_code)
        form = CaptchaForm()
        if agent:
            return render_to_response("api/url_add_agent.html",locals())
        error = u'*该理财师不存在'
        return render_to_response("api/url_add_agent.html",locals())

    if request.method == "POST":
        invitation_code = request.GET.get("invitation_code", "")
        agent = get_agent(invitation_code)
        phoneNum = request.POST["phoneNum"]
        form = CaptchaForm(request.POST)
        if form.is_valid():
            if agent:
                try:
                    #检查该customer是否存在
                    customer = Customer.objects.get(phoneNum=phoneNum)
                    password = request.POST["password"]
                    user = authenticate(username=phoneNum, password=password)
                    if user is not None and user.is_active :
                        #检查该机构是否已存在于该用户中
                        try:
                            customer = Customer.objects.get(phoneNum=phoneNum, agents__business__id=agent.business_id)
                            error = u'*该机构已存在于您的账户，请检查后重新添加，谢谢！'
                            return render_to_response("api/url_add_agent.html",locals())
                        except:
                            customer.agents.add(agent)
                            customer.save()
                            return render_to_response("api/add_success.html")
                except Customer.DoesNotExist:
                    pass

                #如果用户验证不通过或者用户不存在
                error = u'*手机号或密码错误，请检查后重新输入，谢谢！'
                return render_to_response("api/url_add_agent.html",locals())
            error = u'*该理财师不存在，请确认后重新添加，谢谢！'
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
        customer = Customer.objects.filter(phoneNum=request.data["username"])
        if customer.exists():
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
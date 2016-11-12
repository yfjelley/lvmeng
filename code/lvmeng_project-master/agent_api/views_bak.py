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
from api.views import check_IDCardNumber, check_CellNumber
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
import smtplib
from models import *

#发送email
def send_email(agent, subject, content, receivers):
    subject = subject
    content = content
    #sender为在收件人邮件中显示的发件人
    sender = 'feedback@niujidui.com'
    #reveivers为收件人的列表，可以发送给多个人
    # receivers = ['feedback@niujidui.com']
    to_receivers = ""
    for receiver in receivers:
        to_receivers += "<" + receiver + ">;"

    #message为发送邮件的主题和正文
    message = """From:%s <%s>
To: %s
Subject: %s

%s
""" % (agent.name, agent.email if agent.email else sender, to_receivers, subject, content)
    #发件人服务器
    username = 'feedback@niujidui.com'
    password = 'Lvmeng1234'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.niujidui.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receivers, message)
    smtp.quit()

#根据不同类型新增不同的审批
def create_examine(data, type):

    for euser in data.examine_user.all():
        #费用申请审批
        if type=="cost":
            cost_examine = Cost_examine(examine_business=data.cost_business, examine_user=euser, cost_examine=data)
            cost_examine.save()

        #请假申请审批
        if type=="leave":
            leave_examine = Leave_examine(examine_business=data.leave_business, examine_user=euser, leave_examine=data)
            leave_examine.save()

        #出差申请审批
        if type=="travel":
            travel_examine = Travel_examine(examine_business=data.travel_business, examine_user=euser, travel_examine=data)
            travel_examine.save()

#给意向客户群发邮件
class MailToAllPengdingCustomers(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        agent = Agent.objects.get(user=request.user)
        pcustomers_id = data["pcustomers_id"]
        pcustomers = []
        receivers = []
        for id in pcustomers_id:
            pcustomer = Customer_Pending.objects.get(id=id)
            pcustomers.append(pcustomer)
            if pcustomer.email:
                receivers.append(pcustomer.email)
        if len(receivers) > 0:
            send_email(agent=agent, subject=data["subject"], content=data["content"], receivers=receivers)
            return Response({"status":1, "message":u"发送成功!"})
        return Response({"status":0, "message":u"所选用户没有email信息!"})

#给意向客户群发邮件
class MailToCustomers(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        agent = Agent.objects.get(user=request.user)
        customers_id = data["customers_id"]
        customers = []
        receivers = []
        for id in customers_id:
            customer = Customer.objects.get(id=id)
            customers.append(customer)
            if customer.email:
                receivers.append(customer.email)
        if len(receivers) > 0:
            send_email(agent=agent, subject=data["subject"], content=data["content"], receivers=receivers)
            return Response({"status":1, "message":u"发送成功!"})
        return Response({"status":0, "message":u"所选用户没有email信息!"})

#product view for rest api
class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(business__agent__user=self.request.user)#only get self products

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

class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = StandardResultsSetPagination

    # #this limits it only get objects related with itself
    def get_queryset(self):
        return Customer.objects.filter(agents__user=self.request.user)

class AgentViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    # #this limits it only get objects related with itself
    def get_queryset(self):
        return Agent.objects.filter(business__agent__user=self.request.user)

#理财师基本信息修改,只能修改除了机构编号,理财师编号,手机号码,关联的user,是否有效,注册日期,录入人之外的其他信息
class AgentupdateDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def get(self, request, format=None):
        try:
            agent = Agent.objects.get(user=request.user)
            serializer = AgentSerializer(agent, context={'request':request})
            return Response(serializer.data)
        except Agent.DoesNotExist:
            return Response(None)

    def put(self, request, format=None):
        try:
            agent = Agent.objects.get(user=request.user)
            serializer = AgentSerializer(agent, data=request.data)
            if serializer.is_valid():
                if check_IDCardNumber(str(request.data["idCard_num"])):
                   agent.name = request.data["name"]
                   agent.sex = request.data["sex"]
                   agent.address = request.data["address"]
                   agent.idCard_num = request.data["idCard_num"]
                   agent.note = request.data["note"]
                   # agent.avatar = request.data["avatar"]#头像更改用单独api
                   agent.email  = request.data["email"]
                   agent.save()
                   user = request.user
                   user.first_name = request.data["name"]
                   user.save()
                   return Response({"status":1, "message":u"修改成功!"})
                return Response({"status":0, "message":u"身份证号码无效!"})
            return Response({"status":0, "message":serializer.errors})
        except Agent.DoesNotExist:
            return Response(None)

#理财师头像更改api
class AgentAvatarUpdate(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def put(self, request, format=None):
        try:
            agent = Agent.objects.get(user=request.user)
            agent.avatar = request.data["avatar"]#头像更改
            agent.save()
            return Response({"status":1, "message":u"修改成功!"})
        except Agent.DoesNotExist:
            return Response({"status":0, "message":u"修改失败!"})

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
        #理财师所属公司信息
        business = Business.objects.filter(agent__user=request.user)
        business_serializer = BusinessSerializer(business, context={'request':request}, many=True)
        #首页公告
        announcements = Announcement.objects.filter(announce_business=business)
        announcements_serializer = AnnouncementSerializer(announcements, context={'request':request}, many=True)
        #热销产品
        products = Product.objects.filter(business=business, on_top=True)
        products_serializer = ProductSerializer(products, many=True)
        return Response({'announcements':announcements_serializer.data,
                         'business':business_serializer.data,
                         'products':products_serializer.data})

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

#获取该理财师名下某客户在该公司的所有购买
class PurchasesList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        customer_id = request.GET.get("customer_id")
        if customer_id:
            business = Business.objects.filter(agent__user=request.user)
            purchases = Purchase.objects.filter(customer=customer_id, product__business=business)
            serializer = PurchaseSerializer(purchases, many=True)
            return  Response(serializer.data)
        return Response(None)

#登录验证,只有agent可以登录
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        agent = Agent.objects.filter(phoneNum=request.data["username"])
        if agent.exists():
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

#考勤记录,在CheckWork中更新,在CheckWork_history中增加
class CheckWorkView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        now = datetime.datetime.now()
        agent = Agent.objects.get(user=user)
        abscissa = request.data["abscissa"]
        ordinate = request.data["ordinate"]

        #添加到CheckWork_history
        checkhis = CheckWork_history(check_history=user, check_business_history=agent.business, abscissa=abscissa, ordinate=ordinate, check_time=now)
        checkhis.save()

        #更新CheckWork,若存在,更新,否则新增
        try:
            checkwork = CheckWork.objects.get(check_user=user)
            checkwork.abscissa = abscissa
            checkwork.ordinate = ordinate
            checkwork.check_time = now
            checkwork.save()
        except:
            checkwork = CheckWork(check_user=user, check_business=agent.business, abscissa=abscissa, ordinate=ordinate, check_time=now)
            checkwork.save()

        return Response({"status":1, "message":u'更新成功!'})

#内部公告viewset
class InternalAnnouncementViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Internal_announcement.objects.all()
    serializer_class = InternalAnnouncementSerializer

    def get_queryset(self):
        return Internal_announcement.objects.filter(announcement_business__agent__user=self.request.user)#only get self

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        #如果未读添加已读状态
        if not Read_message.objects.filter(read_user=self.request.user, model_name='internal_announcement', record_id=instance.id):
            read_message = Read_message(read_business=instance.announcement_business, read_user=self.request.user, model_name='internal_announcement', record_id=instance.id, read_time=datetime.datetime.now())
            read_message.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

#工作汇报
class DailyWorkViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Daily_work.objects.all()
    serializer_class = DailyWorkSerializer

    def get_queryset(self):
        return Daily_work.objects.filter(daily_user=self.request.user)#only get self

#费用申请
class CostApplicationViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Cost_application.objects.all()
    serializer_class = CostApplicationSerializer

    def get_queryset(self):
        return Cost_application.objects.filter(cost_user=self.request.user)#only get self

    #新增申请的同时要新增审批
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        cost_application = Cost_application.objects.get(id=serializer.data["id"])
        create_examine(cost_application, "cost")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#请假申请
class LeaveManagementViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Leave_management.objects.all()
    serializer_class = LeaveManagementSerializer

    def get_queryset(self):
        return Leave_management.objects.filter(leave_user=self.request.user)#only get self

    #新增申请的同时要新增审批
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        leave_application = Leave_management.objects.get(id=serializer.data["id"])
        create_examine(leave_application, "leave")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#出差申请
class TravelApplyViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Travel_apply.objects.all()
    serializer_class = TravelApplySerializer

    def get_queryset(self):
        return Travel_apply.objects.filter(travel_user=self.request.user)#only get self

    #新增申请的同时要新增审批
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        travel_application = Travel_apply.objects.get(id=serializer.data["id"])
        create_examine(travel_application, "travel")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#意向客户
class CustomerPendingViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Customer_Pending.objects.all()
    serializer_class = CustomerPendingSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Customer_Pending.objects.filter(agents__user=self.request.user)#only get self

#客户转移
class CustomerDeliver(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        customer = Customer.objects.get(id=data["customer_id"])
        from_agent = Agent.objects.get(user=request.user)
        to_agent = Agent.objects.get(id=data["agent_id"])
        customer.agents.remove(from_agent)
        customer.agents.add(to_agent)
        customer.save()
        if customer.email:
            content=u"""尊敬的客户:
您好:
   您的牛基队账户%s机构的理财师已从%s更改为%s,请登录牛基队客户端进行查看,若您存在疑问,请联系您的理财师.
   感谢您的使用!
理财师:%s
电话:%s
%s
""" % (from_agent.business.name, from_agent.name, to_agent.name, from_agent.name, from_agent.phoneNum, datetime.datetime.now().strftime("%F %T"))
            send_email(agent=from_agent, subject=u"理财师更换", content=content, receivers=[customer.email])
        return Response({"status":1, "message":u"转移成功!"})

#理财师和客户通话记录
class CellRecordsCustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Cell_Records_Customer.objects.all()
    serializer_class = CellRecordsCustomerSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Cell_Records_Customer.objects.filter(agent__user=self.request.user)#only get self

#理财师和意向客户通话记录
class CellRecordsPCustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Cell_Records_PCustomer.objects.all()
    serializer_class = CellRecordsPCustomerSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Cell_Records_PCustomer.objects.filter(agent__user=self.request.user)#only get self

#每日待办
class DailyToDoViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Daily_to_do.objects.all()
    serializer_class = DailyToDoSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Daily_to_do.objects.filter(todo_user=self.request.user)#only get self

#反馈信息接收,发送邮件
class FeedbackDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        try:
            agent = Agent.objects.get(user=request.user)
            id = agent.id
            name = agent.name
            number = agent.phoneNum
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

理财师编号:%s, 理财师姓名:%s, 理财师手机号:%s.
反馈内容:%s
""" % (subject, id, name, number, content)
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
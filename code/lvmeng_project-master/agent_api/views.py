#! /usr/bin/env python
#coding:utf-8
from operator import attrgetter
from itertools import chain
import json, time, logging
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# import pandas as pd
import numpy as np
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# from django_pandas.io import read_frame
from django.http import Http404
import django_filters
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.mail.message import EmailMessage
from django.shortcuts import _get_queryset
from rest_framework.authentication import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from localflavor.cn.forms import CNIDCardField, CNCellNumberField

from lvmeng.settings import *
from api.models import *
from api.views import check_IDCardNumber, check_CellNumber, set_picture_pixel, get_request_data
from models import *
from models import *
from erp.models import *
from api.views import get_agent
from lvmeng.settings import *

import logging
logger = logging.getLogger(__name__)

#agent二维码测试
def qrcode_test(request):
    if request.method == "GET":
        agent = Agent.objects.all()[-1]
        agent.create_qrcode(request)
        return render_to_response("agent_api/app_download.html")

#django email测试
def django_email_test(request):
    if request.method == "GET":
        from django.core.mail.message import EmailMessage

        body = '''
        body
        body.
        '''
        file = Agent.objects.get(phoneNum="13520404522").avatar.path
        msg = EmailMessage(subject="subject", body=body, to=['819493212@qq.com'])
        msg.attach_file(file) # self.my_filefield.path for Django 1.7+
        msg.send(fail_silently=not(DEBUG))

        # from django.core.mail import send_mail
        # send_mail('subject', 'message', 'niujidui@niujidui.com', ['819493212@qq.com'], fail_silently=False)
        return HttpResponse("ok")


#通过django发送email
def django_send_email(agent, subject, content, receivers, file_id=None):

    #message为发送邮件的主题和正文
    content = content + u'''


客户经理:%s
所属机构:%s
手机号:%s
邮箱:%s
%s
本邮件是由客户经理发送,若有疑问请直接拨打客户经理的电话，请不要直接回复本邮件！
''' % (agent.name, agent.business.name, agent.phoneNum, agent.email, datetime.datetime.now().strftime("%F %T"))

    msg = EmailMessage(subject=subject, body=content, to=receivers)
    if file_id:
        try:
            file = Temporary_File.objects.get(id=file_id, user=agent.user)
            msg.attach_file(file.file.path)
        except Exception, err:
            pass

    try:
        msg.send(fail_silently=not(DEBUG))
        return True
    except Exception, err:
        logger.error(err)
        return False


#发送email
def send_email(agent, subject, content, receivers):
    #sender为在收件人邮件中显示的发件人
    # sender = agent.email if agent.email else 'niujidui@niujidui.com'
    sender = 'niujidui@niujidui.com'
    #reveivers为收件人的列表，可以发送给多个人
    # receivers = ['feedback@niujidui.com']

    #message为发送邮件的主题和正文
    content = content + u'''<br/><br/>
    客户经理:%s<br/>
    所属机构:%s<br/>
    手机号:%s<br/>
    邮箱:%s<br/>
    %s<br/>
    本邮件是由客户经理发送,若有疑问请直接拨打客户经理的电话，请不要直接回复本邮件！
    ''' % (agent.name, agent.business.name, agent.phoneNum, agent.email, datetime.datetime.now().strftime("%F %T"))

    message = MIMEText(content, 'html', 'utf-8')
    message['subject'] = str(subject)
    message['from'] = sender
    message['to'] = ", ".join(receivers)
    #发件人服务器
    try:
        smtp = smtplib.SMTP(MAIL_HOST)
        smtp.sendmail(sender, receivers, message.as_string())
        return True
    except Exception, err:
        logger.error(err)
        return False

# #从request.data中获取数据,没有返回空
# def get_request_data(request, value, default=None):
#     return request.data[value] if value in request.data else default


#获取对应model的数据,没有返回错误
def get_object_or_error(klass, *args, **kwargs):
    """
    Uses get() to return an object, or raises a Http404 exception if the object
    does not exist.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the get() query.

    Note: Like with get(), an MultipleObjectsReturned will be raised if more than one
    object is found.
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise Http404()


#根据不同类型新增不同的审批
def create_examine(data):

    for euser in data.examine_user.all():
        examine = All_Examine(examine_business=data.business, examine_user=euser, examine=data)
        examine.save()
        # #费用申请审批
        # if type=="cost":
        #     examine = All_Examine(examine_business=data.business, examine_user=euser, examine=data)
        #     examine.save()
        #
        # #请假申请审批
        # if type=="leave":
        #     examine = All_Examine(examine_business=data.business, examine_user=euser, examine=data)
        #     examine.save()
        #
        # #出差申请审批
        # if type=="travel":
        #     examine = All_Examine(examine_business=data.business, examine_user=euser, examine=data)
        #     examine.save()

#根据要删除的申请删除对应的审批
def delete_examine(instance):
    contenttype_obj = ContentType.objects.get_for_model(instance)
    examines = All_Examine.objects.filter(object_id=instance.id, content_type=contenttype_obj)
    for examine in examines:
        examine.delete()


#如果存在agent,将agent保存为request的agent
class AgentViewSetMixin(object):

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            try:
                serializer.save(agent=Agent.objects.get(user=self.request.user))
            except Exception, err:
                logger.error(err)
        # return super(AgentViewSetMixin, self).perform_create(serializer)


#如果存在user,将user保存为request.user
class UserViewSetMixin(object):

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            serializer.save(user=self.request.user)


#客户经理提交申请时绑定user和business
class ApplicationViewSetMixin(object):

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            try:
                serializer.save(user=self.request.user, business=Business.objects.get(agent__user=self.request.user))
            except Exception, err:
                logger.error(err)


#客户经理添加真实购买绑定对应的agent和business
class PurchaseViewSetMixin(object):

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            try:
                serializer.save(real_agent=Agent.objects.get(user=self.request.user), business=Business.objects.get(agent__user=self.request.user))
            except Exception, err:
                logger.error(err)


class TemporaryFileViewSet(UserViewSetMixin, viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Temporary_File.objects.all()
    serializer_class = TemporaryFileSerializer

    def get_queryset(self):
        return Temporary_File.objects.filter(user=self.request.user)#only get self

    def update(self, request, *args, **kwargs):
        return Response(None)

#给特定邮箱发送email
class EmailSend(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        agent = get_object_or_error(Agent, user=request.user)
        receivers = get_request_data(request, "receivers")
        subject = get_request_data(request, "subject")
        content = get_request_data(request, "content")
        file_id = get_request_data(request, "file_id")

        if receivers and subject and content:
            if django_send_email(agent=agent, subject=subject, content=content, receivers=receivers, file_id=file_id):
                return Response({"status":1, "message":u"发送成功!"})
            else:
                return Response({"status":0, "message":u"发送失败,请重新发送!"})
        else:
            return Response({"status":0, "message":u"信息填写不正确!"})


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
            try:
                pcustomer = Customer.objects.get(id=id, agents=agent, is_active=True, customer_type='2')
            except:
                return Response({"status":0, "message":u"不存在该意向客户!"})
            pcustomers.append(pcustomer)
            if pcustomer.email:
                receivers.append(pcustomer.email)

        if 'file_id' in data:
            file_id = data['file_id']
        else:
            file_id = None

        if len(receivers) > 0:
            # send_email(agent=agent, subject=data["subject"], content=data["content"], receivers=receivers)
            if django_send_email(agent=agent, subject=data["subject"], content=data["content"], receivers=receivers, file_id=file_id):
                return Response({"status":1, "message":u"发送成功!"})
            else:
                return Response({"status":0, "message":u"发送失败,请重新发送!"})
        return Response({"status":0, "message":u"所选用户没有email信息!"})

#给真实客户群发邮件
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
            try:
                customer = Customer.objects.get(id=id, agents=agent, customer_type='1', is_active=True)
            except:
                return Response({"status":0, "message":u"不存在该客户!"})
            customers.append(customer)
            if customer.email:
                receivers.append(customer.email)

        if 'file_id' in data:
            file_id = data['file_id']
        else:
            file_id = None

        if len(receivers) > 0:
            # send_email(agent=agent, subject=data["subject"], content=data["content"], receivers=receivers, file_id=file_id)
            if django_send_email(agent=agent, subject=data["subject"], content=data["content"], receivers=receivers, file_id=file_id):
                return Response({"status":1, "message":u"发送成功!"})
            else:
                return Response({"status":0, "message":u"发送失败,请重新发送!"})
        return Response({"status":0, "message":u"所选用户没有email信息!"})

#product filters for rest api
class ProductFilter(filters.FilterSet):
    min_return_expected = django_filters.NumberFilter(name="return_expected", lookup_type='gte')
    max_return_expected = django_filters.NumberFilter(name="return_expected", lookup_type='lte')
    min_period = django_filters.NumberFilter(name="period", lookup_type='gte')
    max_period = django_filters.NumberFilter(name="period", lookup_type='lte')

    class Meta:
        model = Product
        fields = ['product_type', 'return_expected', 'period', 'min_return_expected', 'max_return_expected', 'min_period', 'max_period']

#product view for rest api
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('product_type',)
    filter_class = ProductFilter

    def get_queryset(self):
        return Product.objects.filter(business__agent__user=self.request.user, is_active=True)#only get self products

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

class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = StandardResultsSetPagination

    # #this limits it only get objects related with itself
    def get_queryset(self):
        return Customer.objects.filter(agents__user=self.request.user, customer_type='1', is_active=True)


class AddressCustomerViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    queryset = Customer.objects.all()
    serializer_class = AddressCustomerSerializer
    pagination_class = StandardResultsSetPagination

    # #this limits it only get objects related with itself
    def get_queryset(self):
        return Customer.objects.filter(agents__user=self.request.user, is_active=True)


class AgentViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    queryset = Agent.objects.all()
    serializer_class = AgentSimpleSerializer

    # #this limits it only get objects related with itself
    def get_queryset(self):
        return Agent.objects.filter(business__agent__user=self.request.user, is_active=True).exclude(user=self.request.user)

#理财师基本信息修改,只能修改除了机构编号,理财师编号,手机号码,关联的user,是否有效,注册日期,录入人之外的其他信息
class AgentupdateDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def get(self, request, format=None):
        try:
            agent = Agent.objects.get(user=request.user)
        except Agent.DoesNotExist:
            return Response(None)
        serializer = AgentSerializer(agent, context={'request':request})
        return Response(serializer.data)

    def put(self, request, format=None):
        try:
            agent = Agent.objects.get(user=request.user)
        except Agent.DoesNotExist:
            return Response(None)
        # serializer = AgentSerializer(agent, data=request.data)
        # if serializer.is_valid():

        if "name" in request.data:
            agent.name = request.data["name"]
        if "sex" in request.data:
            agent.sex = request.data["sex"]
        if "address" in request.data:
            agent.address = request.data["address"]
        if "idCard_num" in request.data:
            if check_IDCardNumber(str(request.data["idCard_num"])):
                agent.idCard_num = request.data["idCard_num"]
            else:
                return Response({"status":0, "message":u"身份证号码无效!"})
        if "note" in request.data:
            agent.note = request.data["note"]
         # agent.avatar = request.data["avatar"]#头像更改用单独api
        # agent.email  = request.data["email"]
        agent.save()
        user = request.user
        user.first_name = request.data["name"]
        user.save()
        return Response({"status":1, "message":u"修改成功!"})
        # return Response({"status":0, "message":serializer.errors})


#客户经理头像更改api
class AgentAvatarUpdate(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def post(self, request, format=None):
        try:
            agent = Agent.objects.get(user=request.user)
            agent.avatar = request.data["avatar"]#头像更改
            agent.save()
            image_path = MEDIA_ROOT+str(agent.avatar)
            set_picture_pixel(image_path)
            return Response({"status":1, "message":u"修改成功!"})
        except Agent.DoesNotExist:
            return Response({"status":0, "message":u"修改失败!"})


#客户经理邮箱更改验证
class EamilUpdate(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def post(self, request, format=None):
        try:
            agent = Agent.objects.get(user=request.user, is_active=True)
        except Customer.DoesNotExist:
            return Response(None)

        email = get_request_data(request, "email")
        code = get_request_data(request, "code")
        if email and code:
            email_code = EmailCode.objects.filter(email=email)
            now = datetime.datetime.now()
            valid_second = EmailValidSecond.objects.all()[0].seconds
            if email_code and email_code[0].code == code and (now-email_code[0].register_date).seconds<=valid_second:
                # if not agent.email:
                #     checkin, created = Checkin.objects.get_or_create(user=request.user)
                #     points = Point.objects.get(type='2').points
                #     if created:
                #         checkin.continuous_days=0
                #         checkin.points = points
                #     else:
                #         checkin.points += points
                #     checkin.save()
                agent.email = email
                agent.save()
                return Response({"status":1,"message":u"认证成功!"})
            return Response({"status":0,"message":u"验证码错误,请重新输入或者重新获取!"})
        return Response({"status":0,"message":u"字段错误!"})


#检查是否最新版本
class VersionList(APIView):
    def get(self, request, format=None):
        version = Agent_Version.objects.all()
        serializer = AgentVersionSerializer(version, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #数据库中只有一组版本数据
        version_latest = Agent_Version.objects.all()[0]
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
        #客户经理所属公司信息
        business = Business.objects.filter(agent__user=request.user)
        business_serializer = BusinessSerializer(business, context={'request':request}, many=True)
        #首页公告
        announcements = Announcement.objects.filter(announce_business=business, is_active=True)
        announcements_serializer = AnnouncementSerializer(announcements, context={'request':request}, many=True)
        #热销产品
        products = Product.objects.filter(business=business, on_top=True, is_active=True)
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

#获取该客户经理名下某客户在该公司的所有购买
class PurchasesList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        customer_id = request.GET.get("customer_id",0)
        if customer_id:
            business = Business.objects.filter(agent__user=request.user)
            purchases = Purchase.objects.filter(customer=customer_id, product__business=business)
            serializer = PurchaseSerializer(purchases, many=True)
            return  Response(serializer.data)
        return Response(None)

#客户真实购买
class RealPurchaseViewSet(PurchaseViewSetMixin, viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Real_purchase.objects.all()
    serializer_class = RealPurchaseSerializer

    def get_queryset(self):
        customer_id = self.request.GET.get("customer_id",0)
        if customer_id:
            return Real_purchase.objects.filter(real_agent__user=self.request.user, customer=customer_id, is_active=True)#only get self
        return Real_purchase.objects.filter(real_agent__user=self.request.user, is_active=True)#only get self

    #删除时不直接删除而是把is_active置为False
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        # instance.delete()

#登录验证,只有agent可以登录
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        def login(agent, request):
            userLogin = authenticate(username=request.data["username"],password=request.data["password"])

            # serializer.is_valid(raise_exception=True)
            # user = serializer.validated_data['user']
            if userLogin:
                user = agent.user
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message":u'密码错误!'})


        # serializer = self.serializer_class(data=request.data)
        if "username" not in request.data:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message":u'请输入用户名!'})
        if "password" not in request.data:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message":u'请输入密码!'})

        agent = get_agent(request.data["username"])
        if agent and agent.user:
            if "device_id" in request.data:
                device_id = request.data["device_id"]
                if agent.device_id:
                    if agent.device_id==device_id:
                        return login(agent, request)
                    else:
                        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message":u'用户与手机不匹配，请与管理员联系解除手机绑定!'})
                else:
                    agent.device_id = device_id
                    agent.save()
                    return login(agent, request)
            else:
                return login(agent, request)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message":u'用户不存在!'})
        # agent = Agent.objects.filter(phoneNum=request.data["username"], is_active=True)


#当天签到次数
class CheckWorkCountView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        counts = CheckWork_history.objects.filter(check_history=request.user, type='1',
                                                  check_time__year=now.year,
                                                  check_time__month=now.month,
                                                  check_time__day=now.day).count()
        return Response({"counts": counts})


#考勤历史记录viewset
class CheckWorkHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = CheckWork_history.objects.all()
    serializer_class = CheckWorkHistorySerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return CheckWork_history.objects.filter(check_history=self.request.user).order_by('-check_time')#only get self

#考勤记录,在CheckWork中更新,在CheckWork_history中增加
class CheckWorkView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        now = datetime.datetime.now()
        agent = Agent.objects.get(user=user)
        abscissa = get_request_data(request, 'abscissa')
        ordinate = get_request_data(request, 'ordinate')
        address = get_request_data(request, 'address')
        area = get_request_data(request, 'area')
        type = get_request_data(request, 'type', '1')

        #添加到CheckWork_history
        checkhis = CheckWork_history(check_history=user, check_business_history=agent.business, abscissa=abscissa, ordinate=ordinate, check_time=now, address=address, area=area, type=type)
        checkhis.save()

        #更新CheckWork,若存在,更新,否则新增
        checkwork, created = CheckWork.objects.update_or_create(check_user=user,defaults={
            "check_business": agent.business,
            "abscissa": abscissa,
            "ordinate": ordinate,
            "check_time": now,
            "address": address,
            "area": area,
            "type": type
        })

        return Response({"status":1, "message":u'更新成功!'})


#考勤时间
class CheckWorkTimeViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Check_Time_Setting.objects.all()
    serializer_class = CheckWorkTimeSerializer

    def get_queryset(self):
        return Check_Time_Setting.objects.filter(business__agent__user=self.request.user)#only get self



#内部公告viewset
class InternalAnnouncementViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Internal_announcement.objects.all()
    serializer_class = InternalAnnouncementSerializer
    pagination_class = TenResultsSetPagination

    def get_queryset(self):
        return Internal_announcement.objects.filter(announcement_business__agent__user=self.request.user, is_active=True)#only get self

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        #如果未读添加已读状态
        if not Read_message.objects.filter(read_user=self.request.user, model_name='internal_announcement', record_id=instance.id):
            read_message = Read_message(read_business=instance.announcement_business, read_user=self.request.user, model_name='internal_announcement', record_id=instance.id, read_time=datetime.datetime.now())
            read_message.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


#工作汇报
class DailyWorkViewSet(ApplicationViewSetMixin, viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Daily_work.objects.all()
    serializer_class = DailyWorkSerializer
    pagination_class = TenResultsSetPagination

    def get_queryset(self):
        return Daily_work.objects.filter(user=self.request.user, is_active=True)#only get self

    #新增申请的同时要新增审批
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        daily_work = Daily_work.objects.get(id=serializer.data["id"])
        create_examine(daily_work)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #不能修改申请
    def update(self, request, *args, **kwargs):
        return Response(None)

    #删除时同时删除审批
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        delete_examine(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

#该员工所有未读审批数量
class ExamineUnread(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        unread = All_Examine.objects.filter(examine_user=request.user, read_status='1', is_active=True).count()
        return Response({"examines_unread": unread})

#该员工所有审批
class ExamineViewset(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = All_Examine.objects.all()
    serializer_class = ExamineSerializer
    pagination_class = TenResultsSetPagination

    def get_queryset(self):
        return All_Examine.objects.filter(examine_user=self.request.user, is_active=True).order_by('read_status', '-examine_status', '-id')#only get self

    #添加已读
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.read_status = '2'
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    #只有审批状态为待审核时才可以修改,已经审核之后不能修改
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if instance.examine_status=="3":
            self.perform_update(serializer)
            return Response(serializer.data)
        # self.perform_update(serializer)
        return Response({"message":u"该申请已经审核,不能再修改!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #修改时审批人和机构不能修改
    def perform_update(self, serializer):
        try:
            serializer.save(examine_user=self.request.user, examine_business=Business.objects.get(agent__user=self.request.user))
        except Exception, err:
            logger.error(err)

    #不能直接新增审批
    def create(self, request, *args, **kwargs):
        return Response(None)

    #不能直接删除审批
    def perform_destroy(self, instance):
        return Response(None)

#员工将审批提交给其他员工
class ExamineTranspond(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if "examine_id" in request.data and "user_id_list" in request.data:
            examine_id = request.data['examine_id']
            user_id_list = request.data['user_id_list']
            try:
                examine = All_Examine.objects.get(id=examine_id)
            except:
                return Response({"status":0, "message":u'不存在该审批!'})
            application = examine.examine
            users = application.examine_user.all()
            user_list = []
            #先判断该用户是否存在,或者该用户是否已经在审批列表中,再统一进行数据的添加,避免数据添加了一部分出错
            for user_id in user_id_list:
                try:
                    user = User.objects.get(id=user_id)
                    user_list.append(user)
                except:
                    return Response({"status":0, "message":u'不存在该用户!'})
                if user in users:
                    return Response({"status":0, "message":u'该用户已在该审批中!'})
            for user in user_list:
                new_examine = All_Examine(examine_user=user, examine_business=application.business, examine=application)
                new_examine.save()
                application.examine_user.add(user)
                application.save()
                return Response({"status":1, "message":u'提交成功!'})
        else:
            return Response({"status":0, "message":u'字段不完整!'})

#该员工所有申请列表
class ApplicationViewset(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = All_Examine.objects.all()
    serializer_class = ApplicationSerializer
    pagination_class = TenResultsSetPagination

    def get_queryset(self):
        cost = Cost_application.objects.filter(user=self.request.user, is_active=True)
        leave = Leave_management.objects.filter(user=self.request.user, is_active=True)
        travel = Travel_apply.objects.filter(user=self.request.user, is_active=True)
        return sorted(
            chain(cost, leave, travel),
            key=attrgetter('time'),
            reverse=True
        )

#费用申请
class CostApplicationViewSet(ApplicationViewSetMixin, viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Cost_application.objects.all()
    serializer_class = CostApplicationSerializer
    pagination_class = TenResultsSetPagination

    def get_queryset(self):
        return Cost_application.objects.filter(user=self.request.user, is_active=True).order_by('-id')#only get self

    #新增申请的同时要新增审批
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        cost_application = Cost_application.objects.get(id=serializer.data["id"])
        create_examine(cost_application)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #不能修改申请
    def update(self, request, *args, **kwargs):
        return Response(None)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        delete_examine(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

# #费用审批
# class CostExamineViewSet(viewsets.ModelViewSet):
#     authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
#     permission_classes = (IsAuthenticated,)
#
#     queryset = Cost_examine.objects.all()
#     serializer_class = CostExamineSerializer
#     pagination_class = StandardResultsSetPagination
#
#     def get_queryset(self):
#         return Cost_examine.objects.filter(examine_user=self.request.user, is_active=True)#only get self
#
#     #不能直接新增审批
#     def create(self, request, *args, **kwargs):
#         return Response(None)
#
#     #不能直接删除审批
#     def perform_destroy(self, instance):
#         return Response(None)

#请假申请
class LeaveManagementViewSet(ApplicationViewSetMixin, viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Leave_management.objects.all()
    serializer_class = LeaveManagementSerializer
    pagination_class = TenResultsSetPagination

    def get_queryset(self):
        return Leave_management.objects.filter(user=self.request.user, is_active=True).order_by('-id')#only get self

    #新增申请的同时要新增审批
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        leave_application = Leave_management.objects.get(id=serializer.data["id"])
        create_examine(leave_application)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #不能修改申请
    def update(self, request, *args, **kwargs):
        return Response(None)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        delete_examine(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

# #请假审批
# class LeaveExamineViewSet(viewsets.ModelViewSet):
#     authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
#     permission_classes = (IsAuthenticated,)
#
#     queryset = Leave_examine.objects.all()
#     serializer_class = LeaveExamineSerializer
#     pagination_class = StandardResultsSetPagination
#
#     def get_queryset(self):
#         return Leave_examine.objects.filter(examine_user=self.request.user, is_active=True)#only get self
#
#     #不能直接新增审批
#     def create(self, request, *args, **kwargs):
#         return Response(None)
#
#     #不能直接删除审批
#     def perform_destroy(self, instance):
#         return Response(None)

#出差申请
class TravelApplyViewSet(ApplicationViewSetMixin, viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Travel_apply.objects.all()
    serializer_class = TravelApplySerializer
    pagination_class = TenResultsSetPagination

    def get_queryset(self):
        return Travel_apply.objects.filter(user=self.request.user, is_active=True).order_by('-id')#only get self

    #新增申请的同时要新增审批
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        travel_application = Travel_apply.objects.get(id=serializer.data["id"])
        create_examine(travel_application)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #不能修改申请
    def update(self, request, *args, **kwargs):
        return Response(None)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        delete_examine(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

# #出差审批
# class TravelExamineViewSet(viewsets.ModelViewSet):
#     authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
#     permission_classes = (IsAuthenticated,)
#
#     queryset = Travel_examine.objects.all()
#     serializer_class = TravelExamineSerializer
#     pagination_class = StandardResultsSetPagination
#
#     def get_queryset(self):
#         return Travel_examine.objects.filter(examine_user=self.request.user, is_active=True)#only get self
#
#     #不能直接新增审批
#     def create(self, request, *args, **kwargs):
#         return Response(None)
#
#     #不能直接删除审批
#     def perform_destroy(self, instance):
#         return Response(None)

# #该员工所有审批列表
# class ExamineList(generics.ListAPIView):
#     authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
#     permission_classes = (IsAuthenticated,)
#
#     queryset = Cost_examine.objects.all()
#     serializer_class = ExamineSerializer
#     pagination_class = StandardResultsSetPagination
#
#     def get_queryset(self):
#         cost = Cost_examine.objects.filter(cost_examine__cost_user=self.request.user)
#         leave = Leave_examine.objects.filter(leave_examine__leave_user=self.request.user)
#         travel = Travel_examine.objects.filter(travel_examine__travel_user=self.request.user)
#         return sorted(chain(cost, leave, travel))

#意向客户
class CustomerPendingViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Customer.objects.filter(agents__user=self.request.user, customer_type='2', is_active=True).order_by('-id')#only get self

    #添加时客户经理绑定为request.user对应的客户经理
    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            try:
                serializer.save(customer_type='2', agents=[Agent.objects.get(user=self.request.user)])
            except:
                serializer.save()

    #删除时不直接删除而是把is_active置为False
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        # instance.delete()

#客户名片更改
class CallingCardUpdate(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)#should be customer authenticate, isOwner only

    def post(self, request, format=None):
        customer_id = self.request.GET.get("customer_id",0)
        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
                customer.calling_card = request.data["calling_card"]#名片更改
                customer.save()
                image_path = MEDIA_ROOT+str(customer.calling_card)
                set_picture_pixel(image_path)
                return Response({"status":1, "message":u"修改成功!"})
            except Customer.DoesNotExist:
                return Response({"status":0, "message":u"修改失败!"})
        return Response({"status":0, "message":u"修改失败!"})

#客户转移
class CustomerDeliver(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        customer = Customer.objects.get(id=data["customer_id"], customer_type='1')
        from_agent = Agent.objects.get(user=request.user)
        to_agent = Agent.objects.get(id=data["agent_id"])

        if from_agent.id==to_agent.id or from_agent.business!=to_agent.business:
            return Response({"status":0, "message":u"转移失败!"})

        customer.agents.remove(from_agent)
        customer.agents.add(to_agent)
        customer.save()
        if customer.email:
            content=u"""
            尊敬的客户:<br/>
               您好:<br/>
               您的牛基队账户%s机构的客户经理已从%s更改为%s,请登录牛基队客户端进行查看,若您存在疑问,请联系您的客户经理.感谢您的使用!<br/>
            """ % (from_agent.business.name, from_agent.name, to_agent.name)
            send_email(agent=from_agent, subject=u"客户经理更换", content=content, receivers=[customer.email])
        return Response({"status":1, "message":u"转移成功!"})

#客户经理和客户通话记录
class CellRecordsCustomerViewSet(AgentViewSetMixin, viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Cell_Records_Customer.objects.all()
    serializer_class = CellRecordsCustomerSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Cell_Records_Customer.objects.filter(agent__user=self.request.user, customer__customer_type='1')#only get self

#客户经理和意向客户通话记录
class CellRecordsPCustomerViewSet(AgentViewSetMixin, viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Cell_Records_PCustomer.objects.all()
    serializer_class = CellRecordsPCustomerSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Cell_Records_PCustomer.objects.filter(agent__user=self.request.user, customer__customer_type='2')#only get self


#每日待办
class DailyToDoViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Daily_to_do.objects.all()
    serializer_class = DailyToDoSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Daily_to_do.objects.filter(todo_user=self.request.user)#only get self

    def perform_create(self, serializer):
        serializer.save(todo_user=self.request.user)
        # return super(DailyToDoViewSet, self).perform_create(serializer)

#反馈信息接收,发送邮件
class FeedbackDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        try:
            agent = Agent.objects.get(user=request.user)
        except Agent.DoesNotExist:
            return Response(None)
        id = agent.id
        name = agent.name
        number = agent.phoneNum
        subject = request.data["subject"]
        content = request.data["content"]
        #sender为在收件人邮件中显示的发件人
        sender = 'niujidui@niujidui.com'
        #reveivers为收件人的列表，可以发送给多个人
        receivers = ['niujidui@qq.com']

        #message为发送邮件的主题和正文
        mail_msg = u"""
        客户经理编号:%s, 客户经理姓名:%s, 客户经理手机号:%s.<br/>
        反馈内容:%s""" % (id, name, number, content)
        message = MIMEText(mail_msg, 'html', 'utf-8')
        message['subject'] = str(subject)
        message['from'] = sender
        message['to'] = ", ".join(receivers)

        #发件人服务器
        try:
            smtp = smtplib.SMTP(MAIL_HOST)
            smtp.sendmail(sender, receivers, message.as_string())
            return Response(u"反馈已发送,谢谢您的支持!")
        except:
            return Response(u"发送失败,请重新发送!")


#跳转到相应链接进行app下载
def APPDownload(request):
    if request.method == "GET":
        return render_to_response("agent_api/app_download.html")
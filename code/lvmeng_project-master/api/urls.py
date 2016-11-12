#! /usr/bin/env python
#coding:utf-8
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from rest_framework import routers
# import pinax.messages.views

from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'business', views.BusinessViewSet)
router.register(r'agents', views.AgentViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'purchases', views.PurchaseViewSet)
router.register(r'headlines', views.HeadlineViewSet)
router.register(r'headlines_detail', views.HeadlineDetailViewSet)
router.register(r'collections', views.CollectionViewSet)
router.register(r'attentions', views.AttentionViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^api-token-auth/', views.ObtainAuthToken.as_view()),#登录

    # url(r'^customer_self/$', views.CustomerSelf.as_view()),
    # url(r'^pricedata/(?P<epicname>.+)/$', views.pricedata.as_view()),

    url(r'^customer_update/$', views.CustomerupdateDetail.as_view()),#用户信息修改
    url(r'^idcard_update/$', views.IdCardUpdate.as_view()),#用户身份证号码认证
    url(r'^email_update/$', views.EamilUpdate.as_view()),#用户邮箱认证
    url(r'^email_verify/$', views.EamilVerify.as_view()),#用户邮箱验证码发送
    url(r'^phone_update/$', views.PhoneUpdate.as_view()),#手机号码修改
    url(r'^callingcard_update/$', views.CallingCardUpdate.as_view()),#用户名片修改
    url(r'^avatar_update/$', views.CustomerAvatarUpdate.as_view()),#用户头像修改
    url(r'^version/$', views.VersionList.as_view()),#版本信息
    url(r'^homepage/$', views.HomePageList.as_view()),#主页信息展示
    url(r'^allproducts/$', views.AllProductsList.as_view()),#该用户对应机构的所有产品
    # url(r'^headlines/$', views.HeadlineList.as_view()),#金融头条
    url(r'^checkins/$', views.CheckinList.as_view()),#签到
    url(r'^share_points/$', views.SharePoints.as_view()),#分享积分api
    url(r'^password_change/$', views.PasswordchangeList.as_view()),#修改密码
    # url(r'^purchases/$', views.PurchaseList.as_view()),#用户的购买
    url(r'^feedback/$', views.FeedbackDetail.as_view()),#用户反馈
    url(r'^verification/$', views.Verification.as_view()),#验证码
    url(r'^register/$', views.Register.as_view()),#用户注册
    url(r'^forget_password/$', views.ForgetPassword.as_view()),#忘记密码
    url(r'^invitation_detail/$', views.InvitationDetail.as_view()),#根据邀请码获取机构和客户经理详情
    url(r'^add_agent/$', views.AddAgent.as_view()),#添加机构
    url(r'^delete_agent/$', views.DeleteAgent.as_view()),#删除机构
    # url(r'^headline/$', views.HeadlineListView.as_view()),

    url(r'^url_agent/$', views.UrlAgent),#网页注册客户经理信息确认
    url(r'^url_register/$', views.UrlRegister),#网页注册
    url(r'^url_add_agent/$', views.UrlAddAgent),#网页注册
    url(r'^app_download/$', views.APPDownload),#app跳转下载

    # url(r"^messages/thread/(?P<pk>\d+)/$", pinax.messages.views.ThreadView.as_view(), name="messages_thread_detail"),
    # url(r"^messages/", include("pinax.messages.urls", namespace="pinax_messages")),
]
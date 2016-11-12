#! /usr/bin/env python
#coding:utf-8
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from rest_framework import routers

from . import views
import api.views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'address_customers', views.AddressCustomerViewSet)
router.register(r'agents', views.AgentViewSet)
router.register(r'internal_announcement', views.InternalAnnouncementViewSet)
router.register(r'daily_work', views.DailyWorkViewSet)
router.register(r'cost_application', views.CostApplicationViewSet)
# router.register(r'cost_examine', views.CostExamineViewSet)
router.register(r'leave_management', views.LeaveManagementViewSet)
# router.register(r'leave_examine', views.LeaveExamineViewSet)
router.register(r'travel_apply', views.TravelApplyViewSet)
# router.register(r'travel_examine', views.TravelExamineViewSet)
router.register(r'customer_pendings', views.CustomerPendingViewSet)
router.register(r'cell_records_customer', views.CellRecordsCustomerViewSet)
router.register(r'cell_records_pcustomer', views.CellRecordsPCustomerViewSet)
router.register(r'daily_to_do', views.DailyToDoViewSet)
router.register(r'real_purchases', views.RealPurchaseViewSet)
router.register(r'checkwork_history', views.CheckWorkHistoryViewSet)
router.register(r'checkwork_time', views.CheckWorkTimeViewSet)
router.register(r'examines', views.ExamineViewset)
router.register(r'applications', views.ApplicationViewset)
router.register(r'file_upload', views.TemporaryFileViewSet)

router.register(r'headlines', api.views.HeadlineViewSet)
router.register(r'headlines_detail', api.views.HeadlineDetailViewSet)
router.register(r'comments', api.views.CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^api-token-auth/', views.ObtainAuthToken.as_view()),#登录

    url(r'^version/$', views.VersionList.as_view()),#版本信息
    url(r'^agent_update/$', views.AgentupdateDetail.as_view()),#基本信息修改
    url(r'^callingcard_update/$', views.CallingCardUpdate.as_view()),#意向客户名片修改?customer_id
    url(r'^agent_avatar_update/$', views.AgentAvatarUpdate.as_view()),#头像修改
    url(r'^email_update/$', views.EamilUpdate.as_view()),#邮箱更改
    url(r'^email_verify/$', api.views.EamilVerify.as_view()),#邮箱验证码发送
    url(r'^checkins/$', api.views.CheckinList.as_view()),#签到
    url(r'^share_points/$', api.views.SharePoints.as_view()),#分享积分api
    url(r'^homepage/$', views.HomePageList.as_view()),
    url(r'^password_change/$', views.PasswordchangeList.as_view()),
    url(r'^purchases/$', views.PurchasesList.as_view()),#?customer_id
    url(r'^checkwork/$', views.CheckWorkView.as_view()),#考勤
    url(r'^checkwork_counts/$', views.CheckWorkCountView.as_view()),#考勤次数
    url(r'^mail_to_pcustomers/$', views.MailToAllPengdingCustomers.as_view()),#给意向客户群发邮件
    url(r'^mail_to_customers/$', views.MailToCustomers.as_view()),#给已有客户发送邮件
    url(r'^email_send/$', views.EmailSend.as_view()),#给特定邮箱发邮件
    url(r'^customer_deliver/$', views.CustomerDeliver.as_view()),#客户转移
    url(r'^feedback/$', views.FeedbackDetail.as_view()),#客户经理意见反馈
    url(r'^unread/$', views.ExamineUnread.as_view()),#未读
    url(r'^examine_transpond/$', views.ExamineTranspond.as_view()),#员工将审批提交给其他员工

    # url(r'^examines/$', views.ExamineList.as_view()),#所有的审批列表

    url(r'^app_download/$', views.APPDownload),#客户经理版app跳转下载
    # url(r'^test_qrcode/$', views.qrcode_test),#agent二维码测试
    # url(r'^email/$', views.django_email_test),#django email测试

]
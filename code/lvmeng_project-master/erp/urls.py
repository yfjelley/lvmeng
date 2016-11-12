#coding:utf-8
from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views,views2
from erp import tests1 as tests
urlpatterns = [
    url(r'^product_process/$', views.product_process),#产品操作
    url(r'^position_list/$',views.position_list),#职位列表
    url(r'^position_add_modify/$',views.position_add_modify),#新增/修改职位
    url(r'^business_process/$',views.business_process),#新增客户机构

    url(r'^business_list/$',views.business_list),#客户机构列表
    url(r'^business_password_change/(?P<user_id>\d+)/$',views.business_password_change),#强制修改密码
    url(r'^agent_process/$',views.agent_process),#新增员工
    url(r'^agent_list/$',views.agent_list),#员工列表
    url(r'^product_list/$',views.product_list),#产品列表
    url(r'^check/$',views.check),#查看

    url(r'agent_customer_allot/$',views2.agent_customer_allot),#删除理财师进行客户分配

    # -------------------------下面将要去除（测试用）------------------------------------------
    url(r'^customer_list/$',views.customer_list),#客户列表
    url(r'^customer_add/$',views.customer_add),#新增客户
    # ---------------------------------------------------------------

    # ---------------------------just for admin--------------------------------------
    url(r'^admin_agent_list/$',views2.agent_role),#按员工角色查看
    url(r'^agent_customers/$',views2.agent_customers),#根据员工查看下面的客户
    url(r'^admin_product_list/$',views2.admin_purchase_list),#查看客户的所有购买
    url(r'^purchases_list/$',views2.purchases_list),#查看客户的所有购买
    url(r'^admin_customers/$',views2.admin_customers),#查看所有的客户
    url(r'^redister_customers/$',views2.redister_customers),#查看所有的注册客户
    url(r'^admin_business_product/$',views.admin_business_product),#查看机构所有的产品
    url(r'^business_redister_list/$',views.business_redister_list),#律锰查看注册申请列表
    url(r'^business_redister_examine/$',views.business_redister_examine),#律锰审核注册申请
    # ---------------------------just for admin--------------------------------------

    url(r'^picture_logos/$',views2.business_logos),#添加机构图片信息
    url(r'^business_announcement_list/$',views2.business_announcement_list),#查看机构公告列表

    url(r'^agent_add_product/$',views2.agent_add_product),#理财师添加客户所购买的产品信息/添加的列表
    url(r'^agent_product_list/$',views2.agent_product_list),#理财师添加客户所购买的产品信息的列表

    url(r'^income_inquiry/$',views2.income_inquiry),#财务查看购买的产品信息的列表

    url(r'^customer_business_search/$',views2.customer_business_search),#用户选择机构显示相对应的信息
    url(r'^show_product_by_type/$',views2.show_product_by_type),

    url(r'^financial_headlines/$',views2.financial_headlines),#金融头条列表
    url(r'^headline_add_modify/$',views2.headline_add_modify),#新增/修改金融头条

    url(r'^modify_business_base_info/$',views2.modify_business_base_info),#修改机构基本信息
    url(r'^show_business_base_info/$',views2.show_business_base_info),#机构基本信息

    url(r'^username_change/$',views2.username_change),#修改用户名(账号)

    url(r'^release_base_64/$',views2.release_base_64),


    url(r'^valid_phone/$',tests.valid_phone),#验证手机号是否存在
    url(r'^valid_email/$',tests.valid_email),#验证邮箱是否存在
    url(r'^check_new_message/$',tests.check_new_message),#检测是否有新消息
    url(r'^get_position_permission/$',tests.get_position_permission),#获取对应职位的权限

    #机构轮播图
    url(r'^business_carousel_list_delete/$',views.business_carousel_list_delete),
    url(r'^business_carousel_add/$',views.business_carousel_add),

    url(r'^no_permission/$',views.no_permission),

    url(r'^mail_list/$',views.mail_list),#通讯录

    #机构注册
    url(r'^business_redister/$',views.business_redister.as_view()),#注册第一步
    url(r'^business_redister_detail/$',views.business_redister_detail),#注册第二步
    url(r'^business_redister_save/$',views.business_redister_save),#保存注册信息
    # url(r'^register_success/$',views.register_success),#注册成功

    #客户注册
    url(r'^person_redister/$',views.person_redister),#客户注册
    url(r'^valid_code/$',tests.valid_code),#验证码验证

    url(r'^online_chat/$',views.online_chat),#在线聊天
    url(r'^save_user_message/$',views.save_user_message),#保存聊天信息
    url(r'^chat_user_message/$',views.chat_user_message),#获取聊天信息
    url(r'^chat_logo_message_remind/$',views.chat_logo_message_remind),#获取所有未读信息
    url(r'^message_control/$',views.message_control),#将每个人的信息控制在100条


    url(r'^rejection_reason/$',views.rejection_reason),#机构注册申请驳回原因














    # url(r'', views.employee_list),#所有的员工
]

#coding:utf-8
#employee_distribution

from django.conf.urls import url
from . import views,views2

urlpatterns = [
    url(r'^employee_distribution/$', views.employee_distribution),#
    url(r'^employee_position/$', views.employee_position),#
    url(r'^ajax_name/$', views.ajax_name),#根据ID获取姓名
    url(r'^employee_history_position/$', views.employee_history_position),#根据ID获取姓名
    url(r'^employee_history_position_days/$', views.employee_history_position_days),#根据ID获取姓名

    url(r'^announcement_employee/$', views.announcement_employee),#通知公告(面向员工)
    url(r'^announcement_add_modify/$', views.announcement_add_modify),#通知公告新增/修改/

    url(r'^daily_work/$', views.daily_work),#工作汇报列表/删除
    url(r'^daily_work_add_modify/$', views.daily_work_add_modify),#工作汇报新增/

    url(r'^cost_application/$', views.cost_application),#费用列表和删除
    url(r'^cost_add_modify/$', views.cost_add_modify),#费用新增
    url(r'^edit_examine/$', views.edit_examine),#编写费用审核
    url(r'^cost_examine/$', views2.cost_examine),#查看费用审核结果
    url(r'^daily_work_examine/$', views2.daily_work_examine),#查看工作汇报审核结果
    url(r'^examine_list/$', views2.examine_list),#查看自己的所有审核列表

    url(r'^leave_management/$', views.leave_management),#请假列表和删除
    url(r'^leave_add_modify/$', views.leave_add_modify),#请假新增
    # url(r'^edit_leave_examine/$', views.edit_leave_examine),#编写请假审核
    url(r'^leave_examine/$', views2.leave_examine),#查看请假审核结果
    # url(r'^leave_examine_list/$', views2.leave_examine_list),#查看自己的请假审核列表

    url(r'^travel_apply/$', views.travel_apply),#出差列表和删除
    url(r'^travel_add_modify/$', views.travel_add_modify),#出差新增
    # url(r'^edit_travel_examine/$', views.edit_travel_examine),#编写出差审核
    url(r'^travel_examine/$', views2.travel_examine),#查看出差审核结果
    # url(r'^travel_examine_list/$', views2.travel_examine_list),#查看自己的出差审核列表

    url(r'^daily_todo_list/$', views2.daily_todo_list),#每日待办列表/删除
    url(r'^daily_todo_add_modify/$', views2.daily_todo_add_modify),#每日待办事件新增和修改

    url(r'^check_table/$', views2.check_table),#
    url(r'^check_time_setting/$', views2.check_time_setting),#

    # url(r'^read_message/$', views.read_message),#添加已读记录







]

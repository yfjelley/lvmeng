#coding:utf-8
from erp.models import Announcement,Real_purchase,Position,Online_chat
from oa.models import Internal_announcement
from django.db.models import Q

def check_product(request,id,business):
    ids = []
    if request.user.is_superuser:
        return True
    products = business.product_set.all()
    for pro in products:
        ids.append(int(pro.id))
        if int(id) in ids:
            return True

def check_agent(request,business,agent):
    if request.user.is_superuser:
        return True
    ageId = []
    agent_id = agent.id
    agents = business.agent_set.filter(is_active=1)
    for age in agents:
        ageId.append(age.id)
    if agent_id in ageId:
        return True

def check_agent_modify(request,business,agent):
    if request.user.is_superuser:
        return False
    ageId = []
    agent_id = agent.id
    agents = business.agent_set.filter(is_active=1)
    for age in agents:
        ageId.append(age.id)
    if agent_id in ageId:
        return True

def check_customer(request,customer,business,permissions):
    if request.user.is_superuser:
        return True

    ids = []
    agents = customer.agents.filter(is_active=1,business=business)
    try:
        user_agent = request.user.agent

        if user_agent in agents :
            return True

        if 'auth.customer_show' in permissions and agents:
            return True
    except:
        pass

    try:
        user_business = request.user.business
        for age in agents:
            ids.append(age.business)
        if business in ids:
            return True
    except:
        pass

def check_announcement_out(request,announce,business):#面向客户(对外)
    announcements = Announcement.objects.filter(announce_business=business,is_active=1)
    if request.user.is_superuser or announce in announcements:
        return True

def check_internal_announcement(request,announce,business):#面向员工(对内)
    announcements = Internal_announcement.objects.filter(announcement_business=business,is_active=1)
    if request.user.is_superuser or announce in announcements:
        return True

def check_position(request,position,business):#面向员工(对内)
    positions = Position.objects.filter(business=business)
    if position in positions:
        return True

def check_daily_work(request,dailyWork,business):
    if request.user.is_superuser:
        return True
    try:
        employee = request.user.agent
        user = request.user
        daily_works = user.daily_work_set.filter(is_active=1)
        if dailyWork in daily_works:
            return True
    except:
        daily_works = business.daily_work_set.filter(is_active=1)
        if dailyWork in daily_works:
            return True
    
def check_cost_application(request,cost,business):
    if request.user.is_superuser:
        return True
    try:
        employee = request.user.agent
        user = request.user
        costs = user.cost_application_set.filter(is_active=1)
        if cost in costs:
            return True
    except:
        costs = business.cost_application_set.filter(is_active=1)
        if cost in costs:
            return True

def check_leave_application(request,leave,business):
    if request.user.is_superuser:
        return True
    try:
        employee = request.user.agent
        user = request.user
        leaves = user.leave_management_set.filter(is_active=1)
        if leave in leaves:
            return True
    except:
        leaves = business.leave_management_set.filter(is_active=1)
        if leave in leaves:
            return True

def check_travel_apply(request,travel,business):
    if request.user.is_superuser:
        return True
    try:
        employee = request.user.agent
        user = request.user
        travels = user.travel_apply_set.filter(is_active=1)
        if travel in travels:
            return True
    except:
        travels = business.travel_apply_set.filter(is_active=1)
        if travel in travels:
            return True

def delete_customer(request,obj):#客户操作限制
    try:
        if obj.customer_type == '2' and request.user.agent in obj.agents.filter(is_active=1):
            return True
    except:
        return False
    return False

def real_purchase_precess(request,obj):#真实购买修改和删除
    try:
        if request.user.agent in obj.agents.filter(is_active=1):
            return True
    except:
        return False
    return False

def real_purchase_list(request,business):#购买列表
    if request.user.is_superuser:
        return Real_purchase.objects.filter(customer__is_active=1)
    try:
        agent = request.user.agent
        return Real_purchase.objects.filter(business=business,real_agent=request.user.agent,customer__is_active=1)
    except:
        return Real_purchase.objects.filter(business=business,customer__is_active=1)

def check_real_purchase(request,obj,business):#真实购买查看过滤
    if request.user.is_superuser:
        return True
    try:
        agent = request.user.agent
        if obj in agent.real_purchase_set.filter(is_active=1):
            return True
    except:
        if obj in business.real_purchase_set.filter(is_active=1):
            return True

def check_employee(request,obj,business):#过滤员工是否属于该机构并删除

    if business and obj in business.agent_set.filter(is_active=1):
        return True

def delete_announcement_inner(request,obj,business):#删除内部公告过滤

    if business and obj in business.internal_announcement_set.filter(is_active=1):

        return True

#删除产品过滤
def product_delete(request,obj,business):
    if not request.user.is_superuser and obj in business.product_set.filter(is_active=1):
        return True

#删除每日待办过滤
def delete_daily(request,obj):
    if obj in request.user.daily_to_do_set.filter(is_active=1):
        return True

class Apply_Process(object):#所有申请操作

    def daily_work_delete(self,request,obj):#工作日报删除
        try:
            agent = request.user.agent
            if obj in request.user.daily_work_set.all():
                return True
        except:
            return False

    def check_daily_work_examine(self,request,obj,business):#工作日报查看审核情况
        if request.user.is_superuser:
            return True
        try:
            agent = request.user.agent
            if obj in request.user.daily_work_set.all():
                return True
        except:
            if obj in business.daily_work_set.all():
                return True

    def cost_application_delete(self,request,obj):#费用申请删除
            try:
                agent = request.user.agent
                if obj in request.user.cost_application_set.all():
                    return True
            except:
                return False

    def check_cost_application_examine(self,request,obj,business):#费用申请查看审核情况
        if request.user.is_superuser:
            return True
        try:
            agent = request.user.agent
            if obj in request.user.cost_application_set.all():
                return True
        except:
            if obj in business.cost_application_set.all():
                return True

    def leave_management_delete(self,request,obj):#请假申请删除
        try:
            agent = request.user.agent
            if obj in request.user.leave_management_set.all():
                return True
        except:
            return False

    def check_leave_management_examine(self,request,obj,business):#请假申请查看审核情况
        if request.user.is_superuser:
            return True
        try:
            agent = request.user.agent
            if obj in request.user.leave_management_set.all():
                return True
        except:
            if obj in business.leave_management_set.all():
                return True

    def travel_apply_delete(self,request,obj):#出差申请删除
            try:
                agent = request.user.agent
                if obj in request.user.travel_apply_set.all():
                    return True
            except:
                return False

    def travel_apply_management_examine(self,request,obj,business):#出差申请查看审核情况
        if request.user.is_superuser:
            return True
        try:
            agent = request.user.agent
            if obj in request.user.travel_apply_set.all():
                return True
        except:
            if obj in business.travel_apply_set.all():
                return True

#获取聊天消息,对应的每一个员工，和消息总和
def get_user_agents(request,business):
    if request.user.is_superuser:
        return None,None

    total_unread = 0
    user_agents = business.agent_set.filter(~Q(user=request.user),is_active=1)
    for user in user_agents:
        unread = 0
        unread = Online_chat.objects.filter(business=business,recipient=request.user,sender=user.user,read=False).count()
        if unread:
            user.unread = unread
        total_unread += unread
    return user_agents,total_unread

import logging
from erp.diff_finder import NoChangeDiffFinder
logger = logging.getLogger('data_change')
#记录所有的操作记录
def load_process_message(request,old,new,action,id,business,diffs_str=True):
    if diffs_str:
        diff_find = NoChangeDiffFinder()
        diff_find.diff(old, new)
        log_msg = 'user_id=%s user_name=%s action=%s id=%s business=%s %s' % (
            request.user.id,
            request.user,
            action,
            id,
            business,
            diff_find.format_diffs_str
            )
    else:
        log_msg = 'user_id=%s user_name=%s action=%s id=%s business=%s' % (
            request.user.id,
            request.user,
            action,
            id,
            business,
            )
    logger.info(log_msg+"\n")










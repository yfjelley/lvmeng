#coding:utf-8
# from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
# from django.core.files import File
from django.shortcuts import render_to_response,redirect
from django.http import JsonResponse
from django.contrib import messages
import time
from models import *
from forms import *
from erp.utils import *
from django.core import serializers
from erp.views2 import get_permissions,get_all_required
from oa.views2 import get_unread_examine
from oa.views2 import get_emp_self,all_examine
from oa.views2 import paginatorPage
from django.forms.models import model_to_dict
from erp.utils import load_process_message,get_user_agents
# Create your views here.
apply = Apply_Process()
dict_map = {
    u"费用申请":"cost_application",
    u"出差申请":"travel_apply",
    u"请假申请":"leave_management",
    u"工作汇报":"daily_work",
}
dict_map2 = {
    "cost_application":u"费用申请",
    "travel_apply":u"出差申请",
    "leave_management":u"请假申请",
    "daily_work":u"工作汇报",
}
""" ************************************************考勤管理***************************************** """
''' 所有员工的分布图 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def employee_distribution(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    checks = get_self_checks(request)

    json_data = serializers.serialize("json",checks)

    message = u"员工分布"
    return render_to_response("oa/employee_distribution.html",locals(),context_instance=RequestContext(request))

''' 查询员工位置 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def employee_position(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    abscissa = 0
    ordinate = 0
    # check_name = get_self_checks(request)
    if request.user.is_superuser:
        checks = Agent.objects.filter(is_active=1)
    else:
        checks = Agent.objects.filter(business=business,is_active=1)
    if request.method == "POST":
        # checks = get_self_checks(request)
        # ch_name = checks.name
        id = request.POST.get("emp_name","")
        if not id:
            return redirect("/oa/employee_position")
        # user = User.objects.get(first_name=name)
        ck_user = Agent.objects.get(pk=id)
        try:
            check_work = CheckWork.objects.get(check_user=ck_user.user)
            abscissa = check_work.abscissa #员工横坐标
            ordinate = check_work.ordinate #员工纵坐标
            check_time = check_work.check_time
            business = check_work.check_business
            user = check_work.check_user
        except:
            pass
    message = u"员工位置查询"
    return render_to_response("oa/employee_position.html",locals(),context_instance=RequestContext(request))

''' 员工历史轨迹 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def employee_history_position(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    checks = None
    json_data = None
    # check_name = get_self_checks(request)
    if request.user.is_superuser:
        agents = Agent.objects.filter(is_active=1)
    else:
        agents = Agent.objects.filter(business=business,is_active=1)

    if request.method == "POST":
        checks,agent,dataTime,dataEnd = get_history_checks(request)
        json_data = serializers.serialize("json",checks)
    message = u"员工历史轨迹回放"
    return render_to_response("oa/employee_distribution_history.html",locals(),context_instance=RequestContext(request))

''' 员工历史轨迹(按天数显示)  '''

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def employee_history_position_days(request):
    permissions = get_permissions(request)
    count = get_unread_examine(request)
    # check_name = get_self_checks(request)
    business = get_business(request)
    agents = Agent.objects.filter(business=business,is_active=1)
    lv_unread = Redister_Business.objects.filter(status=3).count()

    name = request.GET.get("name","")
    if not name:
        return redirect("/oa/employee_history_position/")
    days = request.GET.get("days","")
    current = datetime.datetime.now().strftime("%Y-%m-%d")
    param = time.strptime(current, '%Y-%m-%d')
    param = datetime.date(param.tm_year,param.tm_mon,param.tm_mday)
    start = param + datetime.timedelta(days=int(days))
    end = param + datetime.timedelta(days=1)

    checks,agent = get_history_checks_days(request,name,start,end)
    json_data = serializers.serialize("json",checks)
    message = u"员工历史轨迹回放"
    return render_to_response("oa/employee_distribution_history.html",locals(),context_instance=RequestContext(request))

""" *********************************************协同办公**************************************************** """
'''通知公告'''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def announcement_employee(request):#通知公告列表/删除
    permissions = get_permissions(request)
    count = get_unread_examine(request)
    business = get_business(request)#获取机构
    user_agents,total_unread = get_user_agents(request,business)
    read = []
    internal_id = request.GET.get("internal_id","")
    lv_unread = Redister_Business.objects.filter(status=3).count()

    topic = None
    data = None
    if request.method == "POST":
        topic = request.POST.get("topic","")
        data = request.POST.get("data","")

    if internal_id:#删除
        internal_announcement = Internal_announcement.objects.get(pk=internal_id)
        if not request.user.is_superuser and delete_announcement_inner(request,internal_announcement,business):
            internal_announcement.is_active = 0
            internal_announcement.save()
            messages.info(request,u"内部公告删除成功!")
            # load_process_message(request,{},{},u'\u5185\u90e8\u516c\u544a\u5220\u9664(\u9762\u5411\u5458\u5de5)',internal_id,business,diffs_str=False)
            return redirect("/oa/announcement_employee/#announcement_employee")
        else:
            return redirect("/erp/no_permission/")

    if business:
        internals = business.internal_announcement_set.filter(is_active=1)
    else:
        internals = Internal_announcement.objects.filter(is_active=1)
    read_messages = Read_message.objects.filter(read_business=business,read_user=request.user,model_name="internal_announcement")
    for read_message in read_messages:#获取已读的该模块里面当前user所读的条目
        read.append(read_message.record_id)

    if data:
        internals = internals.filter(add_time__year=int(data.split('-')[0]),add_time__month=int(data.split('-')[1]),add_time__day=int(data.split('-')[2]))
    if topic:
        internals = internals.filter(topic__icontains=topic)

    internals,page_range,paginator = paginatorPage(request,internals)
    return render_to_response("oa/announcement_employee.html",locals(),context_instance=RequestContext(request))

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def announcement_add_modify(request):#通知公告新增/修改/
    permissions = get_permissions(request)
    count = get_unread_examine(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    business = get_business(request)#获取机构
    internal_announcement = Internal_announcement()
    internal_id = request.GET.get("internal_id","")
    form = InternalForm()
    message = u"新增公告(*为必填项)"

    if request.method == "GET":
        if internal_id:
            message = u"修改公告(*为必填项)"
            internal = Internal_announcement.objects.get(pk=internal_id)
            if not check_internal_announcement(request,internal,business):
                return redirect("/erp/no_permission/")
            form = InternalForm(instance=internal)

    if request.method == "POST":
        if internal_id:
            internal_announcement = Internal_announcement.objects.get(pk=internal_id)
            old_announcement = model_to_dict(internal_announcement)
            form = InternalForm(request.POST,instance=internal_announcement)
            if form.is_valid():#修改
                form.save()
                messages.info(request,u"内部公告修改成功!")
                # load_process_message(request,old_announcement,model_to_dict(internal_announcement),u'\u5185\u90e8\u516c\u544a\u4fee\u6539(\u9762\u5411\u5458\u5de5)',internal_id,business)
                return redirect("/oa/announcement_employee/")
            else:
                messages.error(request,u"内部公告修改失败,请完善信息!")
        else:
            form = InternalForm(request.POST)
            if form.is_valid():#新增
                internal_announcement = form.instance
                internal_announcement.announcement_business = business
                internal_announcement.save()
                messages.info(request,u"内部公告添加成功!")
                # load_process_message(request,{},model_to_dict(internal_announcement),u'\u5185\u90e8\u516c\u544a\u6dfb\u52a0(\u9762\u5411\u5458\u5de5)',internal_announcement.id,business)
                return redirect("/oa/announcement_employee/")
            else:
                messages.error(request,u"内部公告添加失败,请完善信息!")

    return render_to_response("oa/announcement_add_modify.html",locals(),context_instance=RequestContext(request))

''' 工作汇报 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def daily_work(request):#工作汇报列表/删除
    permissions = get_permissions(request)
    business = get_business(request)#获取机构
    count = get_unread_examine(request)
    user_agents,total_unread = get_user_agents(request,business)
    id = request.GET.get("daily_id","")
    lv_unread = Redister_Business.objects.filter(status=3).count()
    name = None
    data = None
    if request.method == "POST":
        name = request.POST.get("name","")
        data = request.POST.get("data","")

    if id:#删除
        daily = Daily_work.objects.get(pk=id)
        if apply.daily_work_delete(request,daily):
            daily.delete()
            con = ContentType.objects.filter(model="daily_work")
            All_Examine.objects.filter(content_type=con,examine_business=business,object_id=id).delete()
            messages.info(request,u"工作汇报删除成功!")
            # load_process_message(request,{},{},u'\u5de5\u4f5c\u6c47\u62a5\u5220\u9664',id,business,diffs_str=False)
            return redirect("/oa/daily_work/#daily_work")
        else:
             return redirect("/erp/no_permission/")

    try:
        user_business = request.user.business
    except:
        user_business = None
    if business:
        # if request.user.last_name == u"客户机构":
        if user_business:
            daily_works = business.daily_work_set.filter(is_active=1)
        else:
            daily_works = business.daily_work_set.filter(is_active=1,user=request.user)
    else:
        daily_works = Daily_work.objects.filter(is_active=1)

    if data:
        daily_works = daily_works.filter(time__year=int(data.split('-')[0]),time__month=int(data.split('-')[1]),time__day=int(data.split('-')[2]))
    if name:
        daily_works = daily_works.filter(user__first_name__icontains=name)

    daily_works,page_range,paginator = paginatorPage(request,daily_works)
    return render_to_response("oa/daily_work.html",locals(),context_instance=RequestContext(request))

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def daily_work_add_modify(request):#工作汇报新增
    permissions = get_permissions(request)
    count = get_unread_examine(request)
    business = get_business(request)#获取机构
    lv_unread = Redister_Business.objects.filter(status=3).count()
    try:
        if request.user.is_superuser or request.user.business:
            return render_to_response("404.html",locals(),context_instance=RequestContext(request))
    except:
        pass
    message = u"新增工作汇报(*为必填项)"
    daily_work = Daily_work()
    form = DailyForm()

    user_list = get_emp_self(request,business)

    if request.method == "GET":
        ''' 获取该机构的所有员工 '''


        form.fields['examine_user'].queryset = User.objects.filter(pk__in=user_list)

    if request.method == "POST":
        form = DailyForm(request.POST)

        if form.is_valid():#新增
            form.save()
            daily_work = form.instance
            daily_work.business = business
            daily_work.user = request.user
            daily_work.save()
            for key,val in form.cleaned_data.items():#获取审批USER，并创建
                    if key == "examine_user":
                        all_examine(business,daily_work,val)
            messages.info(request,u"工作汇报新增成功!")
            # load_process_message(request,{},model_to_dict(daily_work),u'\u5de5\u4f5c\u6c47\u62a5\u65b0\u589e',daily_work.id,business)
            return redirect("/oa/daily_work/#daily_work")
        else:
            messages.error(request,u"工作汇报新增失败,请完善信息!")
            form.fields['examine_user'].queryset = User.objects.filter(pk__in=user_list)

    return render_to_response("oa/daily_add_modify.html",locals(),context_instance=RequestContext(request))

''' 费用申请 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def cost_add_modify(request):#费用新增
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    try:
        if request.user.is_superuser or request.user.business:
            return render_to_response("404.html",locals(),context_instance=RequestContext(request))
    except:
        pass
    message = u"新增费用申请(*为必填项)"
    cost_id = request.GET.get("cost_id","")
    costApplication = Cost_application()
    form = CostForm()

    ''' 获取该机构的所有员工 '''
    user_list = get_emp_self(request,business)
    # form.fields['examine_user'].queryset = User.objects.filter(pk__in=user_list)

    if request.method == "POST":
        form = CostForm(request.POST)

        if form.is_valid():
            form.save()
            costApplication = form.instance
            costApplication.business = business
            costApplication.user = request.user
            costApplication.save()
            for key,val in form.cleaned_data.items():#获取审批USER，并创建
                if key == "examine_user":
                    all_examine(business,costApplication,val)
            messages.info(request,u"费用申请新增成功!")
            # load_process_message(request,{},model_to_dict(costApplication),u'\u8d39\u7528\u7533\u8bf7\u65b0\u589e',costApplication.id,business)
            return redirect("/oa/cost_application/#cost_application")
        else:
            messages.error(request,u"费用申请新增失败,请完善信息!")
    form.fields['examine_user'].queryset = User.objects.filter(pk__in=user_list)
    return render_to_response("oa/cost_add_modify.html",locals(),context_instance=RequestContext(request))

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def cost_application(request):#费用列表和删除
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    cost_id = request.GET.get("cost_id","")

    name = None
    data = None
    if request.method == "POST":
        name = request.POST.get("name","")
        data = request.POST.get("data","")

    if cost_id:#删除
        cost = Cost_application.objects.get(pk=cost_id)
        if apply.cost_application_delete(request,cost):
            cost.delete()
            con = ContentType.objects.filter(model="cost_application")
            All_Examine.objects.filter(content_type=con,examine_business=business,object_id=cost_id).delete()
            messages.info(request,u"费用申请删除成功!")
            # load_process_message(request,{},{},u'\u8d39\u7528\u7533\u8bf7\u5220\u9664',cost_id,business,diffs_str=False)
            return redirect("/oa/cost_application/#cost_application")
        else:
             return redirect("/erp/no_permission/")

    try:
        user_business = request.user.business
    except:
        user_business = None
    if business:
        # if request.user.last_name == u"客户机构":
        if user_business:
            costs = business.cost_application_set.filter(is_active=1)
        else:
            costs = business.cost_application_set.filter(is_active=1,user=request.user)
    else:
        costs = Cost_application.objects.filter(is_active=1)

    if data:
        costs = costs.filter(time__year=int(data.split('-')[0]),time__month=int(data.split('-')[1]),time__day=int(data.split('-')[2]))
    if name:
        costs = costs.filter(user__first_name__icontains=name)

    costs,page_range,paginator = paginatorPage(request,costs)
    return render_to_response("oa/cost_application.html",locals(),context_instance=RequestContext(request))

''' 请假管理 '''

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def leave_management(request):#请假列表和删除
    permissions = get_permissions(request)
    count = get_unread_examine(request)
    business = get_business(request)
    user_agents,total_unread = get_user_agents(request,business)
    leave_id = request.GET.get("leave_id","")
    lv_unread = Redister_Business.objects.filter(status=3).count()
    name = None
    data = None
    if request.method == "POST":
        name = request.POST.get("name","")
        data = request.POST.get("data","")

    if leave_id:#删除
        leave = Leave_management.objects.get(pk=leave_id)
        if apply.leave_management_delete(request,leave):
            leave.delete()
            con = ContentType.objects.filter(model="leave_management")
            All_Examine.objects.filter(content_type=con,examine_business=business,object_id=leave_id).delete()
            messages.info(request,u"请假申请删除成功!")
            # load_process_message(request,{},{},u'\u8bf7\u5047\u7533\u8bf7\u5220\u9664',leave_id,business,diffs_str=False)
            return redirect("/oa/leave_management/#leave_management")
        else:
             return redirect("/erp/no_permission/")

    try:
        user_business = request.user.business
    except:
        user_business = None
    if business:
        # if request.user.last_name == u"客户机构":
        if user_business:
            leaves = business.leave_management_set.filter(is_active=1)
        else:
            leaves = business.leave_management_set.filter(is_active=1,user=request.user)
    else:
        leaves = Leave_management.objects.filter(is_active=1)

    if data:
        leaves = leaves.filter(time__year=int(data.split('-')[0]),time__month=int(data.split('-')[1]),time__day=int(data.split('-')[2]))
    if name:
        leaves = leaves.filter(user__first_name__icontains=name)

    leaves,page_range,paginator = paginatorPage(request,leaves)
    return render_to_response("oa/leave_application.html",locals(),context_instance=RequestContext(request))

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def leave_add_modify(request):#请假新增和修改
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    try:
        if request.user.is_superuser or request.user.business:
            return render_to_response("404.html",locals(),context_instance=RequestContext(request))
    except:
        pass
    message = u"新增请假申请(*为必填项)"
    leave_id = request.GET.get("leave_id","")
    leave = Leave_management()
    form = LeaveForm()

    ''' 获取该机构的所有员工 '''
    user_list = get_emp_self(request,business)

    if request.method == "POST":
        form = LeaveForm(request.POST)

        if form.is_valid():
            form.save()
            leave = form.instance
            leave.business = business
            leave.user = request.user
            leave.save()
            for key,val in form.cleaned_data.items():#获取审批USER，并创建
                if key == "examine_user":
                    all_examine(business,leave,val)
            messages.info(request,u"请假申请新增成功!")
            # load_process_message(request,{},model_to_dict(leave),u'\u8bf7\u5047\u7533\u8bf7\u65b0\u589e',leave.id,business)
            return redirect("/oa/leave_management/#leave_management")
        else:
            messages.error(request,u"请假申请新增失败,请完善信息!")
    form.fields['examine_user'].queryset = User.objects.filter(pk__in=user_list)
    return render_to_response("oa/leave_add_modify.html",locals(),context_instance=RequestContext(request))

''' 出差申请 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def travel_apply(request):#出差申请列表和删除
    travel_id = request.GET.get("travel_id","")
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    travel_id = request.GET.get("travel_id","")
    name = None
    data = None
    if request.method == "POST":
        name = request.POST.get("name","")
        data = request.POST.get("data","")

    if travel_id:#删除
        travel_apply = Travel_apply.objects.get(pk=travel_id)
        if apply.travel_apply_delete(request,travel_apply):
            travel_apply.delete()
            con = ContentType.objects.filter(model="travel_apply")
            All_Examine.objects.filter(content_type=con,examine_business=business,object_id=travel_id).delete()
            messages.info(request,u"出差申请删除成功!")
            # load_process_message(request,{},{},u'\u51fa\u5dee\u7533\u8bf7\u5220\u9664',travel_id,business,diffs_str=False)
            return redirect("/oa/travel_apply/#travel_apply")
        else:
            return redirect("/erp/no_permission/")
    try:
        user_business = request.user.business
    except:
        user_business = None
    if business:
        # if request.user.last_name == u"客户机构":
        if user_business:
            travels = business.travel_apply_set.filter(is_active=1)
        else:
            travels = business.travel_apply_set.filter(is_active=1,user=request.user)
    else:
        travels = Travel_apply.objects.filter(is_active=1)

    if data:
        travels = travels.filter(time__year=int(data.split('-')[0]),time__month=int(data.split('-')[1]),time__day=int(data.split('-')[2]))
    if name:
        travels = travels.filter(user__first_name__icontains=name)

    travels,page_range,paginator = paginatorPage(request,travels)
    return render_to_response("oa/travel_apply.html",locals(),context_instance=RequestContext(request))

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def travel_add_modify(request):#出差申请新增
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    try:
        if request.user.is_superuser or request.user.business:
            return render_to_response("404.html",locals(),context_instance=RequestContext(request))
    except:
        pass
    message = u"出差请假申请(*为必填项)"
    travel_id = request.GET.get("travel_id","")
    travel = Travel_apply()
    form = TravelForm()

    ''' 获取该机构的所有员工 '''
    user_list = get_emp_self(request,business)

    if request.method == "POST":
        form = TravelForm(request.POST)
        if form.is_valid():
            form.save()
            travel = form.instance
            travel.business = business
            travel.user = request.user
            travel.save()
            for key,val in form.cleaned_data.items():#获取审批USER，并创建
                if key == "examine_user":
                    # travel_apply_examine(business,travel,val)
                    all_examine(business,travel,val)
            messages.info(request,u"出差申请新增成功!")
            # load_process_message(request,{},model_to_dict(travel),u'\u51fa\u5dee\u7533\u8bf7\u65b0\u589e',travel.id,business)
            return redirect("/oa/travel_apply/#travel_apply")
        else:
            messages.error(request,u"出差申请新增失败,请完善信息!")
    form.fields['examine_user'].queryset = User.objects.filter(pk__in=user_list)
    return render_to_response("oa/travel_add_modify.html",locals(),context_instance=RequestContext(request))


''' 已读存储 '''
def read_message(request,model_name,record_id,business):
    ''' 判断该记录是否存在 '''
    message = Read_message.objects.filter(model_name=model_name,record_id=record_id,read_business=business,read_user=request.user)
    if not message:#如果存在就忽略，不存在就添加
        readMessage = Read_message(model_name=model_name,record_id=record_id,read_business=business,read_user=request.user)
        readMessage.save()

''' 审核申请 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def edit_examine(request):
    record_id = request.GET.get("id","")
    contype = request.GET.get("contype","")
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    if request.method == "GET":
        con_type = ContentType.objects.get(model=contype)
        chinese_type = dict_map2[contype]
        if contype == 'daily_work':
            daily = Daily_work.objects.get(business=business,pk=record_id)
        # print record_id,request.user.id,con_type.id
        All_Examine.objects.filter(object_id=record_id,examine_user=request.user.id,content_type=con_type).update(read_status='2')
        all_examine = All_Examine.objects.get(object_id=record_id,examine_user=request.user.id,content_type=con_type.id)
        form = AllExamineForm(instance=all_examine)
        message = u"申请审核"
        check_remark = request.GET.get("check_remark","")

    if request.method == "POST":
        examine = All_Examine.objects.get(pk=record_id)
        form = AllExamineForm(request.POST)
        if form.is_valid():
            for key,val in form.cleaned_data.items():
                setattr(examine,key,val)
        examine.examine_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        examine.save()
        if request.POST.get("examine_status") != "3":
            messages.info(request,u"审核成功!")
        return redirect("/oa/examine_list/")

    return render_to_response("oa/edit_examine.html",locals(),context_instance=RequestContext(request))


'''--------------------------------------被调用的方法,不是view---------------------------------------------------'''
def ajax_name(request):
    type = request.GET.get("type","")
    lv_unread = Redister_Business.objects.filter(status=3).count()
    if type:
        check = CheckWork_history.objects.get(pk=int(request.GET.get("id")))
        business = check.check_business_history.name.encode("utf-8")
        first_name = check.check_history.first_name.encode("utf-8")
    else:
        check = CheckWork.objects.get(pk=int(request.GET.get("id")))
        business = check.check_business.name.encode("utf-8")
        first_name = check.check_user.first_name.encode("utf-8")
    return JsonResponse({"name":first_name,"business":business})

''' 按机构过滤员工在地图上显示 '''
def get_self_checks(request):

    try:
        user_agent = request.user.agent
    except:
        user_agent = None
    if request.user.is_superuser:#超级管理员
        checks = CheckWork.objects.all()
        return checks
    # elif request.user.last_name == u"员工":
    elif user_agent:
        agent = Agent.objects.get(user_id=request.user.id)
        business = Business.objects.get(id=agent.business.id)
    else:
        business = Business.objects.get(user_id=request.user.id)
    checks = business.checkwork_set.all()

    return checks

''' 按机构过滤员工在地图上历史轨迹显示 '''
def get_history_checks(request):
    checks = None
    id = request.POST.get("option","")
    agent = Agent.objects.get(pk=id)
    dataTime = request.POST.get("dataTime","")
    dataEnd = request.POST.get("dataEnd","")
    param = time.strptime(dataEnd, '%Y-%m-%d')
    param = datetime.date(param.tm_year,param.tm_mon,param.tm_mday)
    data_day = param+datetime.timedelta(days=1)#一天之内

    # business = get_business(request)
    checks = CheckWork_history.objects.filter(check_history=agent.user.id,check_business_history=agent.business.id,check_time__gte=dataTime,check_time__lt=data_day)

    return checks,agent,dataTime,dataEnd

def get_history_checks_days(request,id,start,end):
    checks = None
    business = get_business(request)
    agent = Agent.objects.get(pk=id)
    checks = CheckWork_history.objects.filter(check_history=agent.user,check_business_history=business,check_time__gt=start,check_time__lt=end)

    return checks,agent

def get_business(request):
    business = None
    try:
        user_agent = request.user.agent
    except:
        user_agent = None
    if request.user.is_superuser:#超级管理员
        return business
    # elif request.user.last_name == u"员工":
    elif user_agent:
        agent = Agent.objects.get(user_id=request.user.id)
        business = Business.objects.get(id=agent.business.id)
    else:
        business = Business.objects.get(user_id=request.user.id)

    return business


'''--------------------------------------end 被调用的方法,不是 view---------------------------------------------------'''








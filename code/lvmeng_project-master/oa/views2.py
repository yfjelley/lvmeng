#coding:utf-8
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.shortcuts import render_to_response,redirect
import time
from models import *
from forms import *
from django.contrib.contenttypes.models import ContentType
from erp.utils import Apply_Process,delete_daily
from django.core.paginator import Paginator,EmptyPage
from erp.utils import load_process_message,get_user_agents
from django.forms.models import model_to_dict
apply = Apply_Process()
dict_map = {
    "cost_application":u"费用申请",
    "travel_apply":u"出差申请",
    "leave_management":u"请假申请",
    "daily_work":u"工作汇报",
}

''' 存储申请审核object '''

def all_examine(business,cost,args):
    for arg in args:
        examines = All_Examine(
                            examine_business = business,
                            examine_user = arg,
                            examine = cost
        )
        examines.save()

''' 查看费用申请审核情况 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def cost_examine(request):
    permissions = get_permissions(request)
    count = get_unread_examine(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    business = get_business(request)
    cost_id = request.GET.get("cost_id")
    cost_application = Cost_application.objects.get(pk=cost_id)
    if apply.check_cost_application_examine(request,cost_application,business):
        con_type = ContentType.objects.get(model="cost_application")
        cost_examines = All_Examine.objects.filter(object_id=cost_id,content_type=con_type)
        return render_to_response("oa/cost_examines.html",locals(),context_instance=RequestContext(request))
    else:
        return redirect("/erp/no_permission/")

''' 查看自己的费用申请审核列表 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def examine_list(request):
    permissions = get_permissions(request)
    count = get_unread_examine(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    apply_type = request.POST.get("apply_type","")
    apply_chinese = None
    objs = []
    if apply_type:
        apply_chinese = dict_map[apply_type]
        costs =  ContentType.objects.get(model=apply_type)
        all_examines = All_Examine.objects.filter(content_type=costs,examine_user=request.user,is_active=1)
    else:
        all_examines = All_Examine.objects.filter(examine_user=request.user,is_active=1)
    for examines in all_examines:
        if examines.examine:
            exam = examines.examine
            exam.Id = examines.examine.id
            exam.status = examines.read_status
            exam.examine_status = examines.examine_status
            exam.type = dict_map[exam.__class__.__name__.lower()]
            # print exam.__class__.__name__.lower(),dict_map[exam.__class__.__name__.lower()]
            exam.model = exam.__class__.__name__.lower()
            objs.append(exam)
    objs,page_range,paginator = paginatorPage(request,objs)
    return render_to_response("oa/examine_list.html",locals(),context_instance=RequestContext(request))

''' 查看请假申请审核情况 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def leave_examine(request):

    permissions = get_permissions(request)
    count = get_unread_examine(request)
    business = get_business(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    leave_id = request.GET.get("leave_id")
    leave_management = Leave_management.objects.get(pk=leave_id)
    if apply.check_leave_management_examine(request,leave_management,business):
        con_type = ContentType.objects.get(model="leave_management")
        leave_examines = All_Examine.objects.filter(object_id=leave_id,content_type=con_type)
        return render_to_response("oa/leave_examines.html",locals(),context_instance=RequestContext(request))
    else:
         return redirect("/erp/no_permission/")


''' 查看出差申请审核情况 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def travel_examine(request):

    permissions = get_permissions(request)
    count = get_unread_examine(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    business = get_business(request)
    travel_id = request.GET.get("travel_id")
    travel_apply = Travel_apply.objects.get(pk=travel_id)
    if apply.travel_apply_management_examine(request,travel_apply,business):
        con_type = ContentType.objects.get(model="travel_apply")
        travel_examines = All_Examine.objects.filter(object_id=travel_id,content_type=con_type)
        return render_to_response("oa/travel_examines.html",locals(),context_instance=RequestContext(request))
    else:
        return redirect("/erp/no_permission/")

''' 查看工作汇报申请审核情况 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def daily_work_examine(request):
    business = get_business(request)
    permissions = get_permissions(request)
    count = get_unread_examine(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    daily_id = request.GET.get("daily_id")
    daily_work = Daily_work.objects.get(pk=daily_id)
    if apply.check_daily_work_examine(request,daily_work,business):
        con_type = ContentType.objects.get(model="daily_work")
        daily_examines = All_Examine.objects.filter(object_id=daily_id,content_type=con_type)
        return render_to_response("oa/daily_work_examine.html",locals(),context_instance=RequestContext(request))
    else:
        return redirect("/erp/no_permission/")

''' 获取本机构的员工 '''
def get_emp_self(request,business):#获取本机构的员工
    user_list = []
    agent = Agent.objects.filter(business=business,is_active=1)

    for age in agent:
        if request.user != age.user:
            user_list.append(age.user.id)
    # user_list.append(business.user.id)
    return user_list

''' 每日待办列表 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def daily_todo_list(request):#每日待办列表/删除
    permissions = get_permissions(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    count = get_unread_examine(request)
    business = get_business(request)
    user_agents,total_unread = get_user_agents(request,business)
    daily_id = request.GET.get("daily_id","")
    data = None
    if daily_id:
        daily = Daily_to_do.objects.filter(pk=daily_id)
        if not delete_daily(request,daily[0]):
            return redirect("/erp/no_permission/")
        daily.update(is_active=0)
        messages.info(request,u"每日待办删除成功!")
        # load_process_message(request,{},{},u'\u6bcf\u65e5\u5f85\u529e\u5220\u9664',daily_id,business,diffs_str=False)
        return redirect("/oa/daily_todo_list/#daily_todo_list")

    if request.method == "POST":
        # name = request.POST.get("name","")
        data = request.POST.get("data","")

    if data:
        dailys = Daily_to_do.objects.filter(todo_user=request.user,is_active=1,add_time__year=int(data.split('-')[0]),add_time__month=int(data.split('-')[1]),add_time__day=int(data.split('-')[2]))
    else:
        dailys = Daily_to_do.objects.filter(todo_user=request.user,is_active=1)
    daily_todos,page_range,paginator = paginatorPage(request,dailys)
    return render_to_response("oa/daily_todo_list.html",locals(),context_instance=RequestContext(request))

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def daily_todo_add_modify(request):
    daily_id = request.GET.get("daily_id","")
    lv_unread = Redister_Business.objects.filter(status=3).count()
    count = get_unread_examine(request)
    business = get_business(request)
    permissions = get_permissions(request)
    user_agents,total_unread = get_user_agents(request,business)

    if request.method == "GET":
        if daily_id:
            message = u"修改每日待办事件(*为必填项)"
            daily = Daily_to_do.objects.get(pk=daily_id)
            if not delete_daily(request,daily):
                return redirect("/erp/no_permission/")
            form = DailyToDoForm(instance=daily)
        else:
            form = DailyToDoForm()
            message = u"添加每日待办事件(*为必填项)"

    if request.method == "POST":
        if daily_id:
            daily = Daily_to_do.objects.get(pk=daily_id)
            old_daily = model_to_dict(daily)
            form = DailyToDoForm(request.POST,instance=daily)
            # if form.is_valid() and form.has_changed():#修改
            if form.is_valid():#修改
                form.save()
                messages.info(request,u"每日待办修改成功!")
                # load_process_message(request,old_daily,model_to_dict(daily),u'\u6bcf\u65e5\u5f85\u529e\u4fee\u6539',daily_id,business,)
            else:
                messages.error(request,u"每日待办修改失败,请完善信息!")
                return render_to_response("oa/daily_todo_add_modify.html",locals(),context_instance=RequestContext(request))
        else:
            form = DailyToDoForm(request.POST)
            if form.is_valid():#新增
                form.save()
                daily_to_do = Daily_to_do()
                daily_to_do = form.instance
                daily_to_do.todo_user = request.user
                daily_to_do.save()
                messages.info(request,u"每日待办添加成功!")
                # load_process_message(request,{},model_to_dict(daily_to_do),u'\u6bcf\u65e5\u5f85\u529e\u6dfb\u52a0',daily_to_do.id,business,)
            else:
                messages.error(request,u"每日待办添加失败,请完善信息!")
                return render_to_response("oa/daily_todo_add_modify.html",locals(),context_instance=RequestContext(request))

        return redirect("/oa/daily_todo_list")

    return render_to_response("oa/daily_todo_add_modify.html",locals(),context_instance=RequestContext(request))


''' 获取未读申请 '''
def get_unread_examine(request):
    id = request.user.id
    business = get_business(request)
    return All_Examine.objects.filter(examine_user_id=id,examine_business=business,is_active=1,read_status="1").count()

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
        # emp = Employee.objects.get(user_id=request.user.id)
        # business = Business.objects.get(id=emp.business.id)

    return business

def get_permissions(request):
    permissions = []
    try:
        user_agent = request.user.agent
    except:
        user_agent = None
    # if request.user.last_name == u"员工":
    if user_agent:
        for permission in request.user.agent.permissions.all():
            permissions.append('auth.'+permission.codename)
    else:
        for permission in request.user.get_all_permissions():
            permissions.append(permission)
    return permissions

''' 考勤表 '''
@login_required(login_url='login/')
def check_table2(request):
    permissions = get_permissions(request)
    business = get_business(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    current = request.GET.get("dataTime","")
    if not current:
        current = datetime.datetime.now().strftime("%Y-%m-%d")
    param = time.strptime(current, '%Y-%m-%d')
    param = datetime.date(param.tm_year,param.tm_mon,param.tm_mday)
    end = param + datetime.timedelta(days=1)

    names = []
    checkTime = []
    checks = CheckWork_history.objects.filter(check_business_history=business,check_time__gte=current,check_time__lt=end).order_by("check_history")

    for check in checks:
        if check.check_history not in names:
            times = []
            names.append(check.check_history)
            checkUsers = CheckWork_history.objects.filter(check_business_history=business,check_history=check.check_history,check_time__gte=current,check_time__lt=end).order_by("check_time")
            for check_user in checkUsers:
                # vari = u"地址:"+check_user.address+u"<>时间:"+str(check_user.check_time)
                # times.append(vari)
                times.append(u"地址:"+check_user.address)
                times.append(u"时间:"+str(check_user.check_time))
            checkTime.append(times)
    return render_to_response("oa/table2.html",locals(),context_instance=RequestContext(request))

import calendar
@login_required(login_url='login/')
def check_table(request):
    permissions = get_permissions(request)
    business = get_business(request)
    count = get_unread_examine(request)
    user_agents,total_unread = get_user_agents(request,business)

    start = request.POST.get("start","")
    lv_unread = Redister_Business.objects.filter(status=3).count()
    end = request.POST.get("end","")
    qr_code = request.POST.get("qr_code","")
    qr_agents = []
    # qr_agent = None

    if request.user.is_superuser:
        agents = Agent.objects.filter(is_active=1)
        for age in agents:
            qrcodes = age.business.business_num+str(age.agent_num)
            age.code = qrcodes
            # qr_codes.append(age.business.business_num+str(age.agent_num))
            if qr_code:
                if qrcodes == qr_code:
                    qr_agents.append(age)
    else:
        agents = Agent.objects.filter(business=business,is_active=1)
        for age in agents:
            qrcodes = business.business_num+str(age.agent_num)
            age.code = qrcodes
            # qr_codes.append(business.business_num+str(age.agent_num))
            if qr_code:
                if qrcodes == qr_code:
                    qr_agents.append(age)
    names = []
    checkTime = []
    date_lists = []

    if not start and not end and not qr_code:
        ''' 获取当前月份 '''
        day_now = time.localtime()
        # print day_now
        start = '%d-%02d-01' % (day_now.tm_year, day_now.tm_mon)  # 月初
        tm_year = day_now.tm_year
        mon = day_now.tm_mon
        wday, monthRange = calendar.monthrange(day_now.tm_year, day_now.tm_mon)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
        end = '%d-%02d-%02d' % (day_now.tm_year, day_now.tm_mon, monthRange)# 月末

        param = time.strptime(start, '%Y-%m-%d')
        start_param = datetime.date(param.tm_year,param.tm_mon,param.tm_mday)
        # print start_param
        param2 = time.strptime(end, '%Y-%m-%d')
        end_param = datetime.date(param2.tm_year,param2.tm_mon,param2.tm_mday)
        end_param2 = end_param + datetime.timedelta(days=1)

        riQis = range(calendar.monthrange(day_now.tm_year, day_now.tm_mon)[1]+1)[1:]
        for ri in riQis:
            date_lists.append(str(mon)+'-'+str(ri)+'/'+get_week_day(str(tm_year)+'-'+str(mon)+'-'+str(ri)))

        for agent in agents:
            check_in = []
            check_out = []
            riQis.insert(0,0)
            for riQi in riQis[:-1]:
                param = strp_time(str(start_param),riQi)
                param2 = strp_time(str(param),1)
                # print param
                # try:
                checks = CheckWork_history.objects.filter(check_history_id=agent.user.id,check_time__gte=param,check_time__lt=param2)
                checks_in = checks.filter(type=1)#签到
                checks_out = checks.filter(type=0)#签退
                if checks_in:
                    Time_now = merge_time(str(checks_in[0].check_time.hour)+':'+str(checks_in[0].check_time.minute))
                    # Time_now = str(checks_in[0].check_time.hour)+':'+str(checks_in[0].check_time.minute)
                    # counts = checks.count()
                    try:
                        check_in.append(Time_now+u'/地址：'+checks_in[0].address)
                    except:
                        check_in.append(Time_now)
                else:
                    check_in.append(None)

                if checks_out:
                    Time_end = merge_time(str(checks_out[len(checks_out)-1].check_time.hour)+':'+str(checks_out[len(checks_out)-1].check_time.minute))
                    # Time_end = str(checks_out[len(checks_out)-1].check_time.hour)+':'+str(checks_out[len(checks_out)-1].check_time.minute)
                    try:
                        check_out.append(Time_end+u'/地址：'+checks_out[len(checks_out)-1].address)
                    except:
                        check_out.append(Time_end)
                else:
                    check_out.append(None)
                # else:
                #     check_in.append(None)
                #     check_out.append(None)
                # except:
                #     check_in.append(None)
                #     check_out.append(None)
            riQis.pop(0)
            agent.checkIn = check_in
            agent.checkOut = check_out
    else:
        d1 = datetime.datetime(int(start.split('-')[0]),int(start.split('-')[1]),int(start.split('-')[2]))
        d2 = datetime.datetime(int(end.split('-')[0]),int(end.split('-')[1]),int(end.split('-')[2]))
        mails_day = (d2 - d1).days
        for ran in range(mails_day+1):
            date_lists.append(strp_day(str(start),ran)+'/'+get_week_day(str(strp_time(start,ran))))

        if qr_agents:
            for qr_agent in qr_agents:
                check_in = []
                check_out = []
                for riQi in range(mails_day+1):
                    param = strp_time(str(start),riQi)
                    param2 = strp_time(str(param),1)
                    checks = CheckWork_history.objects.filter(check_history_id=qr_agent.user.id,check_time__gte=param,check_time__lt=param2)
                    # if checks:
                    #     counts = checks.count()
                    #     Time_now = str(checks[0].check_time.hour)+':'+str(checks[0].check_time.minute)
                    #     try:
                    #         check_in.append(Time_now+u'/地址：'+checks[0].address)
                    #     except:
                    #         check_in.append(Time_now)
                    #
                    #     if counts > 1:
                    #         Time_end = str(checks[counts-1].check_time.hour)+':'+str(checks[counts-1].check_time.minute)
                    #         try:
                    #             check_out.append(Time_end+u'/地址：'+checks[0].address)
                    #         except:
                    #             check_out.append(Time_end)
                    #     else:
                    #         check_out.append(None)
                    # else:
                    #     check_in.append(None)
                    #     check_out.append(None)
                    checks_in = checks.filter(type=1)#签到
                    checks_out = checks.filter(type=0)#签退
                    if checks_in:
                        # Time_now = str(checks_in[0].check_time.hour)+':'+str(checks_in[0].check_time.minute)
                        Time_now = merge_time(str(checks_in[0].check_time.hour)+':'+str(checks_in[0].check_time.minute))
                        # counts = checks.count()
                        try:
                            check_in.append(Time_now+u'/地址：'+checks_in[0].address)
                        except:
                            check_in.append(Time_now)
                    else:
                        check_in.append(None)

                    if checks_out:
                        Time_end = merge_time(str(checks_out[len(checks_out)-1].check_time.hour)+':'+str(checks_out[len(checks_out)-1].check_time.minute))
                        # Time_end = str(checks_out[len(checks_out)-1].check_time.hour)+':'+str(checks_out[len(checks_out)-1].check_time.minute)
                        try:
                            check_out.append(Time_end+u'/地址：'+checks_out[len(checks_out)-1].address)
                        except:
                            check_out.append(Time_end)
                    else:
                        check_out.append(None)

                qr_agent.checkIn = check_in
                qr_agent.checkOut = check_out
        else:
            for agent in agents:
                check_in = []
                check_out = []
                # riQis.insert(0,0)
                for riQi in range(mails_day+1):
                    param = strp_time(str(start),riQi)
                    param2 = strp_time(str(param),1)
                    # print param
                    # try:
                    checks = CheckWork_history.objects.filter(check_history_id=agent.user.id,check_time__gte=param,check_time__lt=param2)
                    # if checks:
                    #     counts = checks.count()
                    #     Time_now = str(checks[0].check_time.hour)+':'+str(checks[0].check_time.minute)
                    #     try:
                    #         check_in.append(Time_now+u'/地址：'+checks[0].address)
                    #     except:
                    #         check_in.append(Time_now)
                    #
                    #     if counts > 1:
                    #         Time_end = str(checks[counts-1].check_time.hour)+':'+str(checks[counts-1].check_time.minute)
                    #         try:
                    #             check_out.append(Time_end+u'/地址：'+checks[0].address)
                    #         except:
                    #             check_out.append(Time_end)
                    #     else:
                    #         check_out.append(None)
                    # else:
                    #     check_in.append(None)
                    #     check_out.append(None)
                    # except:
                    #     check_in.append(None)
                    #     check_out.append(None)
                    checks_in = checks.filter(type=1)#签到
                    checks_out = checks.filter(type=0)#签退
                    if checks_in:
                        # Time_now = str(checks_in[0].check_time.hour)+':'+str(checks_in[0].check_time.minute)
                        Time_now = merge_time(str(checks_in[0].check_time.hour)+':'+str(checks_in[0].check_time.minute))
                        # counts = checks.count()
                        try:
                            check_in.append(Time_now+u'/地址：'+checks_in[0].address)
                        except:
                            check_in.append(Time_now)
                    else:
                        check_in.append(None)

                    if checks_out:
                        Time_end = merge_time(str(checks_out[len(checks_out)-1].check_time.hour)+':'+str(checks_out[len(checks_out)-1].check_time.minute))
                        # Time_end = str(checks_out[len(checks_out)-1].check_time.hour)+':'+str(checks_out[len(checks_out)-1].check_time.minute)
                        try:
                            check_out.append(Time_end+u'/地址：'+checks_out[len(checks_out)-1].address)
                        except:
                            check_out.append(Time_end)
                    else:
                        check_out.append(None)
                # riQis.pop(0)
                agent.checkIn = check_in
                agent.checkOut = check_out

    return render_to_response("oa/table2.html",locals(),context_instance=RequestContext(request))
    # return render_to_response("erp/example.html",locals(),context_instance=RequestContext(request))


def strp_time(kwarg,num):

    str_param = time.strptime(kwarg, '%Y-%m-%d')
    end_param = datetime.date(str_param.tm_year,str_param.tm_mon,str_param.tm_mday)
    param = end_param + datetime.timedelta(days=int(num))
    return param

def strp_day(kwarg,num):

    str_param = time.strptime(kwarg, '%Y-%m-%d')
    end_param = datetime.date(str_param.tm_year,str_param.tm_mon,str_param.tm_mday)
    param = end_param + datetime.timedelta(days=int(num))
    param_day = str(param).split('-')[1]+'-'+str(param).split('-')[2]
    return param_day

def get_week_day(kwarg):
    week_day_dict = {
        0 : u'周一',
        1 : u'周二',
        2 : u'周三',
        3 : u'周四',
        4 : u'周五',
        5 : u'周六',
        6 : u'周日',
      }
    Date=datetime.datetime.strptime(kwarg,'%Y-%m-%d')
    day = Date.weekday()
    return week_day_dict[day]

def merge_time(time_str):
    if len(time_str) == 5:
        return time_str
    string1 = ""
    string2 = ""
    time_lists = time_str.split(":")
    if len(time_lists[0])<2:
        string1 += "0"+time_lists[0]+":"
    else:
        string1 += time_lists[0]+":"
    if len(time_lists[1])<2:
        string2 += "0"+time_lists[1]
    else:
        string2 += time_lists[1]
    return string1+string2

def check_time_setting(request):
    count = get_unread_examine(request)
    permissions = get_permissions(request)
    business = get_business(request)#获取机构
    lv_unread = Redister_Business.objects.filter(status=3).count()
    if request.method == "GET":
        if request.user.is_superuser:
            check_settings = Check_Time_Setting.objects.all()
            check_settings,page_range,paginator = paginatorPage(request,check_settings)
            return render_to_response("oa/check_time_list.html",locals(),context_instance=RequestContext(request))
        check_setting = Check_Time_Setting.objects.filter(business=business)
        if check_setting.count():
            check_zero = check_setting[0]
            form = CheckTimeSettingForm(instance=check_zero)
        else:
            form = CheckTimeSettingForm()
        return render_to_response("oa/check_time_setting.html",locals(),context_instance=RequestContext(request))
    else:
        id = request.GET.get("id","")
        if id:
            check = Check_Time_Setting.objects.get(pk=id)
            if business == check.business:
                form = CheckTimeSettingForm(request.POST,instance=check)
            else:
                return redirect("/erp/no_permission/")
        else:
            form = CheckTimeSettingForm(request.POST)
        if form.is_valid():
            if id:
                form.save()#修改
            else:
                form.save(commit=False)
                check_time = Check_Time_Setting()
                check_time = form.instance
                check_time.business = business
                check_time.save()#新增
            messages.info(request,u"考勤时间设定成功!")
            return redirect("/oa/check_time_setting/#check_time_setting")
        else:
            return render_to_response("oa/check_time_setting.html",locals(),context_instance=RequestContext(request))

def paginatorPage(request,queryset,display_amount=10,after_range_num=3,bevor_range_num=3):
    paginator = Paginator(queryset,display_amount)

    page = int(request.GET.get('page','1'))
    try:
        objects = paginator.page(page)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    except:
        objects = paginator.page(1)

    if page >= after_range_num:
        page_rang = paginator.page_range[page-after_range_num:page+bevor_range_num]
    else:
        page_rang = paginator.page_range[0:page+bevor_range_num]

    return objects,page_rang,paginator




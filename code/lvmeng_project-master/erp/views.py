#coding:utf-8
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render,render_to_response,redirect
from django.http import JsonResponse
from models import *
from django.core.paginator import Paginator,EmptyPage
from forms import *
from oa.models import *
from oa.forms import *
from oa.views import read_message
from oa.views2 import get_emp_self
import datetime
from oa.views import get_business
import time
from api.models import Headline
from api.forms import HeadlineForm
from erp.views2 import get_permissions,send_email,send_email_emp,send_cancel_email
from oa.views2 import get_unread_examine
from django.views.generic import View
# from views2 import set_picture_size
from views2 import release_base_64,get_all_required,send_email_to_redister_person
from web_customer.models import Lv_Announcement,business_carousel
from web_customer.forms import Lv_announcement_Form,Business_Carousel_Form
from erp.utils import *
from django.contrib import messages
from api.models import VerificationCode
from django.forms.models import model_to_dict

# Create your views here.
#use modelform to display product info for edit
#get and post combined, add and edit combined
''' 对产品的操作（添加，修改） '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def product_process(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    if request.user.is_superuser:
        return redirect("/erp/no_permission/")
    product_id = request.GET.get("product_id","")
    try:
        product = Product.objects.get(id=product_id)
        if product not in business.product_set.filter(is_active=1):
            return redirect("/erp/no_permission/")
        message = u"修改现有产品:"+product.name+u"(*为必填项)"
    except:
        product = Product()
        message = u"创建新的产品(*为必填项)"
    form = ProductForm(instance = product)

    if request.method == 'POST': # If the form has been submitted...
        if product_id == "None":#新增
            form = ProductForm(request.POST or None, request.FILES)
            if form.is_valid():
                form.save()
                product = form.instance
                product.business =  Business.objects.get(id=business.id)
                product.save()
                messages.info(request,u"新增产品操作成功!")

                # load_process_message(request,{},model_to_dict(product),u'\u65b0\u589e\u65b0\u4ea7\u54c1',product.id,business,)

            else:
                messages.error(request,u"新增产品操作失败,请完善信息!")
                return render_to_response('erp/product.html',locals(),context_instance=RequestContext(request))
        else:#修改
            form = ProductForm(request.POST or None, request.FILES, instance=product)
            # if form.is_valid() and form.has_changed():
            if form.is_valid():
                model_product = Product.objects.get(id=product_id)
                form.save()
                messages.info(request,u"修改产品操作成功!")

                product_data = Product()
                product_data = form.instance

                # load_process_message(request,model_to_dict(model_product),model_to_dict(product_data),u'\u4ea7\u54c1\u4fee\u6539',product.id,business,)
            else:
                messages.error(request,u"修改产品操作失败,请完善信息!")
                return render_to_response('erp/product.html',locals(),context_instance=RequestContext(request))
        return redirect("/erp/product_list/#product_list")

    return render_to_response('erp/product.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def product_list(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    product_id = request.GET.get("product_id","")

    if product_id:
        product = Product.objects.get(id=product_id)
        if product_delete(request,product,business):
            product.is_active = 0
            product.save()
            messages.info(request,u"产品删除成功!")

            # load_process_message(request,{},{},u'\u5220\u9664\u4ea7\u54c1',product.id,business,diffs_str=False)
            return redirect("/erp/product_list/#product_list")
        else:
            return redirect("/erp/no_permission/")

    if request.user.is_superuser:#超级管理员
        products = Product.objects.filter(is_active=1)
    else:
        products = Product.objects.filter(is_active=1,business=business)

    conditions = {}
    if request.method == "POST":#搜索过滤
        product_name = items = request.POST.get("product_name","")
        product_type = items = request.POST.get("product_type","")
        start_time = items = request.POST.get("start_time","")
        end_time = items = request.POST.get("end_time","")
        conditions["name__icontains"] = product_name
        conditions["product_type__typeName__icontains"] = product_type
        if start_time:
            conditions["begin_date__gte"] = start_time
        if end_time:
            conditions["end_date__lte"] = end_time

    products = products.filter(**conditions)#搜索过滤
    if products:
        for pro in products:
            if pro.return_expected:
                pro.return_expected = str(pro.return_expected*100)
            else:
                pro.return_expected = 0
    products,page_range,paginator = paginatorPage(request,products)
    return render_to_response('erp/product_list.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='login/')
def admin_business_product(request):
    permissions,business,count,user_agents,total_unread = get_all_required(request)
    business_id =  request.GET.get("business_id","")
    if not request.user.is_superuser or not business_id:
        return redirect("/erp/no_permission/")
    count = get_unread_examine(request)
    permissions = get_permissions(request)#获取权限列表
    lv_unread = Redister_Business.objects.filter(status=3).count()

    products = Product.objects.filter(business=business_id,is_active=1)

    conditions = {}
    if request.method == "POST":#搜索过滤
        product_name = items = request.POST.get("product_name","")
        product_type = items = request.POST.get("product_type","")
        start_time = items = request.POST.get("start_time","")
        end_time = items = request.POST.get("end_time","")
        conditions["name__icontains"] = product_name
        conditions["product_type__typeName__icontains"] = product_type
        if start_time:
            conditions["begin_date__gte"] = start_time
        if end_time:
            conditions["end_date__lte"] = end_time

    products = products.filter(**conditions)#搜索过滤

    if products:
        for pro in products:
            if pro.return_expected:
                pro.return_expected = str(pro.return_expected*100)

            else:
                pro.return_expected = 0
    products,page_range,paginator = paginatorPage(request,products)
    return render_to_response('admin_erp/product_list.html',locals(),context_instance=RequestContext(request))

'''
创建用户[注：last_name是用户的角色，first_name是用户的中文名，username是用户的电话号码(用户名)，
初始密码默认：88888888 ]
'''
def create_user(username,name,email,last_name,password):#创建用户
    if password == "":
        password = 88888888
    user = User.objects.create_user(username=username,first_name=name,last_name=last_name,email=email,password=password)#新增用户名和密码
    user.save()
    return user

'''
删除用户登录许可：is_active=0
'''
def deleteUser(obj):
    user = User.objects.get(pk = obj.user.id)
    user.is_active = 0
    user.save()

''' 职位列表 '''
def position_list(request):
    if request.user.last_name == u"客户":
        return redirect("/customer_login/")

    lv_unread = Redister_Business.objects.filter(status=3).count()

    permissions,business,count,user_agents,total_unread = get_all_required(request)

    position_id = request.GET.get("position_id","")
    if position_id:
        position = Position.objects.get(pk=request.GET.get("position_id"))
        if check_position(request,position,business):
            position.delete()
            messages.info(request,u"职位删除成功!")
            # load_process_message(request,{},{},u'\u804c\u4f4d\u5220\u9664',position_id,business,diffs_str=False)
            return redirect("/erp/position_list/#position_list")
        else:
            return redirect("/erp/no_permission/")

    positions = Position.objects.filter(business=business)
    positions,page_range,paginator = paginatorPage(request,positions)
    return render_to_response("erp/position_list.html",locals(),context_instance=RequestContext(request))


'''
添加职位
'''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def position_add_modify(request):#添加职位
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    position_id = request.GET.get("position_id","")
    if request.user.is_superuser:
        return redirect("/erp/no_permission/")
    if request.method=="GET":
        if position_id:
            message = u"修改职位信息"
            position = Position.objects.get(pk=position_id)
            if not check_position(request,position,business):
                return redirect("/erp/no_permission/")
            form = PositionForm(instance=position)
        else:
            form = PositionForm()
            form.fields['entry_person'].initial = request.user.first_name
            form.fields['register_date'].initial = time.strftime("%Y-%m-%d",time.localtime())
            message = u"新增职位"
        form.fields['permissions'].queryset = Permission.objects.filter(id__gt=40,content_type_id=2)#过滤非自己定义的Permission
        return render_to_response("erp/position_add_modify.html",locals(),context_instance=RequestContext(request))
    else:
        position = Position()
        if position_id:#保存修改
            position = Position.objects.get(pk=position_id)
            old_position =  model_to_dict(position)
            form = PositionForm(request.POST,instance=position)
            if form.is_valid():
                for key,val in form.cleaned_data.items():
                    setattr(position,key,val)
                position.save()
                # load_process_message(request,old_position,model_to_dict(position),u'\u804c\u4f4d\u4fee\u6539',position_id,business)
                messages.info(request,u"职位修改成功!")
            else:
                messages.error(request,u"职位修改失败,请完善信息!")
                form.fields['permissions'].queryset = Permission.objects.filter(id__gt=40,content_type_id=2)#过滤非自己定义的Permission
                return render_to_response("erp/position_add_modify.html",locals(),context_instance=RequestContext(request))

        else:#保存新增
            form = PositionForm(request.POST)
            if form.is_valid():
                form.save()
                position = form.instance
                position.business = Business.objects.get(id=business.id)
                position.save()
                # load_process_message(request,{},model_to_dict(position),u'\u804c\u4f4d\u65b0\u589e',position.id,business,)
                messages.info(request,u"职位新增成功!")
            else:
                messages.error(request,u"职位新增失败,请完善信息!")
                form.fields['permissions'].queryset = Permission.objects.filter(id__gt=40,content_type_id=2)#过滤非自己定义的Permission
                return render_to_response("erp/position_add_modify.html",locals(),context_instance=RequestContext(request))
        return redirect("/erp/position_list/")

'''
客户机构操作（）
'''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def business_process(request):
    '''获取客户机构ID'''
    lv_unread = Redister_Business.objects.filter(status=3).count()
    if not request.user.is_superuser:
        permissions = get_permissions(request)#获取权限列表
        return render_to_response("erp/no_permission.html",locals(),context_instance=RequestContext(request))
    # permissions = get_permissions(request)#获取权限列表
    # count = get_unread_examine(request)
    permissions,business,count,user_agents,total_unread = get_all_required(request)
    bus_id = request.GET.get("bus_id","")

    try:
        business = Business.objects.get(pk=bus_id)
    except:
        business = None

    if request.method == "GET":
        '''根据机构ID获取信息'''
        if business:
            remark = "true"
            form = BusinessForm(instance=business)
            message = u"修改客户机构信息(*为必填项)"
        else:
            form = BusinessForm()
            form.fields['entry_person'].initial = request.user.first_name
            form.fields['register_date'].initial = time.strftime("%Y-%m-%d",time.localtime())
            message = u"新增客户机构(*为必填项)"
        return render_to_response("erp/business_add.html",locals(),context_instance=RequestContext(request))

    if request.method == "POST":
        if business:
            form = BusinessForm(request.POST or None, request.FILES,instance=business)
            if form.is_valid():
                form.save()
                business = form.instance
                user = business.user
                user.first_name = business.name #修改user的first_name
                user.save()
                messages.info(request,u"客户机构信息修改成功!")
                # set_picture_size(business.logo)
            else:
                messages.error(request,u"客户机构信息修改失败,请完善信息!")
                return render_to_response("erp/business_add.html",locals(),context_instance=RequestContext(request))
        else:
            password = request.POST.get("password","88888888")
            email = request.POST.get("email","")
            username = request.POST.get("phoneNum","")
            form = BusinessForm(request.POST or None, request.FILES)
            if form.is_valid():
                '''创建用户'''
                name = request.POST.get("name")
                last_name = u"客户机构"
                user = create_user(email,name,email,last_name,password)

                '''获取权限'''
                permissions = Permission.objects.filter(id__gt=40,content_type_id=2)

                '''添加权限 '''
                for permission in permissions:
                    user.user_permissions.add(permission)

                business = Business()
                business.user = user
                for k,v in form.cleaned_data.items():
                    setattr(business,k,v)
                business.save()
                # set_picture_size(business.logo)

                success = send_email(email,name,username,password)#向创建的客户机构发送邮件通知
                if not success:
                    url = "/erp/business_password_change/"+str(business.user.id)+"/?type=business_list&error=邮件发送失败,请重新发送"
                    return redirect(url)
                messages.info(request,u"新增客户机构成功!")
            else:
                messages.info(request,u"新增客户机构失败,请完善信息!")
                return render_to_response("erp/business_add.html",locals(),context_instance=RequestContext(request))
        return redirect("/erp/business_list/#business_list")

'''
客户机构列表
'''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def business_list(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    if not request.user.is_superuser:
        permissions = get_permissions(request)#获取权限列表
        return render_to_response("erp/no_permission.html",locals(),context_instance=RequestContext(request))
    permissions = get_permissions(request)#获取权限列表
    count = get_unread_examine(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    kwargs = {}
    if request.method == "POST":#搜索
        name = request.POST.get("bus_name","")
        business_num = request.POST.get("business_num","")
        phoneNum = request.POST.get("phoneNum","")
        address = request.POST.get("address","")
        kwargs["name__icontains"] = name
        kwargs["business_num__icontains"] = business_num
        kwargs["phoneNum__icontains"] = phoneNum
        kwargs["address__icontains"] = address

    bus_id = request.GET.get("bus_id","")
    '''删除客户机构'''
    if bus_id:
        business = Business.objects.get(pk=bus_id)#将该机构置为无效
        business.is_active = 0
        business.save()
        user = User.objects.get(pk=business.user.id)#将该用户置为无效
        user.is_active = 0
        user.save()
        messages.info(request,u"客户机构删除成功!")
        return redirect("/erp/business_list/#business_list")
    else:
        business = Business.objects.filter(is_active=1)
        business = business.filter(**kwargs)

        for busin in business:
            customer_sum = 0
            ''' 获取每个机构下面的员工 '''
            agents = Agent.objects.filter(business=busin.id,is_active=1)

            ''' 获取该机构下面的所有客户 '''
            for agent in agents:
                customers = agent.customer_set.filter(is_active=1)
                customer_sum += customers.count()

            ''' 获取该机构下面的所有产品 '''
            busin.products = busin.product_set.filter(is_active=1).count()

            busin.count = agents.count()
            busin.customer_sum = customer_sum

        permissions = get_permissions(request)#获取权限列表
        business,page_range,paginator = paginatorPage(request,business)
        return render_to_response("erp/business_list.html",locals(),context_instance=RequestContext(request))

''' 强制修改密码 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def business_password_change(request,user_id):
    type = request.GET.get("type")
    permissions = get_permissions(request)#获取权限列表
    lv_unread = Redister_Business.objects.filter(status=3).count()
    if type == "business_list" and not request.user.is_superuser:
        return render_to_response("erp/no_permission.html",locals(),context_instance=RequestContext(request))
    permissions = get_permissions(request)#获取权限列表
    count = get_unread_examine(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    business = get_business(request)
    user = User.objects.get(pk=user_id)
    # print user,user_id
    if type == "agent_list":
        ageId = []
        agent_id = user.agent.id
        agents = business.agent_set.filter(is_active=1)
        if not user.agent in business.agent_set.filter(is_active=1):
        # for age in agents:
        #     ageId.append(age.id)
        # if agent_id not in ageId:
            return render_to_response("erp/no_permission.html",locals(),context_instance=RequestContext(request))
    # type = request.GET.get("type")
    if request.method == "GET":
        message = u"修改密码"
        error = request.GET.get("error","")
        return render_to_response("erp/business_password_change.html",locals(),context_instance=RequestContext(request))
    else:
        password = request.POST.get("password")
        # print password
        # user = User.objects.get(pk=user_id)
        user.set_password(password)
        user.save()

        try:
            email_business = user.business   #判断是否是机构
        except:
            email_business = None

        # if user.last_name == u"客户机构":
        if email_business:
            success = send_email(user.email,user.first_name,user.username,password)#向创建的客户机构发送邮件通知
        else:
            code = business.business_num+str(user.agent.agent_num)
            success = send_email_emp(request,user.agent.email,business.name,request.user.first_name,user.agent.name,user.username,password,str(user.agent.qrcode),code)#向创建的用户发送邮件通知
                #                              邮件地址       发件机构名称        发件人              收件人名称         账号        密码         邀请码链接      邀请码
        if not success:
            error = u"邮件发送失败,请重新发送"
            url = request.get_full_path()+"&error="+error
            return redirect(url)
        messages.info(request,u"操作成功!")
        # load_process_message(request,{},{},u'\u4fee\u6539\u5bc6\u7801',user_id,business,)
        return redirect("/erp/"+type+"/#"+type)

''' 新增员工'''
from django.db.models import Max
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def agent_process(request):
    # business = get_business(request)
    # permissions = get_permissions(request)#获取权限列表
    # count = get_unread_examine(request)
    permissions,business,count,user_agents,total_unread = get_all_required(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()

    count = get_unread_examine(request)
    user_agents,total_unread = get_user_agents(request,business)

    ''' 获取员工ID '''
    agent_id = request.GET.get("agent_id","")
    try:
        agent = Agent.objects.get(pk=agent_id)
        old_agent = Agent.objects.get(pk=agent_id)
    except:
        agent = None
        old_agent = None

    if request.method == "GET":
        if request.user.is_superuser:
                return render_to_response("erp/no_permission.html",locals(),context_instance=RequestContext(request))
        ''' 修改员工信息 '''
        if agent:
            '''判断是否是本机构员工'''
            if not check_agent_modify(request,business,agent):
                return render_to_response("erp/no_permission.html",locals(),context_instance=RequestContext(request))
            '''-----------------------------------------------------------------'''
            form = AgentForm(instance=agent)
            form.fields['permissions'].queryset = Permission.objects.filter(id__gt=40,content_type_id=2)#过滤非自己定义的Permission
            message = u"修改员工信息(*为必填项)"
            remark = "true"
        else:
            ''' 新增员工 '''
            form = AgentForm()
            form.fields['entry_person'].initial = request.user.first_name
            form.fields['permissions'].queryset = Permission.objects.filter(id__gt=40,content_type_id=2)#过滤非自己定义的Permission
            form.fields['register_date'].initial = time.strftime("%Y-%m-%d",time.localtime())
            message = u"新增员工(*为必填项)"

        form.fields['position'].queryset = Position.objects.filter(business=business)
        return render_to_response("erp/agent_process.html",locals(),context_instance=RequestContext(request))

    if request.method == "POST":
        ''' 保存修改后的员工信息 '''
        storage_url = None
        if agent:
            form = AgentForm(request.POST or None, request.FILES,instance=agent)
            if form.is_valid():
                form.save()
                agent = form.instance
                agent_user = agent.user
                agent_user.first_name = agent.name
                agent_user.email = agent.email
                agent_user.save()

                if request.POST.get("avatar-w[]",""):
                    if request.POST.get("avatar-w[]") == "0":#判断是否上传了图片
                        storage_url = release_base_64(request,"avatar","pass")
                    if request.POST.get("avatar-w[]") != "0":#裁剪图片
                        storage_url = release_base_64(request,"avatar","ahead")
                    if storage_url:
                        agent.avatar = storage_url
                agent.save()
                # load_process_message(request,model_to_dict(old_agent),model_to_dict(agent),u'\u5458\u5de5\u4fe1\u606f\u4fee\u6539',agent.id,business,)
                messages.info(request,u"员工信息修改成功!")

            else:
                messages.error(request,u"员工信息修改失败,请完善信息!")
                form.fields['permissions'].queryset = Permission.objects.filter(id__gt=40,content_type_id=2)#过滤非自己定义的Permission
                return render_to_response("erp/agent_process.html",locals(),context_instance=RequestContext(request))
        else:
            ''' 保存新增员工 '''
            password = request.POST.get("password","88888888")
            email = request.POST.get("email","")
            form2 = AgentForm2(request.POST or None, request.FILES)
            form = AgentForm(request.POST or None, request.FILES)
            if form.is_valid() and form2.is_valid():
                name = request.POST.get("name")
                last_name = u"员工"

                agent = Agent()
                for k,v in form2.cleaned_data.items():
                    setattr(agent,k,v)

                agent.business = Business.objects.get(id=business.id)
                agent.save()

                agent_num = Agent.objects.filter(business=business).aggregate(Max('agent_num'))
                for k,v in form.cleaned_data.items():
                    setattr(agent,k,v)
                try:
                    agent.agent_num = int(agent_num['agent_num__max'])+1
                except:
                    agent.agent_num = 1
                agent.save()
                agent.create_qrcode(request)

                if request.POST.get("avatar-w[]",""):
                    if request.POST.get("avatar-w[]") == "0":#判断是否上传了图片图片
                        storage_url = release_base_64(request,"avatar","pass")
                    if request.POST.get("avatar-w[]") != "0":#裁剪图片
                        storage_url = release_base_64(request,"avatar","ahead")
                    if storage_url:
                        agent.avatar = storage_url
                        agent.save()
                code = business.business_num+str(agent.agent_num)
                user = create_user(code,name,email,last_name,password)#创建user
                agent.user = user
                agent.save()

                # load_process_message(request,{},model_to_dict(agent),u'\u65b0\u589e\u5458\u5de5',agent.id,business,)

                if not password:
                    password = "88888888"
                success = send_email_emp(request,agent.email,business.name,request.user.first_name,agent.name,code,password,str(agent.qrcode),code)#向创建的用户发送邮件通知
                                      # 邮件地址     发件机构名称        发件人           收件人名称         账号    密码     邀请码链接 邀请码
                if not success:
                    url = "/erp/business_password_change/"+str(agent.user.id)+"/?type=agent_list&error=邮件发送失败,请重新发送"
                    return redirect(url)
                messages.info(request,u"员工添加成功!")
            else:
                form.fields['entry_person'].initial = request.user.first_name
                form.fields['permissions'].queryset = Permission.objects.filter(id__gt=40,content_type_id=2)#过滤非自己定义的Permission
                form.fields['register_date'].initial = time.strftime("%Y-%m-%d",time.localtime())
                message = u"新增员工(*为必填项)"
                messages.error(request,u"员工添加失败,请完善信息!")
                return render_to_response("erp/agent_process.html",locals(),context_instance=RequestContext(request))
        return redirect("/erp/agent_list/#agent_list")

''' 员工列表'''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def agent_list(request):
    kwargs = {}
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    agent_id = request.GET.get("agent_id","")
    location = request.GET.get("location","")
    if location:
        messages.info(request,u"员工删除成功!")
        # load_process_message(request,{},{},u'\u5458\u5de5\u5220\u9664',agent_id,business,diffs_str=False)
    if agent_id:
        agent = Agent.objects.get(pk=agent_id)
        if not check_employee(request,agent,business):
            return redirect("/erp/no_permission/")
        agent.device_id = ''
        agent.save()
        messages.info(request,u"手机解除绑定成功!")
        # load_process_message(request,{},{},u'\u624b\u673a\u89e3\u9664\u7ed1\u5b9a',agent_id,business,diffs_str=False)
        return redirect("/erp/agent_list/#agent_list")

    if request.method == "POST":#搜索
        num = request.POST.get("num","")
        agent_name = request.POST.get("agent_name","")
        phoneNum = request.POST.get("phoneNum","")
        idNum = request.POST.get("idNum","")
        kwargs["agent_num__icontains"] = num
        kwargs["name__icontains"] = agent_name
        kwargs["phoneNum__icontains"] = phoneNum
        kwargs["idCard_num__icontains"] = idNum

    try:
        user_agent = request.user.agent
    except:
        user_agent = None
    if request.user.is_superuser:#超级管理员
        agents = Agent.objects.filter(is_active=1)
    # elif request.user.last_name == u"员工":
    elif user_agent:
        agent = Agent.objects.get(user_id=request.user.id)
        agents = Agent.objects.filter(is_active=1,business_id=agent.business_id)
    else:
        agents = Agent.objects.filter(is_active=1,business_id=request.user.business.id)

    agents = agents.filter(**kwargs)
    for age in agents:
        if request.user.is_superuser:
            age.b_a_num = age.business.business_num+str(age.agent_num)
        else:
            age.b_a_num = business.business_num+str(age.agent_num)
        age.count = age.customer_set.filter(is_active=1).count()
    agents,page_range,paginator = paginatorPage(request,agents)
    if request.user.is_superuser:

        return render_to_response("admin_erp/agent_list.html",locals(),context_instance=RequestContext(request))
    elif 'auth.employee_process' not in permissions:
        return render_to_response("erp/agent_lists.html",locals(),context_instance=RequestContext(request))
    return render_to_response("erp/agent_list.html",locals(),context_instance=RequestContext(request))

'''
所有列表的查看
'''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def check(request):
    id = request.GET.get("id")
    type = request.GET.get("type")
    check_remark = "true"
    business = get_business(request)
    permissions = get_permissions(request)#获取权限列表
    count = get_unread_examine(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    business = get_business(request)
    user_agents,total_unread = get_user_agents(request,business)
    ids = []
    if type == "product":#-----------------------
        if check_product(request,id,business):
            product = Product.objects.get(pk=id)
            form = ProductForm(instance=product)
            return render_to_response("erp/product.html",locals(),context_instance=RequestContext(request))
    elif type == "lv":#------------------------
        if request.user.is_superuser:
            lv = Lv_Announcement.objects.get(pk=id)
            form = Lv_announcement_Form(instance=lv)
            return render_to_response("erp/lv_announcement_process.html",locals(),context_instance=RequestContext(request))
    elif type == "agent" or type == "lvmeng_agent":#-----------------------
        agent = Agent.objects.get(pk=id)
        if check_agent(request,business,agent):
            customers = agent.customer_set.all()
            count = customers.count()
            form = AgentForm(instance=agent)
            form.fields['position'].queryset = Position.objects.filter(business=business)
            form.fields['permissions'].queryset = Permission.objects.filter(id__gt=40,content_type_id=2)
            return render_to_response("erp/agent_process.html",locals(),context_instance=RequestContext(request))
    elif type == "business":#------------------------
        if request.user.is_superuser:
            business = Business.objects.get(pk=id)
            # form = BusinessForm(instance=business)
            # return render_to_response("erp/business_add.html",locals(),context_instance=RequestContext(request))
            return render_to_response("admin_erp/business_base_info.html",locals(),context_instance=RequestContext(request))
    elif type == "customer" or type == "lvmeng_customer" or type == "admin_customer" or type == "agent_customer":#------------------------
        age_ids = []
        customer = Customer.objects.get(pk=id)

        if not check_customer(request,customer,business,permissions):
            return redirect("/erp/no_permission/")

        form = CustomerForm(instance=customer)
        agents = customer.agents.filter(is_active=1)
        if request.user.is_superuser:#admin查看所有
            form.fields['product_target'].queryset = Product.objects.filter(is_active=1)
        else:#只能查看自己机构的客户
            form.fields['product_target'].queryset = Product.objects.filter(business=business,is_active=1)
        return render_to_response("erp/customer_add.html",locals(),context_instance=RequestContext(request))

    elif type == "announcement":#公告对外----------------------------
        announcement = Announcement.objects.get(pk=id)
        if check_announcement_out(request,announcement,business):
            read_message(request,"announcement",id,business)#调用read_message,记录该用户已读
            form = PictureForm(instance=announcement)
            return render_to_response("erp/picture_logos.html",locals(),context_instance=RequestContext(request))

    elif type == "internal":#公告对内----------------------------------
        announcement = Internal_announcement.objects.get(pk=id)
        if check_internal_announcement(request,announcement,business):
            read_message(request,"internal_announcement",id,business)#调用read_message,记录该用户已读
            form = InternalForm(instance=announcement)
            return render_to_response("oa/announcement_add_modify.html",locals(),context_instance=RequestContext(request))

    elif type == "daily_work":#工作汇报-------------------------------
        announcement = Daily_work.objects.get(pk=id)
        if check_daily_work(request,announcement,business):
            form = DailyForm(instance=announcement)
            user_list = get_emp_self(request,business)
            form.fields['examine_user'].queryset = User.objects.filter(pk__in=user_list)
            return render_to_response("oa/daily_add_modify.html",locals(),context_instance=RequestContext(request))

    elif type == "check_cost":#-------------------------------------
        announcement = Cost_application.objects.get(pk=id)
        if check_cost_application(request,announcement,business):
            form = CostForm(instance=announcement)
            user_list = get_emp_self(request,business)
            form.fields['examine_user'].queryset = User.objects.filter(pk__in=user_list)
            return render_to_response("oa/cost_add_modify.html",locals(),context_instance=RequestContext(request))
    elif type == "check_leave":#-------------------请假-----------------
        announcement = Leave_management.objects.get(pk=id)
        if check_leave_application(request,announcement,business):
            form = LeaveForm(instance=announcement)
            user_list = get_emp_self(request,business)
            form.fields['examine_user'].queryset = User.objects.filter(pk__in=user_list)
            return render_to_response("oa/leave_add_modify.html",locals(),context_instance=RequestContext(request))
    elif type == "check_travel":#------------出差------------
        announcement = Travel_apply.objects.get(pk=id)
        if check_travel_apply(request,announcement,business):
            form = TravelForm(instance=announcement)
            user_list = get_emp_self(request,business)
            form.fields['examine_user'].queryset = User.objects.filter(pk__in=user_list)
            return render_to_response("oa/travel_add_modify.html",locals(),context_instance=RequestContext(request))
    elif type == "daily":#-------------------------
        announcement = Daily_to_do.objects.get(pk=id)
        if announcement.todo_user == request.user:
            form = DailyToDoForm(instance=announcement)
            return render_to_response("oa/daily_todo_add_modify.html",locals(),context_instance=RequestContext(request))
    elif type == "real_purchase" or type == "income_real_purchase":
        announcement = Real_purchase.objects.get(pk=id)
        if check_real_purchase(request,announcement,business):
            form = RealPurchaseForm(instance=announcement)
            form.fields['product'].queryset = Product.objects.filter(business=business)
            form.fields['customer'].queryset = Customer.objects.filter(pk=announcement.customer.id)
            return render_to_response("erp/agent_add_product.html",locals(),context_instance=RequestContext(request))
    elif type == "headline":
        if request.user.is_superuser:
            announcement = Headline.objects.get(pk=id)
            form = HeadlineForm(instance=announcement)
            return render_to_response("erp/headline_add_modify.html",locals(),context_instance=RequestContext(request))
    elif type == "position":
        announcement = Position.objects.get(pk=id)
        form = PositionForm(instance=announcement)
        form.fields['permissions'].queryset = Permission.objects.filter(id__gt=40,content_type_id=2)
        return render_to_response("erp/position_add_modify.html",locals(),context_instance=RequestContext(request))
    elif type == "redister":
        if not request.user.is_superuser:
            return redirect("/erp/no_permission/")
        announcement = Redister_Business.objects.get(pk=id)
        form = RedisterBusinessForm(instance=announcement)
        return render_to_response("erp/business_add.html",locals(),context_instance=RequestContext(request))

    return render_to_response("404.html",locals(),context_instance=RequestContext(request))

''' 客户操作 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def customer_list(request):
    count = get_unread_examine(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    current_business = get_business(request)
    business = get_business(request)
    user_agents,total_unread = get_user_agents(request,business)
    permissions = get_permissions(request)#获取权限列表
    customer_id = request.GET.get("customer_id","")
    if customer_id:#删除意向客户
        customer = Customer.objects.get(pk=customer_id)
        if delete_customer(request,customer):
            customer.is_active = 0
            customer.save()
            messages.info(request,u"意向客户删除成功!")
            # load_process_message(request,{},{},u'\u610f\u5411\u5ba2\u6237\u5220\u9664',customer_id,business,diffs_str=False)
            return redirect("/erp/customer_list/#customer_list")
        else:
            return redirect("/erp/no_permission/")

    customers = None
    kwargs = {}
    if request.method == "POST":
        customer_name = request.POST.get("customer_name","")
        phoneNum = request.POST.get("phoneNum","")
        idNum = request.POST.get("idNum","")
        kwargs["name__icontains"] = customer_name
        kwargs["phoneNum__icontains"] = phoneNum
        kwargs["idCard_num__icontains"] = idNum

    if request.GET.get("business_id"):#admin操作，获取该机构下面的所有客户
        business = Business.objects.get(pk=request.GET.get("business_id"))
        agents = business.agent_set.filter(is_active=1)
        customers = []
        for agent in agents:
            custs = agent.customer_set.filter(is_active=1)
            for cus in custs:
                customers.append(cus)
    try:
        user_agent = request.user.agent
    except:
        user_agent = None
    try:
        user_business = request.user.business
    except:
        user_business = None
    # if request.user.last_name == u"员工":
    if user_agent:
    # try:
        agent = Agent.objects.get(user_id=request.user.id)
        customers = agent.customer_set.filter(is_active=1).filter(**kwargs)
    # except:
    # if request.user.last_name == u"客户机构":
    if user_business:
        customers = []
        business = Business.objects.get(user_id=request.user.id)
        agents = business.agent_set.filter(is_active=1)
        for agent in agents:
            custs = agent.customer_set.filter(is_active=1).filter(**kwargs)
            for cus in custs:
                customers.append(cus)

    if request.user.is_superuser:
        if not request.GET.get("business_id"):
            customers = Customer.objects.filter(~Q(agents=None),is_active=1).filter(**kwargs)

    for customer in customers:
        sum = 0
        # purchases = customer.purchase_set.filter(product__business=current_business)#获取每个客户的所有购买量
        if request.user.is_superuser:
            purchases = customer.real_purchase_set.filter(is_active=1)#获取每个客户的所有购买量
        else:
            purchases = customer.real_purchase_set.filter(business=current_business,is_active=1)#获取每个客户的所有购买量
        for pur in purchases:
            sum += pur.amount
        customer.count = purchases.count()
        customer.sum = sum                   #购买总金额

        ''' 获取该客户属于哪位客户经理(非律锰) '''
        if not request.user.is_superuser:
            customer.customer_agent = customer.agents.filter(business=current_business,is_active=1)[0]

    customers,page_range,paginator = paginatorPage(request,customers)
    return render_to_response("erp/customer_list.html",locals(),context_instance=RequestContext(request))

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def customer_add(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    try:
        agent = request.user.agent
    except:
        return redirect("/erp/no_permission/")

    customer_id = request.GET.get("customer_id","")
    business = get_business(request)
    if request.user.is_superuser:#超级管理员
        products = Product.objects.filter(is_active=1)
    else:
        products = Product.objects.filter(is_active=1,business=business)

    if request.method == "GET":
        if customer_id:
            customer = Customer.objects.get(pk=customer_id)
            if delete_customer(request,customer):
                form = CustomerForm(instance=customer)

                # form.fields['product_target'].queryset = Product.objects.filter(business=business)
                form.fields['product_target'].queryset = products
                message = u"修改意向客户(*为必填项)"
            else:
                return redirect("/erp/no_permission/")
        else:
            form = CustomerForm()
            form.fields['product_target'].queryset = products

            message = u"新增意向客户(*为必填项)"
        return render_to_response("erp/customer_add.html",locals(),context_instance=RequestContext(request))

    storage_url = None
    if request.method == "POST":
        if customer_id:
            customer = Customer.objects.get(pk=customer_id)
            old_customer = model_to_dict(customer)
            form = CustomerForm(request.POST or None, request.FILES,instance=customer)
            if form.is_valid():
                form.save()
                if request.POST.get("portrait-w[]"):
                    if request.POST.get("portrait-w[]") == "0":#判断是否上传了图片图片
                            storage_url = release_base_64(request,"portrait","pass")
                    if request.POST.get("portrait-w[]") != "0":#裁剪图片
                        storage_url = release_base_64(request,"portrait","ahead")
                    if storage_url:
                        customer.portrait = storage_url
                        customer.save()
                messages.info(request,u"意向客户信息修改成功!")
                # load_process_message(request,old_customer,model_to_dict(customer),u'\u610f\u5411\u5ba2\u6237\u4fe1\u606f\u4fee\u6539',customer.id,business)

            else:
                messages.error(request,u"意向客户信息修改失败,请完善信息!")
                form.fields['product_target'].queryset = products
                return render_to_response("erp/customer_add.html",locals(),context_instance=RequestContext(request))
        else:
            form = CustomerForm(request.POST or None, request.FILES)
            if form.is_valid():
                form.save()
                customer = Customer()
                customer = form.instance
                if request.POST.get("portrait-w[]"):
                    if request.POST.get("portrait-w[]") == "0":#判断是否上传了图片图片
                            storage_url = release_base_64(request,"portrait","pass")
                    if request.POST.get("portrait-w[]") != "0":#裁剪图片
                        storage_url = release_base_64(request,"portrait","ahead")
                    if storage_url:
                        customer.portrait = storage_url
                        customer.save()
                messages.info(request,u"意向客户信息添加成功!")
                # load_process_message(request,{},model_to_dict(customer),u'\u610f\u5411\u5ba2\u6237\u6dfb\u52a0',customer.id,business)
            else:
                message = u"新增意向客户(*为必填项)"
                messages.error(request,u"意向客户信息添加失败,请完善信息!")
                return render_to_response("erp/customer_add.html",locals(),context_instance=RequestContext(request))

        customer = Customer()
        customer = form.instance
        customer.agents.add(request.user.agent)
        customer.save()

        return redirect("/erp/customer_list/#customer_list")

''' 客户登录页面轮播图 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def business_carousel_list_delete(request):#客户登录页面轮播图列表/删除
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    if request.user.is_superuser:
        carousels = business_carousel.objects.all()
    else:
        carousel_id = request.GET.get("carousel_id","")
        if carousel_id:
            carsId = []
            carousels = business.business_carousel_set.all()
            for car in carousels:
                carsId.append(car.id)
            if int(carousel_id) in carsId:
                business_carousel.objects.get(pk=carousel_id).delete()
                messages.info(request,u"机构轮播图删除成功!")
                # load_process_message(request,{},{},u'\u673a\u6784\u8f6e\u64ad\u56fe\u5220\u9664',carousel_id,business,diffs_str=False)
                return redirect("/erp/business_carousel_list_delete/#business_carousel_list_delete")
            else:
                return redirect("/erp/no_permission/")
        carousels = business.business_carousel_set.all()
    carousels,page_range,paginator = paginatorPage(request,carousels)
    return render_to_response("erp/business_carousel_list.html",locals(),context_instance=RequestContext(request))

''' 客户登录页面轮播图添加 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def business_carousel_add(request):#客户登录页面轮播图添加
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    if request.user.is_superuser:
        return redirect("/erp/no_permission/")
    if request.method == "GET":
        form = Business_Carousel_Form()
        return render_to_response("erp/business_carousel_process.html",locals(),context_instance=RequestContext(request))
    else:
        storage_url = None
        carousel = business_carousel()
        if request.POST.get("carousel-w[]",""):
            if request.POST.get("carousel-w[]") == "0":
                storage_url = release_base_64(request,"carousel","pass")
            elif request.POST.get("carousel-w[]") != "0":
                storage_url = release_base_64(request,"carousel","ahead")

        carousel.business = business
        carousel.add_user = request.user
        if storage_url:
            carousel.carousel = storage_url
        carousel.save()
        messages.info(request,u"机构轮播图添加成功!")
        # load_process_message(request,{},model_to_dict(carousel),u'\u673a\u6784\u8f6e\u64ad\u56fe\u6dfb\u52a0',carousel.id,business,)
        return redirect("/erp/business_carousel_list_delete/#business_carousel_list_delete")

@login_required
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def mail_list(request):#通讯录
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    kwargs = {}
    if request.method == "POST":#搜索
        agent_name = request.POST.get("agent_name","")
        phoneNum = request.POST.get("phoneNum","")
        kwargs["name__icontains"] = agent_name
        kwargs["phoneNum__icontains"] = phoneNum

    try:
        user_agent = request.user.agent
    except:
        user_agent = None

    if request.user.is_superuser:#超级管理员
       agents = Agent.objects.filter(is_active=1)
    # elif request.user.last_name == u"员工":
    elif user_agent:
        agent = Agent.objects.get(user_id=request.user.id)
        agents = Agent.objects.filter(is_active=1,business_id=agent.business_id)
    else:
        agents = Agent.objects.filter(is_active=1,business_id=request.user.business.id)

    agents = agents.filter(**kwargs)
    agents,page_range,paginator = paginatorPage(request,agents)
    return render_to_response("erp/mail_list.html",locals(),context_instance=RequestContext(request))

from django.db.models import Q
def online_chat(request):#从主页面进入聊天界面
    business = get_business(request)
    agents = business.agent_set.filter(~Q(user=request.user),is_active=1)
    id = request.GET.get("id","")
    talk_user = Agent.objects.get(pk=id)
    all_messages = get_message(request,request.user,talk_user.user,business)
    if talk_user not in agents:
        return redirect("/erp/no_permission/")
    return render_to_response("erp/online_chat.html",locals(),context_instance=RequestContext(request))

def chat_user_message(request):#获取聊天内容
    business = get_business(request)
    talk_user = Agent.objects.get(id=request.GET.get("talk_user"))
    all_messages = get_message(request,request.user,talk_user.user,business)
    return render_to_response("erp/online_chat_detail_2.html",locals(),context_instance=RequestContext(request))

def save_user_message(request):#保存聊天内容
    id = request.POST.get("talk_user","")
    talk_user = Agent.objects.get(id=id).user
    business = get_business(request)
    Online_chat.objects.create(
        sender = request.user,
        # recipient = Agent.objects.get(id=request.POST.get("talk_user")).user,
        recipient = talk_user,
        content = request.POST.get("content"),
        business = business
    )

    all_messages = get_message(request,request.user,talk_user,business)
    return render_to_response("erp/online_chat_detail.html",locals(),context_instance=RequestContext(request))

def get_message(request,sender,recipient,business):
    chats = Online_chat.objects.filter(Q(sender=sender,recipient=recipient,business=business)|Q(sender=recipient,recipient=sender,business=business))
    Online_chat.objects.filter(recipient=request.user,sender=recipient).update(read=True)
    return chats

#获取所有未读信息
def chat_logo_message_remind(request):

    permissions = get_permissions(request)
    business = get_business(request)
    count = get_unread_examine(request)
    user_agents,total_unread = get_user_agents(request,business)
    return render_to_response("erp/chat_logo_message_remind.html",locals(),context_instance=RequestContext(request))

#将每个人的信息控制在100条
def message_control(request):
    business = get_business(request)
    agents = business.agent_set.filter(~Q(user=request.user),is_active=1)
    for agent in agents:
        chats = Online_chat.objects.filter(Q(sender=request.user,recipient=agent.user,business=business)|Q(sender=agent.user,recipient=request.user,business=business))
        if chats.count() > 100:
            reverse_chats = chats.reverse()
            reverse_chats = reverse_chats[100:]
            for reverse_chat in reverse_chats:
                reverse_chat.delete()
    return JsonResponse({"result":"true"})



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

class business_redister(View):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    def get(self, request, *args, **kwargs):
        permissions = get_permissions(request)
        phoneNum = request.GET.get("phoneNum")
        if phoneNum:
            return render_to_response("erp/business_redister.html",locals(),context_instance=RequestContext(request))
        else:
            return redirect("/")

    def post(self, request, *args, **kwargs):
        permissions = get_permissions(request)
        kwarg = request.POST
        name = kwarg.get("name")
        email = kwarg.get("email")
        password = kwarg.get("password1")
        phoneNum = kwarg.get("phoneNum")
        verification_code = kwarg.get("verification_code")

        if User.objects.filter(username=email).count():#判断该邮箱是否已注册
            error = u"该邮箱已存在!"
            return render_to_response("erp/business_redister.html",locals(),context_instance=RequestContext(request))

        # 验证手机号和验证码是否相符
        codes = VerificationCode.objects.filter(phoneNum=phoneNum,purpose=0)
        if codes and codes[0].code == verification_code:
            user = User.objects.create_user(username=email,first_name=name,last_name=u"客户机构",email=email,password=password)#先将该用户设为无效
            user.is_active = 0
            user.save()
            #跳转到填写机构详情页面
            return business_redister_detail(request,name,email,phoneNum)
        else:
            error = u"验证码有误!"
            return render_to_response("erp/business_redister.html",locals(),context_instance=RequestContext(request))

def business_redister_detail(request,name,email,phone):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions = get_permissions(request)
    form = RedisterBusinessForm()
    # form.fields['register_date'].initial = time.strftime("%Y-%m-%d",time.localtime())
    form.fields['name'].initial = name
    form.fields['email'].initial = email
    form.fields['phoneNum'].initial = phone
    message = u"客户机构注册"
    return render_to_response("erp/business_redister_detail.html",locals(),context_instance=RequestContext(request))

def business_redister_save(request):
    email = request.POST.get('redister_email','')
    phoneNum = request.POST.get('redister_phoneNum','')
    permissions = get_permissions(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    form = RedisterBusinessForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save(commit=False)
        redister_business = Redister_Business()
        redister_business = form.instance
        redister_business.user = User.objects.get(username=email)
        redister_business.register_date = time.strftime("%Y-%m-%d",time.localtime())
        redister_business.save()
        messages.info(request,u"机构注册已提交,请留意邮箱信息!")
        # return redirect("/erp/business_redister/?phoneNum="+str(phoneNum))
        return render_to_response("erp/register_success.html",locals(),context_instance=RequestContext(request))
    messages.info(request,u"机构注册提交失败,请完善信息!")
    return render_to_response("erp/business_redister_detail.html",locals(),context_instance=RequestContext(request))

#客户注册
def person_redister(request):

    name = request.POST.get("person_name")
    phoneNum = request.POST.get("phoneNum2")
    password = request.POST.get("password3")
    person_email = request.POST.get("person_email")
    user = User.objects.create_user(username=phoneNum,password=password,first_name=name,last_name=u"客户",email=person_email)
    customer = Customer(user=user,name=name,phoneNum=phoneNum,email=person_email,customer_type=1)
    customer.save()
    send_email_to_redister_person(person_email,name,phoneNum,password)
    messages.info(request,u"您已注册成功,请下载app客户端登录使用!")
    # return redirect("/erp/business_redister/?phoneNum="+str(phoneNum))
    return render_to_response("erp/register_success.html",locals(),context_instance=RequestContext(request))


def business_redister_list(request):
    count = get_unread_examine(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions = get_permissions(request)#获取权限列表
    if not request.user.is_superuser:
        return redirect("/erp/no_permission/")

    if request.method == "POST":#搜索
        kwargs = {}
        name = request.POST.get("bus_name","")
        phoneNum = request.POST.get("phoneNum","")
        address = request.POST.get("address","")
        email = request.POST.get("email","")
        kwargs["email__icontains"] = email
        kwargs["name__icontains"] = name
        kwargs["phoneNum__icontains"] = phoneNum
        kwargs["address__icontains"] = address
        business = Redister_Business.objects.filter(**kwargs)
    else:
        business = Redister_Business.objects.all()
        business,page_range,paginator = paginatorPage(request,business)
    return render_to_response("admin_erp/business_redister_list.html",locals(),context_instance=RequestContext(request))

#注册审核
def business_redister_examine(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions = get_permissions(request)#获取权限列表
    if not request.user.is_superuser:
        return redirect("/erp/no_permission/")
    lv_unread = Redister_Business.objects.filter(status=3).count()
    cancel = request.GET.get("type","")#驳回申请
    if cancel:
        id = request.GET.get("id","")
        reject_reason = request.POST.get("reject_reason","")
        redisters = Redister_Business.objects.get(pk=id)
        redisters.status = 2
        redisters.save()
        user = redisters.user
        user.username = str(user.id)+"cancel@qq.com"#将username设为
        user.save()
        send_cancel_email(redisters.email,redisters.name,reject_reason)
        messages.info(request,u"客户机构注册申请已驳回!")
        return redirect("/erp/business_redister_list/#redister_business")

    if request.method == "GET":
        id = request.GET.get("id","")
        redisters = Redister_Business.objects.get(pk=id)
        obj = switch_data(request,redisters)
        form = Redister_Business_Save(instance=obj)
        return render_to_response("admin_erp/redister_business_add.html",locals(),context_instance=RequestContext(request))
    else:
        form = BusinessForm(request.POST or None, request.FILES)
        if form.is_valid():

            email = request.POST.get("email")
            user = User.objects.get(username=email)
            user.is_active=1
            user.save()#将该用户设为有效

            '''获取权限'''
            permissions = Permission.objects.filter(id__gt=40,content_type_id=2)

            '''添加权限 '''
            for permission in permissions:
                user.user_permissions.add(permission)

            business = Business()
            business.user = user
            for k,v in form.cleaned_data.items():
                setattr(business,k,v)
            business.save()

            redister_business = user.redister_business
            redister_business.status = 1
            redister_business.is_active = 1
            redister_business.save()#将该注册机构设为有效并通过审核

            password = u"您注册时的密码"

            success = send_email(email,business.name,business.email,u"您注册时的密码")#向创建的客户机构发送邮件通知
            if not success:
                url = "/erp/business_password_change/"+str(business.user.id)+"/?type=business_list&error=邮件发送失败,请重新发送"
                return redirect(url)
            messages.info(request,u"新增客户机构成功!")
        else:
            messages.info(request,u"新增客户机构失败,请完善信息!")
            return render_to_response("admin_erp/redister_business_add.html",locals(),context_instance=RequestContext(request))
        return redirect("/erp/business_list/#business_list")

def switch_data(request,obj):

    business = Business(
        user = obj.user,
        logo = obj.logo,
        business_qrcode = obj.business_qrcode,
        business_license_original = obj.business_license_original,
        business_license_copy = obj.business_license_copy,
        idCard_positive = obj.idCard_positive,
        idCard_negative = obj.idCard_negative,
        name = obj.name,
        phoneNum = obj.phoneNum,
        business_phone = obj.business_phone,
        email = obj.email,
        business_email = obj.business_email,
        address = obj.address,
        work_address = obj.work_address,
        register_date = obj.register_date,
        contact_name = obj.contact_name,
        contact_position = obj.contact_position,
        brief_introduction = obj.brief_introduction,
        note = obj.note,
        entry_person = request.user,

    )

    return business

def rejection_reason(request):

    id = request.GET.get("id")
    return render_to_response("admin_erp/rejection_reason.html",locals(),context_instance=RequestContext(request))

# def register_success(request):
#
#     return render_to_response("erp/register_success.html",locals(),context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def no_permission(request):
    permissions = get_permissions(request)
    business = get_business(request)
    count = get_unread_examine(request)
    return render_to_response("erp/no_permission.html",locals(),context_instance=RequestContext(request))

def page_not_found(request):
    if request.user.is_anonymous() or request.user.last_name == u"客户":
        return render_to_response("404_2.html",locals(),context_instance=RequestContext(request))
    else:
        permissions = get_permissions(request)
        return render_to_response("404.html",locals(),context_instance=RequestContext(request))

def page_error(request):
    if request.user.is_anonymous() or request.user.last_name == u"客户":
        return render_to_response("500_2.html",locals(),context_instance=RequestContext(request))
    else:
        permissions = get_permissions(request)
        return render_to_response("500_2.html",locals(),context_instance=RequestContext(request))



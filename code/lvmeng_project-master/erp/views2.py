#coding:utf-8
from django.contrib.auth.models import User, Group, Permission
from PIL import Image
import random
from erp.utils import *
from oa.views2 import get_unread_examine
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.paginator import Paginator,EmptyPage
from django.shortcuts import render,render_to_response,redirect
from models import *
from forms import *
from api.models import Headline
import time
import smtplib
from oa.models import Read_message
from django.contrib import auth
from django.contrib.auth import authenticate
from api.forms import HeadlineForm
from lvmeng.settings import MEDIA_ROOT
from api.views import check_CellNumber
from django.contrib import messages
from django.forms.models import model_to_dict
'''
删除员工进行客户分配
'''

def get_all_required(request):
    permissions = get_permissions(request)
    business = get_business(request)
    count = get_unread_examine(request)
    user_agents,total_unread = get_user_agents(request,business)
    return permissions,business,count,user_agents,total_unread

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def agent_customer_allot(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)


    if request.method == "GET":
        agent_list = []
        agent_id = request.GET.get("agent_id")
        current_agent = Agent.objects.get(pk=agent_id)#获取当前员工
        if not check_employee(request,current_agent,business):
            return redirect("/erp/no_permission/")
        customers = current_agent.customer_set.filter(is_active=1)#获取当前员工下面的所有客户
        agents = current_agent.business.agent_set.filter(is_active=1)#获取当前机构下面的所有员工

        ''' 获取每个客户购买产品的总金额 '''
        for cus in customers:
            sum = 0
            purchases = cus.real_purchase_set.all()
            for pur in purchases:
                sum += pur.amount
            cus.sum = sum

        for age in agents:#去掉当前员工
            if int(age.id) != int(agent_id):
                agent_list.append(age)

        return render_to_response("erp/agent_customer_allot.html",locals(),context_instance=RequestContext(request))

    if request.method == "POST":
        array = request.POST["array"].split(",")
        customer = None
        for val in array[0:-1]:
            if array.index(val) % 2 == 0:
                customer = Customer.objects.get(pk=val)
            else:
                agent = Agent.objects.get(pk=val)
                customer.agents.add(agent)
        remove_agent(request,array[-1],business)

        return JsonResponse({"da":"true"})

''' 删除员工 '''
def remove_agent(request,agent_id,business):
    agent = Agent.objects.get(pk=agent_id)
    User.objects.get(pk=agent.user.id).delete()#删除该理财师对应的User
    agent.is_active = 0#将该理财师设为无效
    agent.save()
    # load_process_message(request,{},{},u'\u5220\u9664\u7406\u8d22\u5e08',agent_id,business,diffs_str=False)
    customers = agent.customer_set.all()
    for customer in customers:
        customer.agents.remove(agent)

''' -----------------------------------超级管理员按角色查看------------------------------------------------ '''

''' 按员工 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def agent_role(request):
    if not request.user.is_superuser:
        return redirect("/erp/no_permission/")
    permissions = get_permissions(request)#获取权限列表
    count = get_unread_examine(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()

    kwargs = {}
    if request.method == "POST":#搜索
        num = request.POST.get("num","")
        agent_name = request.POST.get("agent_name","")
        phoneNum = request.POST.get("phoneNum","")
        idNum = request.POST.get("idNum","")
        kwargs["agent_num__icontains"] = num
        kwargs["name__icontains"] = agent_name
        kwargs["phoneNum__icontains"] = phoneNum
        kwargs["idCard_num__icontains"] = idNum

    if request.GET.get("id"):
        agents = Agent.objects.filter(business_id=request.GET.get("id"),is_active=1)
    else:
        agents = Agent.objects.filter(is_active=1)
    agents = agents.filter(**kwargs)
    for agent in agents:
        agent.b_a_num = agent.business.business_num+str(agent.agent_num)
        customers = agent.customer_set.filter(is_active=1)
        agent.count = customers.count()
    agents,page_range,paginator = paginatorPage(request,agents)
    return render_to_response("admin_erp/agent_list.html",locals(),context_instance=RequestContext(request))

''' 根据员工ID查看下面的客户 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def agent_customers(request):
    permissions,business,count,user_agents,total_unread = get_all_required(request)
    if request.user.last_name == u"客户":
        return redirect("/customer_login/")
    permissions = get_permissions(request)#获取权限列表
    count = get_unread_examine(request)
    business = get_business(request)
    id = request.GET.get("id")
    agent = Agent.objects.get(pk=id)
    lv_unread = Redister_Business.objects.filter(status=3).count()

    if not check_agent(request,business,agent):
        return redirect("/erp/no_permission/")
    customers = agent.customer_set.filter(is_active=1)#所有的客户

    for customer in customers:
        sum = 0
        purs = customer.real_purchase_set.all()#拿到该客户所有的购买
        customer.purchase = purs.count()
        for pur in purs:
            sum += pur.amount
        customer.sum = sum#购买总金额
    customers,page_range,paginator = paginatorPage(request,customers)
    if request.user.is_superuser:
        position_mark = "admin_agent_list"
    else:
        position_mark = "agent_list"
    return render_to_response("admin_erp/customer_list.html",locals(),context_instance=RequestContext(request))

''' 根据客户id获取该客户的所有购买 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def admin_purchase_list(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    id = request.GET.get("id")
    customer = Customer.objects.get(pk=id)
    # purchases = customer.real_purchase_set.filter(business=current_business)
    purchases = customer.real_purchase_set.all()
    return render_to_response("admin_erp/purchase_list.html",locals(),context_instance=RequestContext(request))

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def purchases_list(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    id = request.GET.get("id")
    customer = Customer.objects.get(pk=id)
    # purchases = customer.real_purchase_set.filter(business=current_business)
    purchases = customer.real_purchase_set.filter(is_active=1)
    purchases,page_range,paginator = paginatorPage(request,purchases)
    return render_to_response("erp/purchase_list.html",locals(),context_instance=RequestContext(request))

''' admin查看所有客户 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def admin_customers(request):
    if not request.user.is_superuser:
        return redirect("/erp/no_permission/")
    # permissions = get_permissions(request)#获取权限列表
    # count = get_unread_examine(request)
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    customers = Customer.objects.filter(~Q(agents=None),is_active=1)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    kwargs = {}
    if request.method == "POST":
        customer_name = request.POST.get("customer_name","")
        phoneNum = request.POST.get("phoneNum","")
        idNum = request.POST.get("idNum","")
        kwargs["name__icontains"] = customer_name
        kwargs["phoneNum__icontains"] = phoneNum
        kwargs["idCard_num__icontains"] = idNum
    customers = customers.filter(**kwargs)
    for customer in customers:
        sum = 0
        purchases = customer.real_purchase_set.all()#获取每个客户的所有购买量
        for pur in purchases:
            sum += pur.amount
        customer.count = purchases.count()
        customer.sum = sum                   #购买总金额
    customers,page_range,paginator = paginatorPage(request,customers)
    return render_to_response("admin_erp/admin_customer_list.html",locals(),context_instance=RequestContext(request))

def redister_customers(request):
    if not request.user.is_superuser:
        return redirect("/erp/no_permission/")
    permissions,business,count,user_agents,total_unread = get_all_required(request)
    lv_unread = Redister_Business.objects.filter(status=3).count()
    customers = Customer.objects.filter(is_active=1,customer_type=1,agents=None)
    kwargs = {}
    if request.method == "POST":
        customer_name = request.POST.get("customer_name","")
        phoneNum = request.POST.get("phoneNum","")
        kwargs["name__icontains"] = customer_name
        kwargs["phoneNum__icontains"] = phoneNum
    customers = customers.filter(**kwargs)
    customers,page_range,paginator = paginatorPage(request,customers)
    return render_to_response("admin_erp/redister_customer_list.html",locals(),context_instance=RequestContext(request))


''' admin查看所有员工
@login_required
def admin_employee_list(request):
    fob_customer(request)
    kwargs = {}
    count = get_unread_examine(request)
    if request.method == "POST":#搜索
        emp_name = request.POST.get("emp_name","")
        phoneNum = request.POST.get("phoneNum","")
        idNum = request.POST.get("idNum","")
        kwargs["name__icontains"] = emp_name
        kwargs["phoneNum__icontains"] = phoneNum
        kwargs["idCard_num__icontains"] = idNum

    permissions = get_permissions(request)#获取权限列表
    employees = Employee.objects.filter(~Q(business=None)& Q(is_active=1)).order_by("business_id")
    employees = employees.filter(**kwargs)

    return render_to_response("admin_erp/employee_list.html",locals(),context_instance=RequestContext(request))
 '''
''' -----------------------------------超级管理员按角色查看END------------------------------------------------ '''

''' 统一权限管理 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def get_permissions(request):
    permissions = []
    user_agent = None
    try:
        user_agent = request.user.agent
    except:
        pass
    if user_agent:
        for permission in request.user.agent.permissions.all():
            permissions.append('auth.'+permission.codename)
    else:
        for permission in request.user.get_all_permissions():
            permissions.append(permission)

    return permissions

''' 发送email到机构 '''
def send_email(email,name,user_name,pass_word):
    if not pass_word:
        pass_word = "88888888"
    data = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    message =(u'上海律锰信息技术有限公司，在%s时已为贵公司/机构[%s]创建/修改了账号。机构账号：%s，密码：%s,请登录查看。<br/>\
            登录网站:http://niujidui.com/login/<br/>\
            牛基队官网：http://niujidui.com/\
            '%(data,name,email,pass_word)).encode('utf8')
    # username = 'shexiaolong@niujidui.com'
    # password = '920403Love'
    # smtp = smtplib.SMTP()
    # smtp.connect('smtp.niujidui.com')
    # smtp.login(username, password)
    # smtp.sendmail(
    #     "shexiaolong@niujidui.com",
    #     [email],
    #     message
    # )

    # host = 'smtp.qq.com'
    # port = 587
    sender = 'niujidui@niujidui.com'
    # pwd = 'swhicietamlddaae'
    receivers = [email]

    msg = MIMEText(message, 'html')
    msg['subject'] = "牛基队邀请您加入"
    msg['from'] = sender
    msg['to'] = ", ".join(receivers)

    try:
        smtpserver = smtplib.SMTP(MAIL_HOST)
        # smtpserver.ehlo()
        # smtpserver.starttls()
        # smtpserver.ehlo()
        # smtpserver.login(sender,pwd)

        smtpserver.sendmail(sender, receivers, msg.as_string())
        smtpserver.close()
        return 1
    except:
        return 0

''' 发送email到机构 '''
def send_cancel_email(email,name,reason):

    data = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    message =(u'上海律锰信息技术有限公司，在%s时驳回了贵公司/机构[%s]的机构注册申请。<br/>\
                驳回原因:%s<br/>\
                您也可以登录下面网站重新注册,<br/>\
                登录网站:http://niujidui.com/login/<br/>\
                牛基队官网：http://niujidui.com/\
            '%(data,name,reason)).encode('utf8')

    sender = 'niujidui@niujidui.com'
    receivers = [email]

    msg = MIMEText(message, 'html')
    msg['subject'] = "牛基队机构注册审批"
    msg['from'] = sender
    msg['to'] = ", ".join(receivers)

    try:
        smtpserver = smtplib.SMTP(MAIL_HOST)
        smtpserver.sendmail(sender, receivers, msg.as_string())
        smtpserver.close()

    except:
        pass

''' 发送email到个人注册 '''
def send_email_to_redister_person(email,name,phoneNum,password):

    data = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    message =(u'恭喜您[%s]先生/女士在%s,在牛基队的个人注册申请已通过，账号:%s，密码：%s。<br/>\
                牛基队官网下载APP：http://niujidui.com/\
            '%(name,data,phoneNum,password)).encode('utf8')

    sender = 'niujidui@niujidui.com'
    receivers = [email]

    msg = MIMEText(message, 'html')
    msg['subject'] = "牛基队个人注册"
    msg['from'] = sender
    msg['to'] = ", ".join(receivers)

    try:
        smtpserver = smtplib.SMTP(MAIL_HOST)
        smtpserver.sendmail(sender, receivers, msg.as_string())
        smtpserver.close()

    except:
        pass


''' 发送email到员工 '''
from lvmeng.settings import BASE_DIR
from email.mime.text import MIMEText
def send_email_emp(request,email,business,sender,name,user_name,pass_word,qrcode,code):
    data = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

    file = "http://" + request.META['HTTP_HOST'] + "/static/img/qrcode.jpg"
    qr_url = "http://" + request.META['HTTP_HOST'] +"/media/"+qrcode

    message = (u'创建人：%s,机构：%s，在%s时已为您[%s]创建/修改了账号。个人登录账号：%s，密码：%s,请登录查看。<br/>\
    登录网站:http://niujidui.com/login/<br/>\
    牛基队官网：http://niujidui.com/<br/>\
    客户经理app下载二维码:%s<br/>\
    客户邀请码链接二维码：%s<br/>\
    客户邀请码：%s'%(business,sender,data,name,user_name,pass_word,file,qr_url,code)).encode('utf8')
    # host = 'smtp.qq.com'
    # port = 587
    sender = 'niujidui@niujidui.com'
    # pwd = 'swhicietamlddaae'
    receivers = [email]

    msg = MIMEText(message, 'html')
    msg['subject'] = "牛基队企业员工注册"
    msg['from'] = sender
    msg['to'] = ", ".join(receivers)

    try:
        smtpserver = smtplib.SMTP(MAIL_HOST)
        # smtpserver.ehlo()
        # smtpserver.starttls()
        # smtpserver.ehlo()
        # smtpserver.login(sender,pwd)

        smtpserver.sendmail(sender, receivers, msg.as_string())
        smtpserver.close()
        return 1
    except:
        return None



''' 添加/修改机构公告信息 '''
import base64
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def business_logos(request):
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    form = PictureForm()
    announce_id = request.GET.get("announce_id","")
    if request.user.is_superuser:
        return redirect("/erp/no_permission/")
    try:
        announcement = Announcement.objects.get(pk=announce_id)#获取修改的机构公告信息 add_business_announcement
        old_announcement = model_to_dict(announcement)
        if not check_announcement_out(request,announcement,business):
            return redirect("/erp/no_permission/")
    except:
        announcement = None
        old_announcement = None
    if announce_id and request.method == "GET":
        form = PictureForm(instance = announcement)
        message = u"修改机构公告信息(*为必填项)"
        return render_to_response("erp/picture_logos.html",locals(),context_instance=RequestContext(request))

    if request.method == "GET":
        message = u"添加机构公告信息(*为必填项)"
        form.fields['date'].initial = time.strftime("%Y-%m-%d",time.localtime())
        return render_to_response("erp/picture_logos.html",locals(),context_instance=RequestContext(request))

    if request.method == "POST":
        storage_url = None
        if announce_id:
            form = PictureForm(request.POST or None, request.FILES,instance=announcement)
            if form.is_valid():
                form.save()
                if request.POST.get("picture-w[]",""):
                    if request.POST.get("picture-w[]") == "0":
                        storage_url = release_base_64(request,"picture","pass")
                    elif request.POST.get("picture-w[]") != "0":
                        storage_url = release_base_64(request,"picture","ahead")

                    if storage_url:
                        announcement.picture = storage_url
                        announcement.save()
                # load_process_message(request,old_announcement,model_to_dict(announcement),u'\u673a\u6784\u516c\u544a\u4fee\u6539(\u9762\u5411\u5ba2\u6237)',announce_id,business)
                messages.info(request,u'机构公告修改成功!')
                # if announcement.picture:
                #     set_picture_size(announcement.picture)
            else:
                messages.error(request,u'机构公告修改失败,请完善信息！')
                return render_to_response("erp/picture_logos.html",locals(),context_instance=RequestContext(request))
        else:

            form = PictureForm(request.POST or None, request.FILES)
            if form.is_valid():
                form.save()
                announcement = form.instance
                if request.POST.get("picture-w[]",""):
                    if request.POST.get("picture-w[]") == "0":
                        storage_url = release_base_64(request,"picture","pass")
                    elif request.POST.get("picture-w[]") != "0":
                        storage_url = release_base_64(request,"picture","ahead")

                announcement.announce_business = Business.objects.get(id=business.id)
                if storage_url:
                    announcement.picture =  storage_url
                announcement.save()
                # load_process_message(request,{},model_to_dict(announcement),u'\u673a\u6784\u516c\u544a\u6dfb\u52a0(\u9762\u5411\u5ba2\u6237)',announce_id,business)
                messages.info(request,u'机构公告添加成功')

            else:
                messages.error(request,u'机构公告添加失败,请完善信息！')
                return render_to_response("erp/picture_logos.html",locals(),context_instance=RequestContext(request))

        return redirect("/erp/business_announcement_list/")

#-------------------------------------------------------------------------------------------

def release_base_64(request,pic_id_name,mark):

    leniystr =  request.POST.get("base_1").split(",")[1]+request.POST.get("base_2")+request.POST.get("base_3")+request.POST.get("base_4")+request.POST.get("base_5")+request.POST.get("base_6")+request.POST.get("base_7")+request.POST.get("base_8")\
                +request.POST.get("base_9")+request.POST.get("base_10")+request.POST.get("base_11")+request.POST.get("base_12")+request.POST.get("base_13")+request.POST.get("base_14")+request.POST.get("base_15")
    box = None
    if mark != "pass":
        box_x = int(request.POST.get(pic_id_name+"-x[]").split(".")[0])
        box_y = int(request.POST.get(pic_id_name+"-y[]").split(".")[0])
        box_w = int(request.POST.get(pic_id_name+"-w[]").split(".")[0])
        box_h = int(request.POST.get(pic_id_name+"-h[]").split(".")[0])
        # box变量是一个四元组(左，上，右，下)
        box = (box_x,box_y,box_w+box_x,box_h+box_y)

    imgData = base64.b64decode(leniystr)
    ''' 生成图片名并用base64加密 '''
    num_str = range(1000)
    eng_str = range(26)
    pic_str = base64.b64encode(str(random.sample(num_str,10))+chr(random.choice(eng_str))+str(random.choice(eng_str))+chr(random.choice(eng_str)))
    if pic_id_name == "avatar":
        storage_url = "agent/avatar/"+pic_str+".jpg"
    elif pic_id_name == "logo":
        storage_url = "business/logo/"+pic_str+".jpg"
    elif pic_id_name == "lv_picture":
        storage_url = "lvmeng/announcement/"+pic_str+".jpg"
    elif pic_id_name == "portrait":
        storage_url = "customer/avatar/"+pic_str+".jpg"
    elif pic_id_name == "carousel":
        storage_url = "business/carousel/"+pic_str+".jpg"
    else:
        storage_url = "business/pictures/"+pic_str+".jpg"
    pic_url = MEDIA_ROOT+storage_url
    leniyimg = open(pic_url,'wb')
    leniyimg.write(imgData)
    leniyimg.close()
    # return storage_url,box
    if mark != "pass":
        return cut_picture(storage_url,box)
    else:
        return storage_url

def release_qrcode_64(request,pic_id_name,mark):

    leniystr =  request.POST.get("qrcode_1").split(",")[1]+request.POST.get("qrcode_2")+request.POST.get("qrcode_3")+request.POST.get("qrcode_4")+request.POST.get("qrcode_5")+request.POST.get("qrcode_6")+request.POST.get("qrcode_7")+request.POST.get("qrcode_8")\
                +request.POST.get("qrcode_9")+request.POST.get("qrcode_10")+request.POST.get("qrcode_11")+request.POST.get("qrcode_12")+request.POST.get("qrcode_13")+request.POST.get("qrcode_14")+request.POST.get("qrcode_15")
    box = None
    if mark != "pass":
        box_x = int(request.POST.get(pic_id_name+"-x[]").split(".")[0])
        box_y = int(request.POST.get(pic_id_name+"-y[]").split(".")[0])
        box_w = int(request.POST.get(pic_id_name+"-w[]").split(".")[0])
        box_h = int(request.POST.get(pic_id_name+"-h[]").split(".")[0])
        # box变量是一个四元组(左，上，右，下)
        box = (box_x,box_y,box_w+box_x,box_h+box_y)

    imgData = base64.b64decode(leniystr)
    ''' 生成图片名并用base64加密 '''
    num_str = range(1000)
    eng_str = range(26)
    pic_str = base64.b64encode(str(random.sample(num_str,10))+chr(random.choice(eng_str))+str(random.choice(eng_str))+chr(random.choice(eng_str)))
    business_qrcode = "business/qrcode/"+pic_str+".jpg"
    pic_url = MEDIA_ROOT+business_qrcode
    leniyimg = open(pic_url,'wb')
    leniyimg.write(imgData)
    leniyimg.close()
    # return storage_url,box
    if mark != "pass":
        return cut_picture(business_qrcode,box)
    else:
        return business_qrcode


def cut_picture(url,box):
    image_url = MEDIA_ROOT+url
    images = Image.open(image_url)
    # xsize,ysize=images.size#获取原图的尺寸
    region = images.crop(box)
    region.save(image_url)
    return url

#-------------------------------------------------------------------------------------------

''' 查看机构公告列表 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def business_announcement_list(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    announce_id = request.GET.get("announce_id","")
    if announce_id:
        announcement = Announcement.objects.get(pk=announce_id)#删除机构公告信息
        if not check_announcement_out(request,announcement,business):
            return redirect("/erp/no_permission/")
        announcement.is_active = 0
        announcement.save()
        messages.info(request,u"机构公告删除成功!")
        # load_process_message(request,{},{},u'\u673a\u6784\u516c\u544a\u5220\u9664(\u9762\u5411\u5ba2\u6237)',announce_id,business,diffs_str=False)
        return redirect("/erp/business_announcement_list/#business_announcement_list")

    read = []
    read_messages = Read_message.objects.filter(read_business=business,read_user=request.user,model_name="announcement")
    for read_message in read_messages:#获取已读的该模块里面当前user所读的条目
        read.append(read_message.record_id)

    announcements = None
    if request.user.is_superuser:#超级管理员
        announcements = Announcement.objects.filter(is_active=1)
        announcements,page_range,paginator = paginatorPage(request,announcements)
        return render_to_response("erp/announcement_list.html",locals(),context_instance=RequestContext(request))

    try:
        user_agent = request.user.agent
    except:
        user_agent = None
    # if request.user.last_name == u"员工":
    if user_agent:
        agent = Agent.objects.get(user_id=request.user.id)
        business = Business.objects.get(id=agent.business.id)
    else:
        business = Business.objects.get(user_id=request.user.id)

    announcements = Announcement.objects.filter(announce_business = business,is_active=1)
    # user_agents = business.agent_set.filter(~Q(user=request.user),is_active=1)
    announcements,page_range,paginator = paginatorPage(request,announcements)
    return render_to_response("erp/announcement_list.html",locals(),context_instance=RequestContext(request))

''' 机构登录 '''
def account_login(request):

    if request.method == "GET":
        if request.user.is_authenticated():
            if request.user.last_name == u"客户":
                return render_to_response("erp/login.html",locals(),context_instance=RequestContext(request))
            return redirect('/erp/business_announcement_list/#business_announcement_list')
        return render_to_response("erp/login.html",locals(),context_instance=RequestContext(request))
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username and password:
            userLogin = None
            if User.objects.filter(username=username).count():
                userLogin = authenticate(username=username,password=password)
            elif User.objects.filter(first_name=username).count():
                user = User.objects.get(first_name=username)

                try:
                    user_business = user.business   #判断是否是机构
                except:
                    user_business = None
                # if user.last_name == u"客户机构":
                if user_business:
                    userLogin = authenticate(username=user.username,password=password)
                else:
                    error = u'!对不起,用户或密码不正确'
                    return render_to_response('erp/login.html',locals(),context_instance=RequestContext(request))

            if userLogin:
                auth.login(request,userLogin)
            else:
                error = u'!对不起,用户或密码不正确'
                return render_to_response('erp/login.html',locals(),context_instance=RequestContext(request))
        else:
            error = u'!对不起,用户或密码不能为空'
            return render_to_response('erp/login.html',locals(),context_instance=RequestContext(request))

        if userLogin.last_name == u"客户":
            auth.logout(request)
            error = u'!对不起,用户或密码不正确'
            return render_to_response('erp/login.html',locals(),context_instance=RequestContext(request))

        return redirect('/erp/business_announcement_list/#business_announcement_list')



from web_customer.views import belong_business_customer
''' 用户选择机构显示相对应的信息 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def customer_business_search(request):
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    bus_id = None
    lv_unread = Redister_Business.objects.filter(status=3).count()
    bus_id = request.GET.get("bus_id","")
    if not bus_id:
        return redirect("/customer_login/")
    elif not belong_business_customer(request,bus_id):
        return render_to_response("404_2.html",locals(),context_instance=RequestContext(request))
    business = Business.objects.get(pk=bus_id)
    products = business.product_set.filter(is_active=1)[:5]
    agents = request.user.customer.agents.all()
    active = 100
    for pro in products:
        pro.return_expected = str(pro.return_expected*100).split(".")[0]
    success = "true"
    headlines = Headline.objects.all()[:6]
    announcements = Announcement.objects.filter(announce_business=business,is_active=1)[:8]
    return render_to_response('web_customer/customer_new/index_2.html',locals(),context_instance=RequestContext(request))

''' 根据产品类型查看当前机构的产品信息 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def show_product_by_type(request):
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    bus_id = request.GET.get("bus_id","")
    product_type = request.GET.get("product_type","")
    lv_unread = Redister_Business.objects.filter(status=3).count()
    if not bus_id:
        return redirect("/customer_login/")
    elif not belong_business_customer(request,bus_id):
        return render_to_response("404_2.html",locals(),context_instance=RequestContext(request))
    business = Business.objects.get(pk=bus_id)
    if  int(product_type) == 100:
        products = business.product_set.filter(is_active=1)[:5]
    else:
        products = business.product_set.filter(product_type_id=product_type,is_active=1)[:5]
    agents = request.user.customer.agents.all()
    active = int(product_type)
    headlines = Headline.objects.all()[:6]
    announcements = Announcement.objects.filter(announce_business=business,is_active=1)[:8]
    for pro in products:
        pro.return_expected = str(pro.return_expected*100).split(".")[0]
    success = "true"
    return render_to_response('web_customer/customer_new/index_2.html',locals(),context_instance=RequestContext(request))

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

''' 员工添加客户所购买的产品信息 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def agent_add_product(request):
    # permissions = get_permissions(request)
    # count = get_unread_examine(request)
    # business = get_business(request)
    # user_agents,total_unread = get_user_agents(request,business)
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    id = request.GET.get("customer_id","")
    if request.method == "GET":
        if id:
            form = PurchaseForm()
            customer = Customer.objects.filter(pk=id)
            if real_purchase_precess(request,customer[0]):
                # form.fields['customer'].queryset = customer
                pass
            else:
                return redirect("/erp/no_permission/")
        else:
            try:
                agent = request.user.agent
                form = RealPurchaseForm()
                form.fields['customer'].queryset = agent.customer_set.filter(is_active=1)
            except:
                return redirect("/erp/no_permission/")
        message = u"添加用户购买(*为必填项)"
        form.fields['product'].queryset = Product.objects.filter(business=business)
        return render_to_response("erp/agent_add_product.html",locals(),context_instance=RequestContext(request))

    if request.method == "POST":
        if id:
            form = PurchaseForm(request.POST)
            if form.is_valid():
                real_purchase = Real_purchase()
                real_purchase = form.instance
                real_purchase.business = business
                real_purchase.customer = Customer.objects.get(pk=id)
                real_purchase.real_agent = Agent.objects.get(user=request.user)
                real_purchase.save()
                messages.info(request,u"客户购买添加成功!")
                # load_process_message(request,{},model_to_dict(real_purchase),u'\u5ba2\u6237\u8d2d\u4e70\u6dfb\u52a0',real_purchase.id,business,)
            else:
                messages.error(request,u"客户购买添加失败,请完善信息!")
                return render_to_response("erp/agent_add_product.html",locals(),context_instance=RequestContext(request))
        else:
            form = RealPurchaseForm(request.POST)
            if form.is_valid():
                real_purchase = Real_purchase()
                real_purchase = form.instance
                real_purchase.business = business
                real_purchase.real_agent = Agent.objects.get(user=request.user)
                real_purchase.save()
                messages.info(request,u"客户购买添加成功!")
                # load_process_message(request,{},model_to_dict(real_purchase),u'\u5ba2\u6237\u8d2d\u4e70\u6dfb\u52a0',real_purchase.id,business,)
            else:
                messages.error(request,u"客户购买添加失败,请完善信息!")
                return render_to_response("erp/agent_add_product.html",locals(),context_instance=RequestContext(request))

        return redirect("/erp/agent_product_list/")

'''员工添加客户所购买的产品信息的列表 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def agent_product_list(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    kwargs = {}
    if request.method == "POST":#搜索
        customer_num = request.POST.get("customer_num","")
        product_name = request.POST.get("product_name","")
        kwargs["customer__name__icontains"] = customer_num
        kwargs["product__name__icontains"] = product_name

    # purchases = Real_purchase.objects.filter(business=business,real_agent=request.user.agent,customer__is_active=1,**kwargs)
    purchases = real_purchase_list(request,business)
    # real_purchases = purchases.filter(**kwargs)
    real_purchases,page_range,paginator = paginatorPage(request,purchases.filter(**kwargs))
    return render_to_response("erp/agent_product_list.html",locals(),context_instance=RequestContext(request))

@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def income_inquiry(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    kwargs = {}
    if request.method == "POST":#搜索
        customer_num = request.POST.get("customer_num","")
        product_name = request.POST.get("product_name","")
        start = request.POST.get("start","")
        product_start = request.POST.get("product_start","")
        end = request.POST.get("end","")
        product_end = request.POST.get("product_end","")
        kwargs["customer__name__icontains"] = customer_num
        kwargs["product__name__icontains"] = product_name
        if start and end:
            kwargs["income_date__gte"] = start
            kwargs["income_date__lte"] = end
        elif start:
            kwargs["income_date__gte"] = start
        elif end:
            kwargs["income_date__lte"] = end

        if product_start and product_end:
            kwargs["end_date__gte"] = product_start
            kwargs["end_date__lte"] = product_end
        elif product_start:
            kwargs["end_date__gte"] = product_start
        elif product_end:
            kwargs["end_date__lte"] = product_end

    if request.user.is_superuser:
        real_purchases = Real_purchase.objects.filter(**kwargs)
        lv_unread = Redister_Business.objects.filter(is_active=0).count()
    else:
        real_purchases = Real_purchase.objects.filter(business=business,**kwargs)

    per_sum = 0
    for real in real_purchases:
        per_sum += real.amount

    real_purchases,page_range,paginator = paginatorPage(request,real_purchases)
    return render_to_response("erp/income_inquiry.html",locals(),context_instance=RequestContext(request))

''' 金融头条列表/删除 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def financial_headlines(request):
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    if not request.user.is_superuser:
        return redirect("/erp/no_permission/")
    headline_id = request.GET.get("headline_id","")
    count = get_unread_examine(request)
    if headline_id:
        Headline.objects.get(pk=headline_id).delete()
        messages.info(request,u"金融头条删除成功!")
        return redirect("/erp/financial_headlines/#financial_headlines")

    permissions = get_permissions(request)
    message = u"金融头条列表"
    headlines = Headline.objects.all()
    lv_unread = Redister_Business.objects.filter(is_active=0).count()
    headlines,page_range,paginator = paginatorPage(request,headlines)
    # if headline_id:
    #     return redirect("/erp/financial_headlines#financial_headlines")
    return render_to_response("erp/headline_list.html",locals(),context_instance=RequestContext(request))

''' 新增/修改金融头条 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def headline_add_modify(request):
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    if not request.user.is_superuser:
        return redirect("/erp/no_permission/")
    permissions = get_permissions(request)
    count = get_unread_examine(request)
    headline_id = request.GET.get("headline_id","")
    lv_unread = Redister_Business.objects.filter(is_active=0).count()
    try:
        headline = Headline.objects.get(pk=headline_id)
    except:
        headline = None

    if request.method == "GET":
        if headline_id:
            form = HeadlineForm(instance=headline)
            message = u"修改金融头条"
        else:
            form = HeadlineForm()
            message = u"添加金融头条"
        return render_to_response("erp/headline_add_modify.html",locals(),context_instance=RequestContext(request))

    if request.method == "POST":
        if headline:
            form = HeadlineForm(request.POST or None, request.FILES,instance=headline)
            if form.is_valid() and form.has_changed():
                form.save()
                headline = form.instance
                set_picture_size(headline.picture)
                messages.info(request,u"金融头条修改成功!")
            else:
                messages.error(request,u"金融头条修改失败,请完善信息!")
                return render_to_response("erp/headline_add_modify.html",locals(),context_instance=RequestContext(request))
        else:
            form = HeadlineForm(request.POST or None, request.FILES)
            if form.is_valid():
                form.save()
                current = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                headline = form.instance
                headline.register_date = current
                headline.save()
                set_picture_size(headline.picture)
                messages.info(request,u"金融头条新增成功!")
            else:
                messages.error(request,u"金融头条新增失败,请完善信息!!")
                return render_to_response("erp/headline_add_modify.html",locals(),context_instance=RequestContext(request))

    return redirect("/erp/financial_headlines/#financial_headlines")

''' 显示机构基本信息 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def show_business_base_info(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    form = BusinessForm(instance=business)
    return render_to_response("erp/business_base_info.html",locals(),context_instance=RequestContext(request))


''' 修改机构基本信息 '''
@login_required(login_url='login/')
@user_passes_test(lambda u: u.last_name !=u"客户", login_url='login/')
def modify_business_base_info(request):
    lv_unread = Redister_Business.objects.filter(status=3).count()
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    if request.user.is_superuser:
        return redirect("/erp/no_permission/")
    business_id = business.id
    if request.method == "GET":
        message = u'修改机构基本信息'
        form = BusinessModifyForm(instance=business)
        return render_to_response("erp/modify_business_base_info.html",locals(),context_instance=RequestContext(request))
    else:
        old_business = get_business(request)
        user = User.objects.get(username=business.email)
        storage_url = None
        business_qrcode = None
        form = BusinessModifyForm(request.POST or None, request.FILES,instance=business)
        if form.is_valid():
            form.save()

            if request.POST.get("logo-w[]",""):
                if request.POST.get("logo-w[]") == "0":#判断是否上传了图片
                    storage_url = release_base_64(request,"logo","pass")
                elif request.POST.get("logo-w[]") != "0":
                    storage_url = release_base_64(request,"logo","ahead")#调用方法裁剪图片
                    business = Business()
                    business = form.instance
                if storage_url:
                    business.logo = storage_url
                    business.save()

            if request.POST.get("business_qrcode-w[]",""):
                if request.POST.get("business_qrcode-w[]") == "0":#判断是否上传了图片
                    storage_url = release_qrcode_64(request,"business_qrcode","pass")
                elif request.POST.get("business_qrcode-w[]") != "0":
                    business_qrcode = release_qrcode_64(request,"business_qrcode","ahead")#调用方法裁剪图片
                    business = Business()
                    business = form.instance
                if business_qrcode:
                    business.business_qrcode = business_qrcode
                    business.save()

            user.username = business.email
            user.email = business.email
            user.save()

            messages.info(request,u"机构信息修改成功！")
            # load_process_message(request,model_to_dict(old_business),model_to_dict(business),u'\u673a\u6784\u4fe1\u606f\u4fee\u6539',business.id,business)
        else:
            messages.error(request,u"机构信息修改失败,请完善信息!")
            return render_to_response("erp/modify_business_base_info.html",locals(),context_instance=RequestContext(request))

    return redirect("/erp/show_business_base_info")

''' 图片大小设置  '''
def set_picture_size(url):#TODO
    try:
        image_url = MEDIA_ROOT+str(url)
        image = Image.open(image_url)
        image.resize((128,128),Image.ANTIALIAS)
        image.save(image_url)
    except:
        pass

    '''
     # pil_im = Image.open('empire.jpg').convert('L')#改变图片颜色

     使用 crop() 方法可以从一幅图像中裁剪指定区域
     box = (100,100,400,400)
     region = pil_im.crop(box)

     可以调用 resize() 方法。该方法的参数是一个元组，用来指定新图像的大小：
     out = pil_im.resize((128,128))

    要旋转一幅图像，可以使用逆时针方式表示旋转角度，然后调用 rotate() 方法：
    out = pil_im.rotate(45)

    '''

''' 修改用户名(账号) '''
def username_change(request):
    user_id = request.GET.get("user_id","")
    user = User.objects.get(pk=user_id)
    # permissions = get_permissions(request)
    # business = get_business(request)
    # count = get_unread_examine(request)
    # user_agents,total_unread = get_user_agents(request,business)
    permissions,business,count,user_agents,total_unread = get_all_required(request)

    redi_type = request.GET.get("type")
    error = request.GET.get("error","")
    if redi_type == "agent_list":
        ageId = []
        agent_id = user.agent.id
        agents = business.agent_set.filter(is_active=1)
        for age in agents:
            ageId.append(age.id)
        if agent_id not in ageId:
            return redirect("/erp/no_permission/")

        message = u"修改手机号(账号)"
    if redi_type == "business_list":
        if not request.user.is_superuser:
           return redirect("/erp/no_permission/")
        message = u"修改邮箱(账号)"

    lv_unread = Redister_Business.objects.filter(status=3).count()
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        if username and password:
            if request.user.is_superuser and "business" in redi_type:
                user_name = User.objects.filter(username=username)
                if user_name:
                    error = u"该邮箱已存在！"
                else:
                    user.username = username
                    user.set_password(password)
                    user.email = username
                    user.save()
                    if user.business:
                        bussin = user.business
                        bussin.email = username
                        bussin.save()

                    success = send_email(username,user.first_name,username,password)#向创建的客户机构发送邮件通知
                    if not success:
                        url = request.get_full_path()+"&error=邮件发送失败,请重新发送"
                        return redirect(url)
                    messages.info(request,u"操作成功!")
                    return redirect("/erp/"+redi_type+"#"+redi_type)
            else:
                result = check_CellNumber(username)
                if result:
                    user_name = User.objects.filter(username=username)
                    if user_name:
                        error = u"该手机号已存在"
                    else:
                        user.username = username
                        user.set_password(password)
                        user.save()
                        if user.agent:
                            agent = user.agent
                            agent.phoneNum = username
                            agent.save()

                        code = business.business_num+str(user.agent.agent_num)
                        success = send_email_emp(request,user.agent.email,business.name,request.user.first_name,user.agent.name,username,password,str(user.agent.qrcode),code)#向创建的用户发送邮件通知
                                #                  邮件地址     发件机构名称        发件人           收件人名称         账号    密码            邀请码链接            邀请码
                        if not success:
                            url = request.get_full_path()+"&error=邮件发送失败,请重新发送"
                            return redirect(url)
                        messages.info(request,u"操作成功!")
                        return redirect("/erp/"+redi_type)
                else:
                    error = u"该手机号无效！"
        else:
            if request.user.is_superuser:
                error = u"新邮箱/密码不能为空！"
            else:
                error = u"新手机号/密码不能为空！"

        if redi_type == "agent_list":
            return render_to_response("erp/username_change.html",locals(),context_instance=RequestContext(request))
        if redi_type == "business_list":
            return render_to_response("erp/email_change.html",locals(),context_instance=RequestContext(request))
    else:
        if redi_type == "agent_list":
            return render_to_response("erp/username_change.html",locals(),context_instance=RequestContext(request))
        if redi_type == "business_list":
            return render_to_response("erp/email_change.html",locals(),context_instance=RequestContext(request))


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














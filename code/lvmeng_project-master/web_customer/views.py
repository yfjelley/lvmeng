#coding:utf-8
from web_customer.forms import Lv_announcement_Form
from django.template import RequestContext, loader
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import JsonResponse
from web_customer.models import Lv_Announcement
from erp.views2 import release_base_64
from erp.views import paginatorPage
from erp.models import Product,Business,Announcement
from api.models import Headline
from django.contrib import auth
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def homePage(request):
    lvs = Lv_Announcement.objects.filter(is_active=1)[:6]
    return render_to_response("web_customer/homePage/index_new.html",locals(),context_instance=RequestContext(request))

def homePage_ie8(request):
    lvs = Lv_Announcement.objects.filter(is_active=1)[:6]
    return render_to_response("web_customer/homePage/index_ie8.html",locals(),context_instance=RequestContext(request))


def mobile_homePage(request):

    return render_to_response("web_customer/homePage/index_mobile.html",locals(),context_instance=RequestContext(request))

# def announcement(request):
#     return render_to_response("web_customer/homePage/announcement.html",locals(),context_instance=RequestContext(request))


''' 客户登录 '''
def customer_login(request):
    if request.method == "GET":
        if request.user.is_authenticated() and request.user.last_name == u"客户":
            agents = request.user.customer.agents.all()#获取当前客户的所哟员工
            agent = agents[0]  #初始默认为第一个员工
            business = agent.business
            announcements = Announcement.objects.filter(announce_business=business,is_active=1)[:8]

            # products = agent.business.product_set.all()[:5]#获取默认员工的机构里面所有的产品
            products = agent.business.product_set.filter(is_active=1)[:5]#获取默认员工的机构里面所有的产品
            for pro in products:
                pro.return_expected = str(pro.return_expected*100).split(".")[0]
            success = "true"
            active = 100
            headlines = Headline.objects.all()[:6]
            return render_to_response('web_customer/customer_new/index_2.html',locals(),context_instance=RequestContext(request))
        return render_to_response("web_customer/customer_new/index.html",locals(),context_instance=RequestContext(request))
    if request.method == "POST":

        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username and password:
            userLogin = authenticate(username=username,password=password)

            if userLogin:
                auth.login(request,userLogin)
            else:
                error = u'!对不起,用户或密码不正确'
                return render_to_response('web_customer/customer_new/index.html',locals(),context_instance=RequestContext(request))
        else:
            error = u'!对不起,用户或密码不能为空'
            return render_to_response('web_customer/customer_new/index.html',locals(),context_instance=RequestContext(request))
        if userLogin.last_name == u"客户":
            agents = userLogin.customer.agents.all()#获取当前客户的所哟员工
            agent = agents[0]  #初始默认为第一个员工
            business = agent.business
            announcements = Announcement.objects.filter(announce_business=business,is_active=1)[:8]
            active = 100

            products = agent.business.product_set.filter(is_active=1)[:5]#获取默认员工的机构里面所有的产品
            for pro in products:
                pro.return_expected = str(pro.return_expected*100).split(".")[0]
            success = "true"
            headlines = Headline.objects.all()[:6]
            return render_to_response('web_customer/customer_new/index_2.html',locals(),context_instance=RequestContext(request))
        else:
            auth.logout(request)
            error = u'!对不起,用户或密码不正确'
            return render_to_response('web_customer/customer_new/index.html',locals(),context_instance=RequestContext(request))


def lv_announment(request):

    lvs = Lv_Announcement.objects.filter(is_active=1)
    annou_id = request.GET.get("annou_id","")
    try:
        announcement = Lv_Announcement.objects.get(pk=annou_id)
    except:
        return redirect("/")
    return render_to_response("web_customer/homePage/announcement.html",locals(),context_instance=RequestContext(request))

def check_announcement(request):
    id = request.GET.get("id")
    announcement = Lv_Announcement.objects.get(pk=id)
    return JsonResponse({"title":announcement.title,"text":announcement.text})

@login_required
def lv_announcement_list(request):
    if not request.user.is_superuser:
        return render_to_response("erp/no_permission.html",locals(),context_instance=RequestContext(request))
    lv_id = request.GET.get("lv_id","")
    if lv_id:
        lv = Lv_Announcement.objects.get(pk=lv_id)
        lv.is_active = 0
        lv.save()
    # lvs = Lv_Announcement.objects.filter(is_active=1)
    lvs,page_range,paginator = paginatorPage(request,Lv_Announcement.objects.filter(is_active=1))
    if lv_id:
        messages.info(request,u"律锰公告删除成功!")
        return redirect("/web_customer/lv_announcement_list/#lv_announcement_list")
    return render_to_response("erp/lv_announcement.html",locals(),context_instance=RequestContext(request))

@login_required
def lv_announcement_process(request):
    if not request.user.is_superuser:
        return render_to_response("erp/no_permission.html",locals(),context_instance=RequestContext(request))
    lv_id = request.GET.get("lv_id","")
    lv = None
    try:
        lv = Lv_Announcement.objects.get(pk=lv_id)
    except:
        pass
    if request.method == "GET":
        if lv_id:
            form = Lv_announcement_Form(instance=lv)
            message = u"修改律锰公告(*为必填项)"
        else:
            message = u"添加律锰公告(*为必填项)"
            form = Lv_announcement_Form()
        return render_to_response("erp/lv_announcement_process.html",locals(),context_instance=RequestContext(request))
    else:
        storage_url = None
        if lv_id:
            form = Lv_announcement_Form(request.POST or None, request.FILES,instance=lv)
            if form.is_valid():
                form.save()
                if request.POST.get("lv_picture-w[]"):
                    if request.POST.get("lv_picture-w[]") == "0":#调用裁剪图片方法
                        storage_url = release_base_64(request,"lv_picture","pass")
                    elif request.POST.get("lv_picture-w[]") != "0":
                        storage_url = release_base_64(request,"lv_picture","ahead")
                    if storage_url:
                        lv.lv_picture = storage_url
                        lv.save()
                messages.info(request,u"律锰公告修改成功!")
            else:
                message = u"修改律锰公告(*为必填项)"
                messages.error(request,u"律锰公告修改失败,请完善信息!")
                return render_to_response("erp/lv_announcement_process.html",locals(),context_instance=RequestContext(request))
        else:
            form = Lv_announcement_Form(request.POST or None, request.FILES)
            if form.is_valid():
                form.save()
                lv = Lv_Announcement()
                lv = form.instance
                if request.POST.get("lv_picture-w[]",""):
                    if request.POST.get("lv_picture-w[]") == "0":#调用裁剪图片方法
                        storage_url = release_base_64(request,"lv_picture","pass")
                    elif request.POST.get("lv_picture-w[]") != "0":
                        storage_url = release_base_64(request,"lv_picture","ahead")
                if storage_url:
                    lv.lv_picture = storage_url
                    lv.save()
                messages.info(request,u"律锰公告新增成功!")
            else:
                message = u"添加律锰公告(*为必填项)"
                messages.error(request,u"律锰公告新增失败,请完善信息!")
                return render_to_response("erp/lv_announcement_process.html",locals(),context_instance=RequestContext(request))
    return redirect("/web_customer/lv_announcement_list/#lv_announcement_list")

@login_required(login_url='customer_login/')
@user_passes_test(lambda u: u.last_name ==u"客户", login_url='customer_login/')
def product(request):
    bus_id = request.GET.get("bus_id")
    product_id = request.GET.get("product_id")
    if not bus_id or not product_id:
        return redirect("/customer_login/")
    elif not belong_business_customer(request,bus_id):
        return render_to_response("404_2.html",locals(),context_instance=RequestContext(request))
    agents = request.user.customer.agents.all()
    # agent = agents[0]  #初始默认为第一个员工
    business = Business.objects.get(pk=bus_id)
    product = Product.objects.get(business=bus_id,pk=product_id)
    expected = str(product.return_expected*100).split(".")[0]
    return render_to_response("web_customer/customer_new/product.html",locals(),context_instance=RequestContext(request))

''' 跳转到首页并定位所选项 '''
@login_required(login_url='customer_login/')
@user_passes_test(lambda u: u.last_name ==u"客户", login_url='customer_login/')
def redi_to_index(request):
    bus_id = request.GET.get("business_id","")
    if not bus_id:
        return redirect("/customer_login/")
    elif not belong_business_customer(request,bus_id):
        return render_to_response("404_2.html",locals(),context_instance=RequestContext(request))
    agents = request.user.customer.agents.all()#获取当前客户的所有员工
    business = Business.objects.get(pk=bus_id)

    products = business.product_set.all()[:5]#获取默认员工的机构里面所有的产品
    for pro in products:
        pro.return_expected = str(pro.return_expected*100).split(".")[0]
    success = "true"
    active = 100
    headlines = Headline.objects.all()[:6]
    announcements = Announcement.objects.filter(announce_business=bus_id,is_active=1)[:8]
    return render_to_response("web_customer/customer_new/index_2.html",locals(),context_instance=RequestContext(request))

''' web_customer 金融头条列表 '''
@login_required(login_url='customer_login/')
@user_passes_test(lambda u: u.last_name ==u"客户", login_url='customer_login/')
def web_customer_headline_list(request):
    bus_id = request.GET.get("bus_id","")
    if not bus_id:
        return redirect("/customer_login/")
    elif not belong_business_customer(request,bus_id):
        return render_to_response("404_2.html",locals(),context_instance=RequestContext(request))
    agents = request.user.customer.agents.all()#获取当前客户的所哟员工
    # agent = agents[0]  #初始默认为第一个员工
    business = Business.objects.get(pk=bus_id)

    success = "true"
    heads = Headline.objects.all()
    if heads:
        head = heads[0]
        headlines = heads[1:]
    return render_to_response("web_customer/customer_new/newslist.html",locals(),context_instance=RequestContext(request))

''' 金融头条详情 '''
@login_required(login_url='customer_login/')
@user_passes_test(lambda u: u.last_name ==u"客户", login_url='customer_login/')
def web_customer_headline_detail(request):
    line_id = request.GET.get("line_id","")
    bus_id = request.GET.get("bus_id","")
    if not line_id or not bus_id:
        return redirect("/customer_login/")
    if not belong_business_customer(request,bus_id):
        return render_to_response("404_2.html",locals(),context_instance=RequestContext(request))
    agents = request.user.customer.agents.all()#获取当前客户的所哟员工
    # agent = agents[0]  #初始默认为第一个员工
    business = Business.objects.get(pk=bus_id)

    headline = Headline.objects.get(pk=line_id)
    headline.read_num = headline.read_num+1
    headline.save()
    return render_to_response("web_customer/customer_new/news.html",locals(),context_instance=RequestContext(request))

''' 企业公告列表 '''
@login_required(login_url='customer_login/')
@user_passes_test(lambda u: u.last_name ==u"客户", login_url='customer_login/')
def noticelist(request):
    id = request.GET.get("business_id","")
    if not id:
        return redirect("/customer_login/")
    elif not belong_business_customer(request,id):
        return render_to_response("404_2.html",locals(),context_instance=RequestContext(request))
    agents = request.user.customer.agents.all()#获取当前客户的所哟员工
    business = Business.objects.get(pk=id)
    announs = Announcement.objects.filter(announce_business=business,is_active=1)
    announ_head = announs[0]
    announcements = announs[1:]
    success = "true"

    return render_to_response("web_customer/customer_new/noticelist.html",locals(),context_instance=RequestContext(request))

''' 企业公告详情 '''
@login_required(login_url='customer_login/')
@user_passes_test(lambda u: u.last_name ==u"客户", login_url='customer_login/')
def notice(request):
    id = request.GET.get("business_id","")
    announce_id = request.GET.get("announce_id","")

    if not id or not announce_id:
        return redirect("/customer_login/")
    elif not belong_business_customer(request,id):
        return render_to_response("404_2.html",locals(),context_instance=RequestContext(request))

    agents = request.user.customer.agents.all()#获取当前客户的所哟员工
    business = Business.objects.get(pk=id)
    announcement = Announcement.objects.get(announce_business=business,pk=announce_id)
    announcement.read_num = announcement.read_num+1
    announcement.save()
    success = "true"

    return render_to_response("web_customer/customer_new/notice.html",locals(),context_instance=RequestContext(request))

''' 判断该用户是否属于该机构 '''
def belong_business_employee(request):

    pass

''' 判断该客户是否属于该机构 '''
def belong_business_customer(request,business_id):
    ids = []
    agents = request.user.customer.agents.all()
    for agent in agents:
        ids.append(int(agent.business.id))
    if int(business_id) in ids:
        return 1
    else:
        return 0

''' 查看自己账户信息 '''
from api.models import Checkin
import time,datetime
@login_required(login_url='customer_login/')
@user_passes_test(lambda u: u.last_name ==u"客户", login_url='customer_login/')
def personal_info(request):
    check_in = None
    bus_id = request.GET.get("bus_id")
    if not bus_id:
        return redirect("/customer_login/")
    if not belong_business_customer(request,bus_id):
        return render_to_response("404_2.html",locals(),context_instance=RequestContext(request))
    current = time.strftime("%Y-%m-%d",time.localtime()).split("-")#当前时间
    agents = request.user.customer.agents.all()#获取当前客户的所有客户经理
    business = Business.objects.get(pk=bus_id)#当前客户所属机构
    customer = request.user.customer#当前客户

    check = Checkin.objects.filter(user=request.user)#获取积分和签到
    if check:
        check_in = check[0]

    products = customer.product_target.filter(business=business)#获取所有已购买的产品
    for pro in products:
        pro.expected = str(pro.return_expected*100).split(".")[0]#产品预期收益
        end = str(pro.end_date).split("-")
        pro.day = (datetime.datetime(int(current[0]),int(current[1]),int(current[2]))-datetime.datetime(int(end[0]),int(end[1]),int(end[2]))).days#产品剩余天数
    return render_to_response("web_customer/customer_new/personal.html",locals(),context_instance=RequestContext(request))

''' 用户选择机构显示相对应的信息 '''
@login_required(login_url='customer_login/')
@user_passes_test(lambda u: u.last_name ==u"客户", login_url='customer_login/')
def customer_business_search(request):
    bus_id = None
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
@login_required(login_url='customer_login/')
@user_passes_test(lambda u: u.last_name ==u"客户", login_url='customer_login/')
def show_product_by_type(request):
    bus_id = request.GET.get("bus_id","")
    product_type = request.GET.get("product_type","")
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

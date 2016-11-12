#coding:utf8
from django.test import TestCase

# Create your tests here.

from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from django.contrib import auth
from selenium import webdriver
from django.core.management import call_command
from lvmeng.settings import MEDIA_ROOT
from PIL import Image
import time
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.shortcuts import render,render_to_response,redirect
# from selenium.webdriver.common.action_chains import ActionChains
'''
1,登录,查看个人信息,登出
2,添加金融头条,修改金融头条,删除金融头条(已测试，由于confirm中文不支持),查看金融头条[admin]
3,客户机构列表,添加客户机构,修改客户机构,修改密码(客户机构),重发邮件(客户机构),删除机构(已测试),查看机构详细信息(客户机构),根据机构编号搜索[admin]
4,律锰公告列表,添加律锰公告,修改律锰公告,删除律锰公告(已测试),查看律锰公告[admin]
5,律锰公告列表,角色查看列表,所有员工,查看员工信息,在员工信息里面点击查看该员工的客户信息,查看理财师的所有客户,点击产品数量进入该客户所购买的产品,查看产品详情,根据员工姓名搜索[admin]
6,律锰公告列表,角色查看列表,所有客户,查看客户信息,点击进入客户所有购买产品,查看产品详情,根据客户姓名搜索[admin]
7,所有机构,该机构所有员工,该机构所有客户,该机构所有产品,查看机构信息
8,查看本机构基本信息,修改本机构基本信息[business]
9,职位列表,添加职位,职位修改[business]
10,员工列表,员工添加,员工修改[business]
11,员工列表,员工查看,在员工查看里面查看所拥有的客户的信息[business]
12,员工列表,解除手机绑定,删除理财师,根据姓名搜索员工[business]
13,员工通讯录列表,根据姓名搜索员工[business]
14,添加机构公告信息(对外),修改公告信息,删除机构公告信息(对外),查看机构公告信息(对外)[business]
15,产品列表,添加产品,修改产品,删除产品[business]

16,客户列表,添加购买,客户购买列表,查看客户购买基本信息[agent]
17,客户列表,修改客户信息,点击产品购买数量进入查看产品详情,返回客户列表,删除意向客户,查看客户详情[agent]
'''
def test_login(request):
    if request.method == "GET":
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

                print username,password,user_business,user.username
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
        try:
            user_customer = userLogin.business   #判断是否是客户
        except:
            user_customer = None
    # return redirect('/erp/financial_headlines/#financial_headlines')
    return redirect('/erp/business_announcement_list/#business_announcement_list')

def create_data():
    #python manage.py dumpdata > lv_test_data.json
    # call_command("loaddata --clobber", "lv_test_data.json")
    call_command("loaddata", "lv_test_data.json")

#====================================================admin begin==================================
'''
class AdminTestCase(LiveServerTestCase):#登录,登出测试
    def setUp(self):
        # setUp is where you instantiate the selenium webdriver and loads the browser.
        # User.objects.create_superuser(
        #     username='test',
        #     password='test',
        #     email='admin@example.com'
        # )
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(AdminTestCase, self).setUp()

    def tearDown(self):
        # Call tearDown to close the web browser
        self.selenium.quit()
        super(AdminTestCase, self).tearDown()
    #user login
    def test_user_login(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/login/")
        )
        # Fill login information of admin
        username = self.selenium.find_element_by_id("username")
        username.send_keys("test")
        password = self.selenium.find_element_by_id("password")
        password.send_keys("test")

        # 提交表单
        self.selenium.find_element_by_id("submit").submit()
        time.sleep(5)
        #查看个人信息
        self.selenium.find_element_by_xpath("//a[@data-toggle='dropdown']").click()
        time.sleep(5)
        #登出
        self.selenium.find_element_by_class_name("logout")
        time.sleep(10)
        # class_name = self.selenium.find_element_by_class_name("logout")
        # self.assertEqual(class_name.get_attribute("innerHTML"),u"退出")
'''
'''
class test_headlines(LiveServerTestCase):#金融头条测试
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/test/"))
        self.selenium.find_element_by_id("username").send_keys("test")
        self.selenium.find_element_by_id("password").send_keys("test")
        self.selenium.find_element_by_id("submit").submit()
        super(test_headlines, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_headlines, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_headline(self):
        #点击添加金融头条
        self.selenium.find_element_by_id("lvmeng_click").click()
        time.sleep(3)
        self.wait_css_class("li.financial_headlines a").click()
        time.sleep(5)
        self.wait_css_class("div.btn-add a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_title").send_keys("headline2")#标题
        self.btn_submit().submit()
        time.sleep(5)
        #修改金融头条
        self.selenium.find_element_by_class_name("headline_modify").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_title").send_keys("modify")
        self.btn_submit().submit()
        time.sleep(5)
        #删除金融头条(已测试，由于confirm中文不支持)
        #self.selenium.find_element_by_class_name("headline_delete").click()

        #查看金融头条
        self.selenium.find_element_by_class_name("headline_check").click()

        time.sleep(20)#此处等待为了观察是否成功,等待加载，否则error: [Errno 10054]
'''
'''
class test_admin_business(LiveServerTestCase):#律锰对机构的操作

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/test/"))
        self.selenium.find_element_by_id("username").send_keys("test")
        self.selenium.find_element_by_id("password").send_keys("test")
        self.selenium.find_element_by_id("submit").submit()
        super(test_admin_business, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_admin_business, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_business(self):
        #客户机构列表
        self.selenium.find_element_by_id("lvmeng_click").click()
        time.sleep(3)
        self.wait_css_class("li.business_list a").click()
        time.sleep(5)
        #添加客户机构
        self.wait_css_class("li.business_process a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_name").send_keys("NiuJiDui")
        self.selenium.find_element_by_id("id_business_num").send_keys("B0022")
        self.selenium.find_element_by_id("id_phoneNum").send_keys("18701730286")
        self.selenium.find_element_by_id("init_password").send_keys("88888888")
        self.selenium.find_element_by_id("id_business_phone").send_keys("18701730286")
        self.selenium.find_element_by_id("id_email").send_keys("1668380928@qq.com")
        self.selenium.find_element_by_id("id_business_email").send_keys("1668380928@qq.com")
        self.selenium.find_element_by_id("id_address").send_keys("BeiJing")
        self.selenium.find_element_by_id("id_work_address").send_keys("ShangHai")
        self.btn_submit().submit()
        time.sleep(5)
        #修改客户机构
        self.selenium.find_element_by_class_name("business_modify").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_name").send_keys("--NiuJiDui")
        self.btn_submit().submit()
        time.sleep(5)
        #修改密码(客户机构)
        self.selenium.find_element_by_class_name("business_password_modify").click()
        time.sleep(5)
        self.selenium.find_element_by_id("password").send_keys("12345678")
        self.selenium.find_element_by_id("password2").send_keys("12345678")
        self.selenium.find_element_by_class_name("btn-change-pwd").click()
        time.sleep(5)

        #重发邮件(客户机构)
        self.selenium.find_element_by_class_name("email_resend").click()
        time.sleep(5)
        self.selenium.find_element_by_id("password").send_keys("12345678")
        self.selenium.find_element_by_id("password2").send_keys("12345678")
        self.selenium.find_element_by_class_name("btn-change-pwd").click()
        time.sleep(5)
        #删除机构(已测试)
        #####self.selenium.find_element_by_class_name("business_delete").click()
        #####time.sleep(5)
        #查看机构详细信息(客户机构)
        self.selenium.find_element_by_class_name("business_check").click()
        time.sleep(5)
        #根据机构编号搜索
        self.wait_css_class("li.business_list a").click()
        time.sleep(5)
        self.selenium.find_element_by_xpath("//input[@name='business_num']").send_keys("B0011")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)
'''
'''
class test_lv_announcement(LiveServerTestCase):#律锰公告测试

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/test/"))
        self.selenium.find_element_by_id("username").send_keys("test")
        self.selenium.find_element_by_id("password").send_keys("test")
        self.selenium.find_element_by_id("submit").submit()
        super(test_lv_announcement, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_lv_announcement, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_lv_announcement(self):
        #律锰公告列表
        self.selenium.find_element_by_id("lvmeng_click").click()
        time.sleep(3)
        self.wait_css_class("li.lv_announcement_list a").click()
        time.sleep(5)

        #点击添加律锰公告
        self.wait_css_class("div.btn-add a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_title").send_keys("lv_announcement_01")
        self.btn_submit().submit()
        time.sleep(5)
        #修改律锰公告
        self.selenium.find_element_by_class_name("lv_announcement_modify").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_title").send_keys("modify")
        self.btn_submit().submit()
        time.sleep(5)
        #删除律锰公告(已测试)
        ####self.selenium.find_element_by_class_name("lv_announcement_delete").click()
        ####time.sleep(3)

        #查看律锰公告
        self.selenium.find_element_by_class_name("lv_announcement_check").click()
        time.sleep(20)
'''
'''
class test_role_employee(LiveServerTestCase):#律锰按角色（员工查看）
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/test/"))
        self.selenium.find_element_by_id("username").send_keys("test")
        self.selenium.find_element_by_id("password").send_keys("test")
        self.selenium.find_element_by_id("submit").submit()
        super(test_role_employee, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_role_employee, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_role_employee(self):
        self.selenium.find_element_by_id("lvmeng_click").click()
        time.sleep(3)
        #角色查看列表
        self.selenium.find_element_by_id("role_click").click()
        time.sleep(3)
        #所有员工
        self.wait_css_class("li.admin_agent_list a").click()
        time.sleep(5)
        #查看员工信息
        self.selenium.find_element_by_class_name("check_agent").click()
        time.sleep(5)
        #在员工信息里面点击查看该员工的客户信息
        self.selenium.find_element_by_class_name("customer_check").click()
        time.sleep(5)
        #查看理财师的所有客户
        self.wait_css_class("li.admin_agent_list a").click()
        time.sleep(5)
        self.selenium.find_elements_by_class_name("agent_count")[2].click()
        time.sleep(5)
        #点击产品数量进入该客户所购买的产品
        self.selenium.find_element_by_class_name("product_count").click()
        time.sleep(5)
        #查看产品详情
        self.selenium.find_element_by_class_name("product_check").click()
        time.sleep(5)
        #根据员工姓名搜索
        self.wait_css_class("li.admin_agent_list a").click()
        time.sleep(5)
        self.selenium.find_element_by_xpath("//input[@name='agent_name']").send_keys("where")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)
'''
'''
class test_role_customer(LiveServerTestCase):#律锰按角色（客户查看）
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/test/"))
        self.selenium.find_element_by_id("username").send_keys("test")
        self.selenium.find_element_by_id("password").send_keys("test")
        self.selenium.find_element_by_id("submit").submit()
        super(test_role_customer, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_role_customer, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_role_customer(self):
        self.selenium.find_element_by_id("lvmeng_click").click()
        time.sleep(3)
        #角色查看列表
        self.selenium.find_element_by_id("role_click").click()
        time.sleep(3)
        #所有客户
        self.wait_css_class("li.admin_customers a").click()
        time.sleep(5)
        #查看客户信息
        self.selenium.find_element_by_class_name("customer_check").click()
        time.sleep(5)
        #点击进入客户所有购买产品
        self.wait_css_class("li.admin_customers a").click()
        time.sleep(5)
        self.selenium.find_element_by_class_name("customer_count").click()
        time.sleep(5)
        #查看产品详情
        self.selenium.find_element_by_class_name("product_check").click()
        time.sleep(5)
        #按客户姓名搜索
        self.wait_css_class("li.admin_customers a").click()
        time.sleep(5)
        self.selenium.find_element_by_xpath("//input[@name='customer_name']").send_keys("join")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)
'''
'''
class test_admin_business_info(LiveServerTestCase):#律锰通过机构查看该机构所有的员工和客户
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/test/"))
        self.selenium.find_element_by_id("username").send_keys("test")
        self.selenium.find_element_by_id("password").send_keys("test")
        self.selenium.find_element_by_id("submit").submit()
        super(test_admin_business_info, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_admin_business_info, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_admin_business_info(self):
        self.selenium.find_element_by_id("lvmeng_click").click()
        time.sleep(3)
        #所有机构
        self.wait_css_class("li.business_list a").click()
        time.sleep(5)
        #该机构所有员工
        self.selenium.find_element_by_class_name("business_agent").click()
        time.sleep(5)
        self.wait_css_class("li.business_list a").click()
        time.sleep(5)
        #该机构所有客户
        self.selenium.find_element_by_class_name("business_customers").click()
        time.sleep(5)
        self.wait_css_class("li.business_list a").click()
        time.sleep(5)
        #该机构所有产品
        self.selenium.find_element_by_class_name("product_check").click()
        time.sleep(5)
        self.wait_css_class("li.business_list a").click()
        time.sleep(5)
        #查看机构信息
        self.selenium.find_element_by_class_name("business_check").click()
        time.sleep(20)
'''
#===============================================admin end====================================================

#==============================================business begin================================================
'''
class test_business_base_info(LiveServerTestCase):#机构操作基本信息测试

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("nicai")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_business_base_info, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_business_base_info, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_business_base_info(self):

        #查看本机构基本信息
        self.selenium.find_element_by_id("business_click").click()
        time.sleep(3)
        self.wait_css_class("li.show_business_base_info a").click()
        time.sleep(5)

        #修改本机构基本信息
        self.wait_css_class("div.btn-modify a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_work_address").send_keys("modify")
        self.btn_submit().submit()
        time.sleep(20)
'''
'''
class test_business_position(LiveServerTestCase):#机构操作职位测试

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("nicai")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_business_position, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_business_position, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_business_base_info(self):

        self.selenium.find_element_by_id("employee_click").click()
        time.sleep(3)
        #职位列表
        self.wait_css_class("li.position_list a").click()
        time.sleep(5)
        #添加职位
        self.wait_css_class("div.btn-add a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_permissions_1").click()
        self.selenium.find_element_by_id("id_permissions_2").click()
        self.selenium.find_element_by_id("id_permissions_3").click()
        self.selenium.find_element_by_id("id_permissions_4").click()
        self.selenium.find_element_by_id("id_permissions_5").click()
        self.selenium.find_element_by_id("id_permissions_6").click()
        self.selenium.find_element_by_id("id_name").send_keys("manager")
        self.selenium.find_element_by_id("id_department").send_keys("Technology")
        self.btn_submit().submit()
        time.sleep(5)
        #职位修改
        self.selenium.find_element_by_class_name("position_modify").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_name").send_keys("manager lead")
        self.btn_submit().submit()
        time.sleep(20)
'''
'''
class test_business_agent(LiveServerTestCase):#机构操作员工测试(不含删除)

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("nicai")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_business_agent, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_business_agent, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_business_base_info(self):
        self.selenium.find_element_by_id("employee_click").click()
        time.sleep(3)
        #员工列表
        self.wait_css_class("li.agent_list a").click()
        time.sleep(5)
        #员工添加
        self.wait_css_class("li.agent_process a").click()
        time.sleep(5)
        self.selenium.find_elements_by_tag_name("option")[1].click()
        self.selenium.find_element_by_id("id_name").send_keys("louis")
        self.selenium.find_element_by_id("id_phoneNum").send_keys("18701730286")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("id_email").send_keys("1668380928@qq.com")
        self.selenium.find_element_by_id("id_address").send_keys("shanghai")
        self.selenium.find_element_by_id("id_idCard_num").send_keys("342625199102082395")
        self.btn_submit().submit()
        time.sleep(5)

        #员工修改
        self.selenium.find_element_by_class_name("agent_modify").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_name").send_keys("_modify")
        self.btn_submit().submit()

        time.sleep(20)
'''
'''
class test_business_agent_check(LiveServerTestCase):#机构操作员工查看并查看该员工拥有的客户信息

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("nicai")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_business_agent_check, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_business_agent_check, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_business_agent_info(self):
        self.selenium.find_element_by_id("employee_click").click()
        time.sleep(5)
        #员工列表
        self.wait_css_class("li.agent_list a").click()
        time.sleep(5)

        #员工查看
        self.selenium.find_elements_by_class_name("agent_check")[3].click()
        time.sleep(5)
        #在员工查看里面查看所拥有的客户的信息
        self.selenium.find_element_by_class_name("customer_check").click()

        time.sleep(20)
'''
'''
class test_business_agent_delete(LiveServerTestCase):#机构删除员工测试

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("nicai")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_business_agent_delete, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_business_agent_delete, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_business_base_info(self):
        self.selenium.find_element_by_id("employee_click").click()
        time.sleep(5)
        #员工列表
        self.wait_css_class("li.agent_list a").click()
        time.sleep(5)

        #解除手机绑定(已测试)
        #####self.selenium.find_element_by_class_name("device_delete").click()
        #####time.sleep(3)

        #删除理财师
        self.selenium.find_elements_by_class_name("agent_delete")[2].click()
        time.sleep(5)
        self.selenium.find_element_by_id("submit").click()
        time.sleep(5)
        #根据姓名搜索员工
        self.selenium.find_element_by_xpath("//input[@name='agent_name']").send_keys("home")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)

'''
'''
class test_business_mail_list(LiveServerTestCase):#机构查看员工通信录测试

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("nicai")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_business_mail_list, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_business_mail_list, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_business_mail_list(self):
        self.selenium.find_element_by_id("employee_click").click()
        time.sleep(5)
        #员工通讯录列表
        self.wait_css_class("li.mail_list a").click()
        time.sleep(5)
        #根据姓名搜索员工
        self.selenium.find_element_by_xpath("//input[@name='agent_name']").send_keys("home")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)
'''
'''
class test_business_announcement(LiveServerTestCase):#机构对机构公告操作测试(对外)

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("nicai")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_business_announcement, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_business_announcement, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_business_announcement(self):
        #添加机构公告信息(对外)
        self.wait_css_class("li.picture_logos a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_title").send_keys("ShangHai No 2")
        self.selenium.find_element_by_id("id_order").send_keys("2")
        self.btn_submit().submit()
        time.sleep(5)
        #修改公告信息
        self.selenium.find_element_by_class_name("announcement_modify").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_title").send_keys("modify")
        self.btn_submit().submit()
        time.sleep(5)

         #删除机构公告信息(对外)
        ####self.selenium.find_element_by_class_name("announcement_delete").click()
        ###time.sleep(5)

        #查看机构公告信息(对外)
        self.selenium.find_element_by_class_name("announcement_check").click()
        time.sleep(20)
'''
'''
class test_business_product_add(LiveServerTestCase):#机构对产品操作测试

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("nicai")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_business_product_add, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_business_product_add, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_business_product_add(self):
        #产品列表
        self.selenium.find_element_by_id("product_click").click()
        time.sleep(5)
        #添加产品
        self.wait_css_class("li.product_process a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_name").send_keys("product 1")
        self.selenium.find_element_by_id("id_abbreviation").send_keys("product 1")
        self.selenium.find_element_by_id("id_return_expected").send_keys("1")
        self.selenium.find_element_by_id("id_period").send_keys("12")
        self.selenium.find_element_by_id("id_mini_sub").send_keys("1000")
        self.selenium.find_element_by_id("id_manager").send_keys("zhang san")
        self.btn_submit().submit()
        time.sleep(5)
        #修改产品
        self.selenium.find_element_by_class_name("product_modify").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_return_expected").send_keys("1")
        self.btn_submit().submit()
        time.sleep(5)
        #删除产品
        ###self.selenium.find_element_by_class_name("product_delete").click()
        time.sleep(20)
'''
#==============================================business end==================================================

#============================================agent begin=====================================================
'''
class test_customer_purchase(LiveServerTestCase):#理财师添加客户购买

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_customer_purchase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_customer_purchase, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_customer_purchase(self):
        self.selenium.find_element_by_id("agent_click").click()
        time.sleep(5)
        #客户列表
        self.wait_css_class("li.customer_list a").click()
        time.sleep(5)
        #添加购买
        self.selenium.find_element_by_class_name("product_purchase").click()
        time.sleep(5)
        self.selenium.find_elements_by_tag_name("option")[1].click()
        self.selenium.find_element_by_id("id_amount").send_keys("100000")
        self.selenium.find_element_by_xpath("//input[@id='id_income_date']").send_keys("2016/07/13")
        self.selenium.find_element_by_xpath("//input[@id='id_end_date']").send_keys("2016/07/13")
        self.btn_submit().submit()
        time.sleep(5)
        #查看客户购买基本信息
        self.selenium.find_element_by_xpath("//td[@class='sorting_1']/a").click()
        time.sleep(20)
'''
'''
class test_customer_process(LiveServerTestCase):#理财师修改、删除、查看客户，点击购买产品数量--》查看产品详情

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_customer_process, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_customer_process, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_customer_process(self):
        self.selenium.find_element_by_id("agent_click").click()
        time.sleep(5)
        #客户列表
        self.wait_css_class("li.customer_list a").click()
        time.sleep(5)
        #修改客户信息
        self.selenium.find_element_by_class_name("customer_modify").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_name").send_keys("_modify")
        self.btn_submit().submit()
        time.sleep(8)
        #点击产品购买数量，进入查看产品详情
        self.selenium.find_element_by_class_name("counts").click()
        time.sleep(5)
        self.selenium.find_element_by_class_name("product_check").click()
        time.sleep(5)
        #返回客户列表
        self.wait_css_class("li.customer_list a").click()
        time.sleep(5)
        #删除意向客户
        #####self.selenium.find_element_by_class_name("customer_delete").click()
        #####time.sleep(5)
        #查看客户详情
        self.selenium.find_element_by_class_name("customer_check").click()
        time.sleep(20)
'''

#===========================================agent end========================================================





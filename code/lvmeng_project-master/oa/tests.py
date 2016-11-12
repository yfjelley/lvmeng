#coding:utf-8
from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from django.core.management import call_command
import time
from selenium.webdriver.support.wait import WebDriverWait
time_out = 5
# Create your tests here.
'''
1,点击打开办公自动化,每日待办列表,点击新增每日待办,保存新增,根据时间搜索
2,点击打开办公自动化,每日待办列表,修改每日待办,删除每日待办,查看每日待办
3,点击打开办公自动化,点击打开协同办公,内部公告列表,内部公告添加,查看公告,返回列表是否已读,根据主题搜索
4,点击打开办公自动化,点击打开协同办公,内部公告列表,修改内部公告,删除内部公告
5,点击打开办公自动化,点击打开协同办公,工作汇报列表,新增工作汇报,查看汇报内容,根据填报时间搜索
6,点击打开办公自动化,点击打开协同办公,工作汇报列表,查看汇报审批，删除汇报
7,点击打开办公自动化,点击打开协同办公,费用申请列表,费用申请添加，查看费用申请内容,根据时间搜索
8,点击打开办公自动化,点击打开协同办公,费用申请列表,查看费用审批,费用申请删除
9,点击打开办公自动化,点击打开协同办公,请假申请列表,请假申请添加，查看请假申请内容
10,点击打开办公自动化,点击打开协同办公,请假申请列表,查看请假审批,请假申请删除
11,点击打开办公自动化,点击打开协同办公,出差申请列表,出差申请添加，查看出差申请内容
12,点击打开办公自动化,点击打开协同办公,出差申请列表,查看出差审批,出差申请删除
13,点击打开办公自动化,点击打开协同办公,审批列表,点击审批,按类型搜索
14,点击打开办公自动化,点击打开财务管理,客户搜索
'''
def create_data():
    #python manage.py dumpdata > lv_test_data.json
    # call_command("loaddata --clobber", "lv_test_data.json")
    call_command("loaddata", "lv_test_data.json")

'''
class test_daily_add(LiveServerTestCase):#每日待办新增
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_daily_add, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_daily_add, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_daily_add(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(5)
        #每日待办列表
        self.wait_css_class("li.daily_todo_list a").click()
        time.sleep(5)
        #点击新增每日待办
        self.wait_css_class("div.btn-add a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_topic").send_keys("qqqqqqq")
        self.selenium.find_element_by_id("id_content").send_keys("bbbbb")
        self.selenium.find_element_by_xpath("//input[@id='id_to_do_time']").send_keys("2016/07/15 10:15")
        self.btn_submit().submit()
        time.sleep(5)
        #根据时间搜索
        self.selenium.find_element_by_id("data").send_keys("2016-07-11")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)
'''
'''
class test_daily_to_do(LiveServerTestCase):#每日待办修改，删除，查看

    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_daily_to_do, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_daily_to_do, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_daily_to_do(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(5)
        #每日待办列表
        self.wait_css_class("li.daily_todo_list a").click()
        time.sleep(5)
        #修改每日待办
        self.selenium.find_element_by_class_name("daily_modify").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_topic").send_keys("_modify")
        self.btn_submit().submit()
        time.sleep(5)
        #删除每日待办
        #####self.selenium.find_element_by_class_name("daily_delete").click()
        #####time.sleep(5)
        #查看每日待办
        self.selenium.find_element_by_class_name("daily_check").click()
        time.sleep(20)
'''
'''
class test_announcement_inner(LiveServerTestCase):#内部公告(面向员工),添加、查看
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_announcement_inner, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_announcement_inner, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_announcement_inner(self):

        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(2)
        #点击打开协同办公
        self.selenium.find_element_by_id("Cooperative_Office_click").click()
        time.sleep(5)
        #内部公告列表
        self.wait_css_class("li.announcement_employee a").click()
        time.sleep(5)
        #内部公告添加
        self.wait_css_class("div.btn-add a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_topic").send_keys("ssssssss")
        self.selenium.find_element_by_xpath("//input[@id='id_onTop_start']").send_keys("2016/07/14")
        self.selenium.find_element_by_xpath("//input[@id='id_onTop_end']").send_keys("2016/07/06")
        self.selenium.find_element_by_xpath("//input[@id='id_publish_start']").send_keys("2016/07/14")
        self.selenium.find_element_by_xpath("//input[@id='id_publish_end']").send_keys("2016/07/06")
        self.btn_submit().submit()
        time.sleep(5)
        #查看公告
        self.selenium.find_element_by_class_name("announcement_check").click()
        time.sleep(5)
        #返回列表是否已读
        self.wait_css_class("li.announcement_employee a").click()
        time.sleep(5)
        #根据主题搜索
        self.selenium.find_element_by_id("topic").send_keys("sssss")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)
'''
'''
class test_announcement_modify_delete(LiveServerTestCase):#内部公告(面向员工),修改、删除
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_announcement_modify_delete, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_announcement_modify_delete, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_announcement_modify_delete(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(2)
        #点击打开协同办公
        self.selenium.find_element_by_id("Cooperative_Office_click").click()
        time.sleep(5)
        #内部公告列表
        self.wait_css_class("li.announcement_employee a").click()
        time.sleep(5)
        #修改内部公告
        self.selenium.find_element_by_class_name("announcement_modify").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_topic").send_keys("_modify")
        self.btn_submit().submit()
        time.sleep(5)
        #删除内部公告
        #####self.selenium.find_element_by_class_name("announcement_delete").click()
        time.sleep(20)
'''
'''
class test_daily_work_add_check(LiveServerTestCase):#工作汇报列表
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_daily_work_add_check, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_daily_work_add_check, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_daily_work_add_check(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(2)
        #点击打开协同办公
        self.selenium.find_element_by_id("Cooperative_Office_click").click()
        time.sleep(5)
        #工作汇报列表
        self.wait_css_class("li.daily_work a").click()
        time.sleep(5)
        #新增工作汇报
        self.wait_css_class("div.btn-add a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_examine_user_1").click()
        self.selenium.find_element_by_id("id_examine_user_2").click()
        self.selenium.find_element_by_id("id_topic").send_keys("11111111")
        self.selenium.find_element_by_id("id_content").send_keys("22222222")
        self.selenium.find_elements_by_tag_name("option")[2].click()
        self.btn_submit().submit()
        time.sleep(5)
        #查看汇报内容
        self.selenium.find_element_by_class_name("daily_check").click()
        #根据填报时间搜索
        self.wait_css_class("li.daily_work a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("data").send_keys("2016-07-11")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)
'''
'''
class test_daily_delete_checkExamine(LiveServerTestCase):#查看汇报审批，删除汇报
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_daily_delete_checkExamine, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_daily_delete_checkExamine, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_daily_delete_checkExamine(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(2)
        #点击打开协同办公
        self.selenium.find_element_by_id("Cooperative_Office_click").click()
        time.sleep(5)
        #工作汇报列表
        self.wait_css_class("li.daily_work a").click()
        time.sleep(5)
        #查看汇报审批
        self.selenium.find_element_by_class_name("daily_examine").click()
        time.sleep(5)
        self.wait_css_class("li.daily_work a").click()
        time.sleep(5)
        #删除汇报
        #####self.selenium.find_element_by_class_name("daily_delete").click()
        time.sleep(20)
'''
'''
class test_cost_add_check(LiveServerTestCase):#费用申请添加，查看费用申请内容
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_cost_add_check, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_cost_add_check, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_cost_add_check(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(2)
        #点击打开协同办公
        self.selenium.find_element_by_id("Cooperative_Office_click").click()
        time.sleep(5)
        #费用申请列表
        self.wait_css_class("li.cost_application a").click()
        time.sleep(5)
        #添加费用申请
        self.selenium.find_element_by_class_name("btn-add").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_examine_user_1").click()
        self.selenium.find_element_by_id("id_examine_user_2").click()
        self.selenium.find_element_by_id("id_topic").send_keys("1111111")
        self.selenium.find_element_by_id("id_content").send_keys("122222")
        self.selenium.find_element_by_id("id_cost").send_keys("100000")
        self.btn_submit().submit()
        time.sleep(5)
        #查看费用申请内容
        self.selenium.find_element_by_class_name("cost_check").click()
        time.sleep(5)
        #根据时间搜索
        self.wait_css_class("li.cost_application a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("data").send_keys("2016-07-11")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)
'''
'''
class test_leave_add_check(LiveServerTestCase):#请假申请添加，查看请假审批内容查看
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_leave_add_check, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_leave_add_check, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_leave_add_check(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(2)
        #点击打开协同办公
        self.selenium.find_element_by_id("Cooperative_Office_click").click()
        time.sleep(5)
        #请假申请列表
        self.wait_css_class("li.leave_management a").click()
        time.sleep(5)
        #添加请假申请
        self.selenium.find_element_by_class_name("btn-add").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_examine_user_1").click()
        self.selenium.find_element_by_id("id_examine_user_2").click()
        self.selenium.find_element_by_id("id_topic").send_keys("1111111")
        self.selenium.find_element_by_id("id_content").send_keys("122222")
        self.selenium.find_element_by_xpath("//input[@id='id_start']").send_keys("2016/07/13")
        self.selenium.find_element_by_xpath("//input[@id='id_end']").send_keys("2016/07/29")
        self.btn_submit().submit()
        time.sleep(5)
        #查看请假申请内容
        self.selenium.find_element_by_class_name("leave_check").click()
        time.sleep(5)
        #根据日期搜索
        self.wait_css_class("li.leave_management a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("data").send_keys("2016-07-11")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)
'''
'''
class test_leave_delete_checkExamine(LiveServerTestCase):#请假申请删除，查看请假审批
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_leave_delete_checkExamine, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_leave_delete_checkExamine, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_leave_delete_checkExamine(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(2)
        #点击打开协同办公
        self.selenium.find_element_by_id("Cooperative_Office_click").click()
        time.sleep(5)
        #请假申请列表
        self.wait_css_class("li.leave_management a").click()
        time.sleep(5)
        #查看请假申请审核
        self.selenium.find_element_by_class_name("leave_examine").click()
        time.sleep(5)
        #删除请假申请
        #####self.wait_css_class("li.leave_management a").click()
        #####time.sleep(5)
        #####self.selenium.find_element_by_class_name("leave_delete").click()
        time.sleep(20)
'''
'''
class test_travel_add_check(LiveServerTestCase):#出差申请添加，查看出差审批内容查看
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_travel_add_check, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_travel_add_check, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_travel_add_check(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(2)
        #点击打开协同办公
        self.selenium.find_element_by_id("Cooperative_Office_click").click()
        time.sleep(5)
        #出差申请列表
        self.wait_css_class("li.travel_apply a").click()
        time.sleep(5)
        #添加出差申请
        self.selenium.find_element_by_class_name("btn-add").click()
        time.sleep(5)
        self.selenium.find_element_by_id("id_examine_user_1").click()
        self.selenium.find_element_by_id("id_examine_user_2").click()
        self.selenium.find_element_by_id("id_topic").send_keys("1111111")
        self.selenium.find_element_by_id("id_content").send_keys("122222")
        self.selenium.find_element_by_id("id_cost").send_keys("100000")
        self.selenium.find_element_by_xpath("//input[@id='id_start']").send_keys("2016/07/13")
        self.selenium.find_element_by_xpath("//input[@id='id_end']").send_keys("2016/07/29")
        self.btn_submit().submit()
        time.sleep(5)
        #查看出差申请内容
        self.selenium.find_element_by_class_name("travel_check").click()
        time.sleep(5)
        #根据日期搜索
        self.wait_css_class("li.travel_apply a").click()
        time.sleep(5)
        self.selenium.find_element_by_id("data").send_keys("2016-07-11")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)
'''
'''
class test_travel_delete_checkExamine(LiveServerTestCase):#出差申请删除，查看出差审批
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_travel_delete_checkExamine, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_travel_delete_checkExamine, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_travel_delete_checkExamine(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(2)
        #点击打开协同办公
        self.selenium.find_element_by_id("Cooperative_Office_click").click()
        time.sleep(5)
        #请假申请列表
        self.wait_css_class("li.travel_apply a").click()
        time.sleep(5)
        #查看请假申请审核
        self.selenium.find_element_by_class_name("travel_examine").click()
        time.sleep(5)
        #删除请假申请
        #####self.wait_css_class("li.travel_apply a").click()
        #####time.sleep(5)
        #####self.selenium.find_element_by_class_name("travel_delete").click()
        time.sleep(20)
'''
'''
class test_examine(LiveServerTestCase):#审批列表,审批,按类型搜索
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_examine, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_examine, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_examine(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(2)
        #点击打开协同办公
        self.selenium.find_element_by_id("Cooperative_Office_click").click()
        time.sleep(5)
        #审批列表
        self.wait_css_class("li.examine_list a").click()
        time.sleep(5)
        #审批
        self.selenium.find_element_by_class_name("examine").click()
        time.sleep(5)
        self.selenium.find_elements_by_tag_name("option")[0].click()
        self.selenium.find_element_by_id("id_examine_message").send_keys("You get it!")
        self.btn_submit().submit()
        time.sleep(5)
        #按类型搜索
        self.selenium.find_elements_by_tag_name("option")[2].click()
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(20)
'''
'''
class test_income_inquiry(LiveServerTestCase):#收款查询测试
    def setUp(self):
        create_data()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get( '%s%s' % (self.live_server_url,  "/login/"))
        self.selenium.find_element_by_id("username").send_keys("B00111")
        self.selenium.find_element_by_id("password").send_keys("88888888")
        self.selenium.find_element_by_id("submit").submit()
        super(test_income_inquiry, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(test_income_inquiry, self).tearDown()

    def wait_css_class(self, selector):
        return self.selenium.find_element_by_css_selector(selector)

    def btn_submit(self,arg="submit-id-save"):
        return self.selenium.find_element_by_id(arg)

    def test_income_inquiry(self):
        #点击打开办公自动化
        self.selenium.find_element_by_id("check_work_click").click()
        time.sleep(2)
        #点击打开财务管理
        self.selenium.find_element_by_id("financial_management_click").click()
        time.sleep(5)
        #客户购买总列表
        self.wait_css_class("li.income_inquiry a").click()
        time.sleep(5)
        #根据客户姓名搜索
        self.selenium.find_element_by_xpath("//input[@name='customer_num']").send_keys("join")
        self.selenium.find_element_by_class_name("btn-submit").click()
        time.sleep(5)
        #查看客户购买详细信息
        self.selenium.find_element_by_class_name("customer_check").click()
        time.sleep(20)
'''


















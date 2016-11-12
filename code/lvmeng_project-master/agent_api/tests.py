#! /usr/bin/env python
#coding:utf-8
import datetime
import functools
import sys

from django.test import TestCase
from django.core.management import call_command
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from api.models import *
from agent_api.models import *
from erp.models import *

# Create your tests here.
'''
所有测试帐号密码为12345678
'''


def create_data():
    #python manage.py dumpdata --exclude=contenttypes --exclude=auth.Permission > api_test_data.json
    # call_command("loaddata --clobber", "api_test_data.json")
    call_command("loaddata", "api_test_data.json")


class login(object):

    def __init__(self, Case, user_id=4):
        self.Case = Case
        user = User.objects.get(id=user_id)
        token, create = Token.objects.get_or_create(user=user)
        self.Case.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def __enter__(self):
        pass

    def __exit__(self, *args):
        self.Case.client.credentials()


def error(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        try:
            return f(*args, **kw)
        except Exception, err:
            print args[0].__class__.__name__ + ' ' + f.__name__ + ' error.'
            s=sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1],s[2].tb_next.tb_lineno)
            # print err
            # print "on line " + str(s[2].tb_lineno)
    return wrapper


@error
def application(self, apply_url, data):
    create_data()

    with login(self):
        '''查看所有'''
        url = apply_url
        response = self.client.get(url)
        agent = Agent.objects.get(user=response.wsgi_request.user)
        user_id = agent.user.id
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for result in response.data["results"]:
            self.assertEqual(result["user"], user_id)

        '''新增'''
        url = '/agent_api/agents/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        examine_user = response.data[0]["user"]["id"]

        url = apply_url
        data = data
        data["examine_user"] = [examine_user]
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        if "start" in data and "end" in data:
            data["start"] = data["start"].replace("-", "/")
            data["end"] = data["end"].replace("-", "/")
        self.assertDictContainsSubset(data, response.data)

        '''查看对应id的申请详情'''
        id = response.data["id"]
        url = apply_url + str(id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], user_id)
        self.assertEqual(response.data["examine"][0]["examine_user"]["id"], examine_user)
        self.assertEqual(response.data["examine"][0]["read_status"], "1")
        self.assertEqual(response.data["examine"][0]["examine_status"], "3")

    with login(self, examine_user):
        '''查看审批'''
        object_id = response.data["examine"][0]["object_id"]
        examine_id = response.data["examine"][0]["id"]
        url = '/agent_api/examines/' + str(examine_id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["read_status"], "2")

        date = datetime.datetime.now()
        examine_time = date.strftime("%F %T")
        data = {
            "examine_status": "1",
            "examine_message": "xxx",
            "examine_time": examine_time,
            "object_id": object_id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    with login(self):
        '''查看对应id的申请详情'''
        url = apply_url + str(id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], user_id)
        data["examine_time"] = data["examine_time"].replace(" ", "T")
        self.assertDictContainsSubset(data, response.data["examine"][0])
        self.assertEqual(response.data["examine"][0]["examine_user"]["id"], examine_user)
        self.assertEqual(response.data["examine"][0]["read_status"], "2")

        '''删除'''
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    with login(self, examine_user):
        '''查看审批'''
        url = '/agent_api/examines/' + str(examine_id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


'''
版本更新测试
'''
class Test_AgentAPI_1_Version(APITestCase):


    @error
    def test_1_get_version(self):
        create_data()

        version = Agent_Version.objects.all()[0]
        url = '/agent_api/version/'
        data = {"version":"0.0.1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"url": version.url, "update": 1, "context": version.context})

        data = {"version":"10.0.1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"url": "", "update": 0, "context": ""})


'''
登录测试
'''
class Test_AgentAPI_2_Register(APITestCase):


    #登录测试
    @error
    def test_1_login(self):
        create_data()

        agent = Agent.objects.all()[0]
        username = agent.business.business_num + str(agent.agent_num)
        url = '/agent_api/api-token-auth/'
        data = {
            "username":username,
            "password":"12345678"
        }
        response = self.client.post(url, data)
        user = User.objects.get(username=username)
        token, create = Token.objects.get_or_create(user=user)
        token = token.key
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['token'], token)


'''
首页
'''
class Test_AgentAPI_3_Homepage(APITestCase):


    @error
    def test_1_homepage(self):
        create_data()

        with login(self):
            url = '/agent_api/homepage/'
            response = self.client.get(url)
            agent = Agent.objects.get(user=response.wsgi_request.user)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for announcement in response.data["announcements"]:
                self.assertEqual(announcement["announce_business"], agent.business.id)
            for product in response.data["products"]:
                self.assertEqual(product["business"], agent.business.id)
            for business in response.data["business"]:
                self.assertEqual(business["id"], agent.business.id)


'''
客户管理
'''
class Test_AgentAPI_4_Customer(APITestCase):


    #注册客户
    @error
    def test_1_customer(self):
        create_data()

        with login(self):
            '''查看所有客户'''
            url = '/agent_api/customers/'
            response = self.client.get(url)
            agent = Agent.objects.get(user=response.wsgi_request.user)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for customer in response.data["results"]:
                self.assertIn(agent.id, customer["agents"])
            customer_id = response.data["results"][0]["id"]

            '''查看单个客户'''
            url = '/agent_api/customers/' + str(customer_id) + '/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn(agent.id, response.data["agents"])

            '''通话记录'''
            url = '/agent_api/cell_records_customer/'
            date = datetime.datetime.now()
            start_time = date.strftime("%F %T")
            end_time = (date+datetime.timedelta(minutes=10)).strftime("%F %T")
            data = {
                "agent": agent.id,  #该理财师id
                "customer": customer_id, #用户id
                "start_time": start_time, #通话开始时间
                "end_time": end_time #通话结束时间
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            response = self.client.get(url)
            data["start_time"] = data["start_time"].replace(" ", "T")
            data["end_time"] = data["end_time"].replace(" ", "T")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertDictContainsSubset(data, response.data["results"][0])

            '''客户转移'''
            url = '/agent_api/agents/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            to_agent = response.data[0]["id"]
            to_agent_user = response.data[0]["user"]["id"]

            url = '/agent_api/customer_deliver/'
            data = {
                "agent_id": to_agent,
                "customer_id": customer_id
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status": 1, "message":"转移成功!"})

        with login(self, to_agent_user):
            url = '/agent_api/customers/' + str(customer_id) + '/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertNotIn(agent.id, response.data["agents"])
            self.assertIn(to_agent, response.data["agents"])


    #真实购买
    @error
    def test_2_realpurchase(self):
        create_data()

        with login(self):
            '''查看购买信息'''
            url = '/agent_api/customers/'
            response = self.client.get(url)
            agent = Agent.objects.get(user=response.wsgi_request.user)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for customer in response.data["results"]:
                self.assertIn(agent.id, customer["agents"])

            customer_id = response.data["results"][0]["id"]
            url = '/agent_api/real_purchases/?customer_id=' + str(customer_id)
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for purchase in response.data:
                self.assertEqual(purchase["real_agent"], agent.id)
                self.assertEqual(purchase["customer"], customer_id)
                self.assertEqual(purchase["business"], agent.business.id)

            '''添加购买'''
            url = '/agent_api/real_purchases/'
            date = datetime.datetime.now()
            income_date = date.strftime("%F")
            end_date = (date+datetime.timedelta(days=100)).strftime("%F")
            data = {
                "real_agent": agent.id, #所属理财师id
                "business": agent.business.id, #所属机构id
                "customer": customer_id, #客户id
                "product": Product.objects.filter(business=agent.business)[0].id, #产品id
                "amount": 1000000, #实收金额
                "income_date": income_date, #收款日期
                "end_date": end_date, #产品结束日期
                "pay_type": "1", #付款方式(('1',u'现金'),('2',u'汇票'),('3',u'支票'))
                "department": "", #部门
                "bill_number": "", #票据单号
                "brief": "", #简介
                "is_active": True #是否有效,一般为True
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            purchase_id=response.data["id"]

            url = '/agent_api/real_purchases/' + str(purchase_id) + '/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertDictContainsSubset(data, response.data)

            '''修改购买'''
            url = '/agent_api/real_purchases/' + str(purchase_id) + '/'
            data = {
                "real_agent": agent.id, #所属理财师id
                "business": agent.business.id, #所属机构id
                "customer": customer_id, #客户id
                "product": Product.objects.filter(business=agent.business)[0].id, #产品id
                "amount": 2000000, #实收金额
                "income_date": income_date, #收款日期
                "end_date": end_date, #产品结束日期
                "pay_type": "3", #付款方式(('1',u'现金'),('2',u'汇票'),('3',u'支票'))
                "department": "xxx", #部门
                "bill_number": "xxx", #票据单号
                "brief": "xxx", #简介
                "is_active": True #是否有效,一般为True
            }
            response = self.client.put(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertDictContainsSubset(data, response.data)

            '''删除购买'''
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    #意向客户
    @error
    def test_3_pcustomer(self):
        create_data()

        with login(self):
            '''查看所有客户'''
            url = '/agent_api/customer_pendings/'
            response = self.client.get(url)
            agent = Agent.objects.get(user=response.wsgi_request.user)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for pcustomer in response.data["results"]:
                self.assertIn(agent.id, pcustomer["agents"])
            pcustomer_id = response.data["results"][0]["id"]

            '''查看单个客户'''
            url = '/agent_api/customer_pendings/' + str(pcustomer_id) + '/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn(agent.id, response.data["agents"])

            '''通话记录'''
            url = '/agent_api/cell_records_pcustomer/'
            date = datetime.datetime.now()
            start_time = date.strftime("%F %T")
            end_time = (date+datetime.timedelta(minutes=10)).strftime("%F %T")
            data = {
                "agent": agent.id,  #该理财师id
                "customer": pcustomer_id, #用户id
                "start_time": start_time, #通话开始时间
                "end_time": end_time #通话结束时间
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            response = self.client.get(url)
            data["start_time"] = data["start_time"].replace(" ", "T")
            data["end_time"] = data["end_time"].replace(" ", "T")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertDictContainsSubset(data, response.data["results"][0])

            '''添加意向客户'''
            url = '/agent_api/customer_pendings/'
            data = {
                "name": u"xxx",
                "phoneNum": "13800138000"
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            pcustomer_id = response.data["id"]

            url = '/agent_api/customer_pendings/' + str(pcustomer_id) + '/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn(agent.id, response.data["agents"])
            self.assertDictContainsSubset(data, response.data)

            '''修改意向客户'''
            data = {
                "name": u"ooo",
                "phoneNum": "13800138000",
                "note": "xxx",
                "address": "xxx",
                "sex": "2",
            }
            response = self.client.put(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn(agent.id, response.data["agents"])
            self.assertDictContainsSubset(data, response.data)

            '''删除意向客户'''
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


'''
产品
'''
class Test_AgentAPI_5_Product(APITestCase):


    #获取产品信息
    @error
    def test_1_product(self):
        create_data()

        with login(self):
            url = '/agent_api/products/'
            response = self.client.get(url)
            agent = Agent.objects.get(user=response.wsgi_request.user)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for product in response.data:
                self.assertEqual(product["business"], agent.business.id)

            url = '/agent_api/products/' + str(response.data[0]["id"]) + '/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["business"], agent.business.id)


'''
个人中心
'''
class Test_AgentAPI_6_Personal(APITestCase):


    #信息修改
    @error
    def test_1_update(self):
        create_data()

        with login(self):
            '''基本信息修改'''
            url = '/agent_api/agent_update/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            data = {
                "name": "用户姓名",
                "sex": "2",
                "address": "88888888",
                "note": "xxx",
                "email": "xxx"
            }
            response = self.client.put(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status":1, "message":u"修改成功!"})
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertDictContainsSubset(data, response.data)


    #密码修改
    @error
    def test_2_password(self):
        create_data()

        with login(self):
            '''密码修改'''
            url = '/agent_api/password_change/'
            data = {
                "old_password": "12345678",
                "new_password1": "88888888",
                "new_password2": "88888888"
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {'password_change':1, 'message':"密码修改成功!"})

        agent = Agent.objects.get(user=response.wsgi_request.user)
        username = agent.business.business_num + str(agent.agent_num)
        url = '/agent_api/api-token-auth/'
        data = {
            "username":username,
            "password":"88888888"
        }
        response = self.client.post(url, data)
        user = User.objects.get(username=username)
        token, create = Token.objects.get_or_create(user=user)
        token = token.key
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['token'], token)


    #签到
    @error
    def test_3_checkin(self):
        create_data()

        with login(self):
            url = '/agent_api/checkins/'

            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            if response.data["checkin"]:
                points = response.data["checkin"]["points"]
            else:
                points = 0

            response = self.client.post(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["checkin"], 1)

            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["checkin"]["points"], points+1)
            self.assertEqual(response.data["checkin"]["continuous_days"], 1)

            response = self.client.post(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["checkin"], 0)


'''
OA
'''
class Test_AgentAPI_7_OA(APITestCase):


    #考勤
    @error
    def test_1_checkwork(self):
        create_data()

        with login(self):
            '''考勤'''
            #签到
            url = '/agent_api/checkwork/'
            data = {
                "abscissa": "111",
                "ordinate": "222",
                "address": "333",
                "area": "444"
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status":1, "message": u"更新成功!"})
            agent = Agent.objects.get(user=response.wsgi_request.user)
            checkwork = agent.user.checkwork
            data["type"] = '1'
            self.assertEqual(data, {
                "abscissa": checkwork.abscissa,
                "ordinate": checkwork.ordinate,
                "address": checkwork.address,
                "area": checkwork.area,
                "type": checkwork.type
            })

            #签退
            data = {
                "abscissa": "111",
                "ordinate": "222",
                "address": "333",
                "area": "444",
                "type": '0'
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status":1, "message": u"更新成功!"})
            agent = Agent.objects.get(user=response.wsgi_request.user)
            checkwork = agent.user.checkwork
            self.assertEqual(data, {
                "abscissa": checkwork.abscissa,
                "ordinate": checkwork.ordinate,
                "address": checkwork.address,
                "area": checkwork.area,
                "type": checkwork.type
            })

            '''考勤历史'''
            url = '/agent_api/checkwork_history/'
            response = self.client.get(url)
            agent = Agent.objects.get(user=response.wsgi_request.user)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertDictContainsSubset(data, response.data["results"][0])

            for result in response.data["results"]:
                self.assertEqual(result["check_history"], agent.user.id)
                self.assertEqual(result["check_business_history"], agent.business.id)


    #内部公告
    @error
    def test_2_internal_announcement(self):
        create_data()

        with login(self):
            url = '/agent_api/internal_announcement/'
            response = self.client.get(url)
            agent = Agent.objects.get(user=response.wsgi_request.user)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for result in response.data["results"]:
                self.assertEqual(result["announcement_business"], agent.business.id)
                self.assertEqual(result["read_status"], 0)
                url = '/agent_api/internal_announcement/' + str(result["id"]) + '/'
                response = self.client.get(url)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.data["read_status"], 1)


    #每日代办
    @error
    def test_3_dailytodo(self):
        create_data()

        with login(self):
            '''查看所有'''
            url = '/agent_api/daily_to_do/'
            response = self.client.get(url)
            agent = Agent.objects.get(user=response.wsgi_request.user)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for result in response.data["results"]:
                self.assertEqual(result["todo_user"], agent.user.id)

            '''新增'''
            date = datetime.datetime.now()
            to_do_time = date.strftime("%F %T")
            data = {
                "topic": "xxx",
                "content": "xxx",
                "remark": "xxx",
                "to_do_time": to_do_time
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            data["to_do_time"] = data["to_do_time"].replace(" ", "T")
            url = '/agent_api/daily_to_do/' + str(response.data["id"]) + '/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertDictContainsSubset(data, response.data)

            '''修改'''
            data = {
                "topic": "ooo",
                "content": "ooo",
                "remark": "ooo",
                "to_do_time": to_do_time
            }
            response = self.client.put(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            data["to_do_time"] = data["to_do_time"].replace(" ", "T")
            url = '/agent_api/daily_to_do/' + str(response.data["id"]) + '/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertDictContainsSubset(data, response.data)

            '''删除'''
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    #工作汇报
    @error
    def test_4_dailywork(self):
        url = '/agent_api/daily_work/'
        data = {
            "examine_user": [],
            "topic": "xxx",
            "content": "xxx",
            "work_type": "1"
        }
        application(self, url, data)


    #费用申请
    @error
    def test_5_cost_application(self):
        url = '/agent_api/cost_application/'
        data = {
            "examine_user": [],
            "topic": "xxx",
            "content": "xxx",
            "cost": 1000
        }
        application(self, url, data)


    #请假申请
    @error
    def test_6_leave_management(self):
        url = '/agent_api/leave_management/'
        date = datetime.datetime.now()
        start = date.strftime("%F")
        end = (date + datetime.timedelta(days=3)).strftime("%F")
        data = {
            "examine_user": [],
            "topic": "xxx",
            "content": "xxx",
            "start": start,
            "end": end
        }
        application(self, url, data)


    #出差申请
    @error
    def test_7_travel_apply(self):
        url = '/agent_api/travel_apply/'
        date = datetime.datetime.now()
        start = date.strftime("%F")
        end = (date + datetime.timedelta(days=3)).strftime("%F")
        data = {
            "examine_user": [],
            "topic": "xxx",
            "content": "xxx",
            "start": start,
            "end": end,
            "cost": 3000
        }
        application(self, url, data)


    #所有申请列表
    @error
    def test_8_apply(self):
        create_data()

        with login(self):
            url = '/agent_api/applications/'
            response = self.client.get(url)
            agent = Agent.objects.get(user=response.wsgi_request.user)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for result in response.data["results"]:
                self.assertEqual(result["application"]["user"]["id"], agent.user.id)


    #所有审批列表
    @error
    def test_9_examine(self):
        create_data()

        with login(self):
            url = '/agent_api/examines/'
            response = self.client.get(url)
            agent = Agent.objects.get(user=response.wsgi_request.user)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for result in response.data["results"]:
                self.assertEqual(result["examine_user"], agent.user.id)


'''
新闻头条
'''
class Test_AgentAPI_8_Headline(APITestCase):


    #获取所有头条信息
    @error
    def test_1_allheadline(self):
        create_data()

        with login(self):
            url = '/agent_api/headlines/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for result in response.data["results"]:
                self.assertNotEqual(result["title"], None)
                self.assertNotIn("context", result)


    #获取单个头条信息详情
    @error
    def test_2_headlinedetail(self):
        create_data()

        with login(self):
            id = Headline.objects.all()[0].id
            url = '/agent_api/headlines_detail/' + str(id) + '/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["id"], id)
            self.assertNotEqual(response.data["title"], None)
            self.assertNotEqual(response.data["context"], None)
            self.assertNotEqual(response.data["comments"], None)


    #新闻评论点赞
    @error
    def test_3_headlinecomment(self):
        create_data()

        with login(self):
            '''评论'''
            id = Headline.objects.all()[0].id
            url = '/agent_api/comments/'
            data = {
                "headline": id,
                "content": "xxx"
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data["headline"], id)
            self.assertNotEqual(response.data["content"], None)
            comment_id = response.data["id"]

            '''点赞'''
            url += str(comment_id) + '/'
            response = self.client.put(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status": 1, "message": "点赞成功!"})
            response = self.client.put(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status": 0, "message": "已经赞过!"})
            user=response.wsgi_request.user
            comment = Comment.objects.get(id=comment_id)
            self.assertEqual([praise.id for praise in comment.praise.all()], [user.id])
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

    def __init__(self, Case, user_id=7):
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


'''
版本更新测试
'''
class Test_API_1_Version(APITestCase):


    @error
    def test_1_get_version(self):
        create_data()

        version = Version.objects.all()[0]
        url = '/api/version/'
        data = {"version":"0.0.1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"url": version.url, "update": 1, "context": version.context})

        data = {"version":"10.0.1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"url": "", "update": 0, "context": ""})


# class VericodeTests(APITestCase):
#     def test_create_vericode(self):
#         validSecond = ValidSecond(seconds=300)
#         validSecond.save()
#
#         url = '/api/verification/?phone_number=13520404512&purpose=register'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


'''
用户登录注册测试
'''
class Test_API_2_Register(APITestCase):


    #注册测试
    @error
    def test_1_register(self):
        create_data()

        now = datetime.datetime.now()
        code = VerificationCode(phoneNum='13812345678',code='123456',purpose='0',register_date=now)
        code.save()
        url = '/api/register/'
        data = {
            "name":"李志",
            "phoneNum":"13812345678",
            "invitation_code":"A00011",
            "verification_code":code.code,
            "password1":"13812345678",
            "password2":"13812345678"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], 1)

        customer = Customer.objects.get(phoneNum=data["phoneNum"], customer_type='1')
        with login(self, customer.user.id):
            url = '/api/checkins/'
            response = self.client.get(url)
            points = Point.objects.get(type='0').points
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["checkin"]["points"], points)



    #登录测试
    @error
    def test_2_login(self):
        create_data()

        url = '/api/api-token-auth/'
        data = {
            "username":"13612345678",
            "password":"12345678"
        }
        response = self.client.post(url, data)
        user = User.objects.get(username=data['username'])
        token, create = Token.objects.get_or_create(user=user)
        token = token.key
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['token'], token)


    #忘记密码测试
    @error
    def test_3_forgetpassword(self):
        create_data()

        now = datetime.datetime.now()
        code = VerificationCode(phoneNum='13612345678',code='123456',purpose='1',register_date=now)
        code.save()
        url = '/api/forget_password/'
        data = {
            "phoneNum":"13612345678",
            "verification_code":code.code,
            "password1":"12345678",
            "password2":"12345678"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], 1)


'''
首页
'''
class Test_API_3_Homepage(APITestCase):


    @error
    def test_1_homepage(self):
        create_data()

        with login(self):
            url = '/api/homepage/?business_id=2'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for announcement in response.data["announcements"]:
                self.assertEqual(announcement["announce_business"], 2)
            for product in response.data["products"]:
                self.assertEqual(product["business"], 2)

            url = '/api/homepage/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for announcement in response.data["announcements"]:
                self.assertEqual(announcement["announce_business"], 1)
            for product in response.data["products"]:
                self.assertEqual(product["business"], 1)


'''
产品
'''
class Test_API_4_Product(APITestCase):


    #获取产品信息
    @error
    def test_1_product(self):
        create_data()

        with login(self):
            url = '/api/products/?business_id=2'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for product in response.data:
                self.assertEqual(product["business"], 2)

            url = '/api/products/?business_id=1'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for product in response.data:
                self.assertEqual(product["business"], 1)


    #产品收藏
    @error
    def test_2_collection(self):
        create_data()

        with login(self):
            url = '/api/collections/'
            data = {
                "customer":None,
                "product":1
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            id = response.data["id"]

            url = '/api/collections/' + str(id) + '/'
            data = {
                "customer":None,
                "product":2
            }
            response = self.client.put(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            url = '/api/collections/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for collection in response.data:
                self.assertEqual(collection["customer"], 1)
                self.assertEqual(collection["product"], 1)
            id = response.data[0]["id"]

            url = '/api/collections/' + str(id) + '/'
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            url = '/api/collections/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 0)


    #产品关注
    @error
    def test_3_attention(self):
        create_data()

        with login(self):
            url = '/api/attentions/'
            data = {
                "customer":None,
                "product":1
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            id = response.data["id"]

            url = '/api/attentions/' + str(id) + '/'
            data = {
                "customer":None,
                "product":2
            }
            response = self.client.put(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            url = '/api/attentions/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            for collection in response.data:
                self.assertEqual(collection["customer"], 1)
                self.assertEqual(collection["product"], 1)
            id = response.data[0]["id"]

            url = '/api/attentions/' + str(id) + '/'
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            url = '/api/attentions/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 0)


'''
新闻头条
'''
class Test_API_5_Headline(APITestCase):


    #获取所有头条信息
    @error
    def test_1_allheadline(self):
        create_data()

        with login(self):
            url = '/api/headlines/'
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
            url = '/api/headlines_detail/' + str(id) + '/'
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
            url = '/api/comments/'
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


'''
个人中心
'''
class Test_API_6_Personal(APITestCase):


    #签到
    @error
    def test_1_checkin(self):
        create_data()

        with login(self):
            url = '/api/checkins/'

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


    #购买
    @error
    def test_2_purchase(self):
        create_data()

        with login(self):
            '''添加购买'''
            #获取机构
            url = '/api/business/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            business_id = response.data[0]["id"]

            #获取产品
            url = '/api/products/?business_id=' + str(business_id)
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            product_id = response.data[0]["id"]

            #添加购买
            user = response.wsgi_request.user
            customer = Customer.objects.get(user=user)
            amount = 1000000
            start_date = datetime.datetime.now()
            end_date = (start_date + datetime.timedelta(days=100)).strftime("%F")
            start_date = start_date.strftime("%F")
            data = {
                "customer": customer.id,
                "product": product_id,
                "amount": amount,
                "start_date": start_date,
                "end_date": end_date
            }
            url = '/api/purchases/'
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            '''获取购买信息'''
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data[0]["product"], product_id)
            self.assertEqual(response.data[0]["customer"], customer.id)
            self.assertEqual(response.data[0]["start_date"], start_date.replace('-', '/'))
            self.assertEqual(response.data[0]["end_date"], end_date.replace('-', '/'))
            self.assertEqual(response.data[0]["amount"], amount)

            '''修改购买信息'''
            purcharse_id = response.data[0]["id"]
            url = '/api/purchases/' + str(purcharse_id) + '/'
            amount = 2000000
            start_date = datetime.datetime.now()
            end_date = (start_date + datetime.timedelta(days=200)).strftime("%F")
            start_date = start_date.strftime("%F")
            data = {
                "customer": customer.id,
                "product": product_id,
                "amount": amount,
                "start_date": start_date,
                "end_date": end_date
            }
            response = self.client.put(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["product"], product_id)
            self.assertEqual(response.data["customer"], customer.id)
            self.assertEqual(response.data["start_date"], start_date.replace('-', '/'))
            self.assertEqual(response.data["end_date"], end_date.replace('-', '/'))
            self.assertEqual(response.data["amount"], amount)

            '''删除购买'''
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            url = '/api/purchases/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, [])


    #机构管理
    @error
    def test_3_business(self):
        create_data()

        with login(self):
            #查看关联的客户经理
            url = '/api/agents/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 2)

            agent0 = response.data[0]
            agent1 = response.data[1]
            business = Business.objects.get(id=agent0["business"])
            invitation_code = business.business_num + str(agent0["agent_num"])

            #删除机构
            url = '/api/delete_agent/'
            data = {
                "business_id": business.id
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status":1, "message":u'机构删除成功!'})

            data = {
                "business_id": agent1["business"]
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status": 0, "message": u"用户至少需要保留一个机构,谢谢!"})

            url = '/api/agents/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0], agent1)

            #添加机构
            url = '/api/invitation_detail/?invitation_code=' + invitation_code
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["status"], 1)
            self.assertEqual(response.data["message"]["agent"]["id"], agent0["id"])
            self.assertEqual(response.data["message"]["business"]["id"], business.id)

            url = '/api/add_agent/'
            data = {
                "agent_id": agent0["id"]
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status":1, "message":u'机构添加成功!'})

            url = '/api/agents/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 2)
            self.assertIn(agent0, response.data)
            self.assertIn(agent1, response.data)


    #信息修改
    @error
    def test_4_update(self):
        create_data()
        risk_preference = {
            '1': u'极低风险型',
            '2': u'极低风险型',
            '3': u'较低风险型',
            '4': u'中等风险型',
            '5': u'较高风险型',
            '6': u'高风险型'
        }

        with login(self):
            '''基本信息修改'''
            url = '/api/customer_update/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            data = {
                "name": "用户姓名",
                "sex": "2",
                "address": "88888888",
                "note": "xxx",
                "industry": "xxx",
                "city": "xxx",
                "company": "xxx",
                "risk_preference": '3'
            }
            response = self.client.put(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status":1,"message":u"修改成功!"})
            response = self.client.get(url)
            response_data = {
                "name": response.data["name"],
                "sex": response.data["sex"],
                "address": response.data["address"],
                "note": response.data["note"],
                "industry": response.data["industry"],
                "city": response.data["city"],
                "company": response.data["company"],
                "risk_preference": response.data["risk_preference"]
            }
            data["risk_preference"] = risk_preference[data["risk_preference"]]
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response_data, data)

            '''身份认证'''
            url = '/api/checkins/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            if response.data["checkin"]:
                points = response.data["checkin"]["points"]
            else:
                points = 0

            url = '/api/idcard_update/'
            data = {
                "idCard_num": "411500199403152275"
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status":1,"message":u"身份认证成功!"})

            url = '/api/customer_update/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["idCard_num"], data["idCard_num"])

            url = '/api/checkins/'
            response = self.client.get(url)
            add_point = Point.objects.get(type='1').points
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["checkin"]["points"], points+add_point)

            '''邮箱认证'''
            url = '/api/checkins/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            if response.data["checkin"]:
                points = response.data["checkin"]["points"]
            else:
                points = 0

            code = EmailCode(email='niujidui@niujidui.com', code='123456', register_date=datetime.datetime.now())
            code.save()
            url = '/api/email_update/'
            data = {
                "email": "niujidui@niujidui.com",
                "code": code.code
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status":1,"message":u"认证成功!"})

            url = '/api/customer_update/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["email"], data["email"])

            url = '/api/checkins/'
            response = self.client.get(url)
            add_point = Point.objects.get(type='2').points
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["checkin"]["points"], points+add_point)

            '''手机号修改'''
            code = VerificationCode(phoneNum='13812345678',code='123456',purpose='2',register_date=datetime.datetime.now())
            code.save()
            url = '/api/phone_update/'
            data = {
                "phoneNum": "13812345678",
                "code":code.code
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {"status":1,"message":u"修改成功!"})

            url = '/api/customer_update/'
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["phoneNum"], data["phoneNum"])
            self.assertEqual(response.wsgi_request.user.username, data["phoneNum"])

    #密码修改
    @error
    def test_5_password(self):
        create_data()

        with login(self):
            '''密码修改'''
            url = '/api/password_change/'
            data = {
                "old_password": "12345678",
                "new_password1": "88888888",
                "new_password2": "88888888"
            }
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, {'password_change':1, 'message':"密码修改成功!"})

        customer = Customer.objects.get(user=response.wsgi_request.user)
        username = customer.phoneNum
        url = '/api/api-token-auth/'
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
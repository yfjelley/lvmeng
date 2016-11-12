#! /usr/bin/env python
#coding:utf-8
__author__ = 'jiechaoli'
import datetime

from django.db.models.fields import DateField
from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from erp.models import *
from api.models import *
from lvmeng.settings import PRODUCT_LINK, NEWS_LINK


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 200

# serialize user model to get firstname for agents and customers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Type
        fields = ['typeName']

class ProductSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer()
    risk_preference = serializers.SerializerMethodField()#风险偏好直接显示文字
    product_link = serializers.SerializerMethodField()#产品的mobi链接
    class Meta:
        model = Product
        # fields = ['name','chinese_name','bid','offer','change','multiply_factor']

    def get_risk_preference(self, obj):
        return obj.get_risk_preference_display()

    def get_product_link(self, obj):
        return PRODUCT_LINK + str(obj.id)

class AgentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    business_name = serializers.SerializerMethodField()
    class Meta:
        model = Agent
        # fields = ['epic_name','update_time','bid','offer','change']

    def get_business_name(self, obj):
        return obj.business.name

class BusinessSerializer(serializers.ModelSerializer):
    agent_phoneNum = serializers.SerializerMethodField()

    class Meta:
        model = Business
        exclude = ('business_license_original', 'business_license_copy', 'idCard_positive', 'idCard_negative')

    def get_agent_phoneNum(self, obj):
        try:
            agent = Agent.objects.get(business=obj, customer=Customer.objects.get(user=self.context['request'].user))
            return agent.phoneNum
        except Agent.DoesNotExist:
            return None

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    calling_card = serializers.SerializerMethodField()
    continuous_days = serializers.SerializerMethodField()
    risk_preference = serializers.SerializerMethodField()#风险偏好直接显示文字
    class Meta:
        model = Customer

    def get_calling_card(self, obj):
        if obj.calling_card:
            return self.context['request'].build_absolute_uri(obj.calling_card.url)
        return ""

    def get_continuous_days(self, obj):
        #返回连续签到天数
        try:
            checkin = Checkin.objects.get(customer=obj)
            return checkin.continuous_days
        except:
            return 0

    def get_risk_preference(self,obj):
        return obj.get_risk_preference_display()

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version

class AnnouncementSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Announcement

    def get_picture(self, obj):
        if obj.picture:
            return self.context['request'].build_absolute_uri(obj.picture.url)
        return ""

class HeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        exclude = ('context',)

class HeadlineDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()#评论
    mobi_link = serializers.SerializerMethodField()#新闻的mobi链接
    class Meta:
        model = Headline

    def get_comments(self,obj):
        comments = Comment.objects.filter(headline=obj, is_valid=True)
        return CommentSerializer(comments, context=self.context, many=True).data

    def get_mobi_link(self, obj):
        return NEWS_LINK + str(obj.id)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Comment

    def get_user(self,obj):
        customer = Customer.objects.filter(user=obj.user)
        agent = Agent.objects.filter(user=obj.user)
        if customer and customer[0].portrait:
            avatar = self.context['request'].build_absolute_uri(customer[0].portrait.url)
        elif agent and agent[0].avatar:
            avatar = self.context['request'].build_absolute_uri(agent[0].avatar.url)
        else:
            avatar = ""
        return {"id":obj.user.id, "name":obj.user.first_name, "avatar":avatar}


class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin

class PurchaseSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    return_expected = serializers.SerializerMethodField()
    start_date = serializers.DateField(format="%Y/%m/%d", input_formats=["%Y/%m/%d", "%Y-%m-%d"])
    end_date = serializers.DateField(format="%Y/%m/%d", input_formats=["%Y/%m/%d", "%Y-%m-%d"])

    class Meta:
        model = Purchase

    def get_product_name(self, obj):
        if obj.product:
            return obj.product.abbreviation
        return ""

    def get_return_expected(self, obj):
        if obj.product:
            return obj.product.return_expected
        return ""

class CollectionSerializer(serializers.ModelSerializer):
    product_detail = serializers.SerializerMethodField()
    class Meta:
        model = Collection

    def get_product_detail(self, obj):
        if obj.product:
            return ProductSerializer(obj.product).data
        return ""

class AttentionSerializer(serializers.ModelSerializer):
    product_detail = serializers.SerializerMethodField()
    class Meta:
        model = Attention

    def get_product_detail(self, obj):
        if obj.product:
            return ProductSerializer(obj.product).data
        return ""
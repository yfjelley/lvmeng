#! /usr/bin/env python
#coding:utf-8
__author__ = 'lizhi'
from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from django.contrib.contenttypes.models import ContentType

from erp.models import *
from api.models import *
from oa.models import *
from .models import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 200

class TenResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 200

# serialize user model to get firstname for agents and customers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id']

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


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ['name', 'department']


class AgentSimpleSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    user = UserSerializer()
    class Meta:
        model = Agent
        exclude = ('permissions', 'idCard_num')
        # fields = ['name', 'position', 'phoneNum', 'email', 'avatar']


class AgentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    avatar = serializers.SerializerMethodField()
    agent_url = serializers.SerializerMethodField()
    position = PositionSerializer()
    class Meta:
        model = Agent
        # exclude = ('permissions', 'idCard_num')
        # fields = ['epic_name','update_time','bid','offer','change']

    def get_avatar(self, obj):
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        return ""

    def get_agent_url(self, obj):
        invitation_code = obj.business.business_num + str(obj.agent_num)
        return 'http://' + self.context["request"].get_host() + '/api/url_agent/?invitation_code=' + invitation_code

class BusinessSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    class Meta:
        model = Business
        exclude = ('business_license_original', 'business_license_copy', 'idCard_positive', 'idCard_negative')

    def get_logo(self, obj):
        if obj.logo:
            return self.context['request'].build_absolute_uri(obj.logo.url)
        return ""

class CustomerSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # purchases_count = serializers.SerializerMethodField()
    # purchases_amounts = serializers.SerializerMethodField()
    real_purchases_count = serializers.SerializerMethodField()
    real_purchases_amounts = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        # exclude = ('agents', 'user')

    # def get_purchases_count(self, obj):
    #     return Purchase.objects.filter(customer=obj).count()
    #
    # def get_purchases_amounts(self, obj):
    #     purchases = Purchase.objects.filter(customer=obj)
    #     amounts = 0
    #     for purchase in purchases:
    #         amounts += purchase.amount
    #     return amounts

    def get_real_purchases_count(self, obj):
        return Real_purchase.objects.filter(customer=obj, real_agent__user=self.context["request"].user).count()

    def get_real_purchases_amounts(self, obj):
        real_purchases = Real_purchase.objects.filter(customer=obj, real_agent__user=self.context["request"].user)
        amounts = 0
        for real_purchase in real_purchases:
            amounts += real_purchase.amount
        return amounts


class AddressCustomerSerializer(serializers.ModelSerializer):
    customer_type = serializers.SerializerMethodField()
    real_purchases_count = serializers.SerializerMethodField()
    real_purchases_amounts = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id', 'portrait', 'name', 'phoneNum', 'sex', 'address', 'customer_type', 'real_purchases_count', 'real_purchases_amounts', 'note']

    def get_customer_type(self, obj):
        return obj.get_customer_type_display()

    def get_real_purchases_count(self, obj):
        return Real_purchase.objects.filter(customer=obj, real_agent__user=self.context["request"].user).count()

    def get_real_purchases_amounts(self, obj):
        real_purchases = Real_purchase.objects.filter(customer=obj, real_agent__user=self.context["request"].user)
        amounts = 0
        for real_purchase in real_purchases:
            amounts += real_purchase.amount
        return amounts


class AnnouncementSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Announcement

    def get_picture(self, obj):
        if obj.picture:
            return self.context['request'].build_absolute_uri(obj.picture.url)
        return ""

class PurchaseSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    product_id = serializers.SerializerMethodField()
    class Meta:
        model = Purchase

    def get_product(self, obj):
        if obj.product:
            return obj.product.abbreviation
        return ""

    def get_product_id(self, obj):
        if obj.product:
            return obj.product.id
        return ""

class RealPurchaseSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    class Meta:
        model = Real_purchase

    def get_product_name(self, obj):
        if obj.product:
            return obj.product.abbreviation
        return ""

class CheckWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckWork

class CheckWorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckWork_history

class CheckWorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check_Time_Setting
        exclude = ('business', )


class InternalAnnouncementSerializer(serializers.ModelSerializer):
    read_status = serializers.SerializerMethodField()
    class Meta:
        model = Internal_announcement

    def get_read_status(self, obj):
        read = Read_message.objects.filter(read_user=self.context['request'].user, model_name="internal_announcement", record_id=obj.id)
        if read:
            return 1
        return 0

"""
申请和审批API,其中基础审批和基础申请只是获取数据的时候用到,
把对应用户名的id改为id和姓名,申请包含了申请以及所关联的所有审批,
审批包含了自己的审批以及关联的申请以及该申请关联的其他所有审批.
"""
class BaseAgentSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = Agent
        fields = ['avatar', 'sex']

    def get_avatar(self, obj):
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        return ""


#获取不同类型的基础申请
def get_application_serializer(self, obj):
        name = obj.__class__.__name__.lower()
        if name=="cost_application":
            return GetCostApplicationSerializer(obj, context=self.context).data
        elif name=="leave_management":
            return GetLeaveManagementSerializer(obj, context=self.context).data
        elif name=="travel_apply":
            return GetTravelApplySerializer(obj, context=self.context).data
        elif name=="daily_work":
            return GetDailyWorkSerializer(obj, context=self.context).data
        else:
            return None

#所有的基础审批
class GetExamineSerializer(serializers.ModelSerializer):
    examine_user = serializers.SerializerMethodField()
    class Meta:
        model = All_Examine

    def get_examine_user(self, obj):
        if obj.examine_user:
            examine_user={
                "id": obj.examine_user.id,
                "name": obj.examine_user.first_name,
                "agent": BaseAgentSerializer(Agent.objects.get(user=obj.examine_user), context=self.context).data
            }
            return examine_user
        return ""

#所有的审批
class ExamineSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    examine = serializers.SerializerMethodField()
    application = serializers.SerializerMethodField()
    class Meta:
        model = All_Examine

    def get_type(self, obj):
        name = obj.examine.__class__.__name__.lower()
        return name
        # if name=="cost_application":
        #     return "cost"
        # elif name=="leave_management":
        #     return "leave"
        # elif name=="travel_apply":
        #     return "travel"
        # else:
        #     return None

    def get_examine(self, obj):
        try:
            contenttype_obj = ContentType.objects.get_for_model(obj.examine)
            examine = All_Examine.objects.filter(object_id=obj.examine.id, content_type=contenttype_obj).exclude(id=obj.id)
            return GetExamineSerializer(examine, many=True, context=self.context).data
        except:
            return ""

    def get_application(self, obj):
        return get_application_serializer(self, obj.examine)

#所有申请
class ApplicationSerializer(serializers.Serializer):
    type = serializers.SerializerMethodField()
    application = serializers.SerializerMethodField()

    def get_type(self, obj):
        name = obj.__class__.__name__.lower()
        return name

    def get_application(self, obj):
        return get_application_serializer(self, obj)

#获取用户信息,包括对应员工的性别和头像
class GetUser(object):
    def get_user(self, obj):
        if Agent.objects.filter(user=obj.user):
            user={
                "id": obj.user.id,
                "name": obj.user.first_name,
                "agent": BaseAgentSerializer(Agent.objects.get(user=obj.user), context=self.context).data
            }
            return user
        return ""

#基础工作日报
class GetDailyWorkSerializer(GetUser, serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Daily_work


#工作日报
class DailyWorkSerializer(serializers.ModelSerializer):
    examine = serializers.SerializerMethodField()
    class Meta:
        model = Daily_work

    def get_examine(self, obj):
        contenttype_obj = ContentType.objects.get_for_model(obj)
        cost_examine = All_Examine.objects.filter(object_id=obj.id, content_type=contenttype_obj)
        return GetExamineSerializer(cost_examine, many=True, context=self.context).data

# #基础费用审批
# class GetCostExamineSerializer(serializers.ModelSerializer):
#     examine_user = serializers.SerializerMethodField()
#     class Meta:
#         model = Cost_examine
#     def get_examine_user(self, obj):
#         examine_user={"id":obj.examine_user.id, "name":obj.examine_user.first_name}
#         return examine_user
#基础费用申请
class GetCostApplicationSerializer(GetUser, serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Cost_application

#费用申请
class CostApplicationSerializer(serializers.ModelSerializer):
    examine = serializers.SerializerMethodField()
    class Meta:
        model = Cost_application
    def get_examine(self, obj):
        contenttype_obj = ContentType.objects.get_for_model(obj)
        cost_examine = All_Examine.objects.filter(object_id=obj.id, content_type=contenttype_obj)
        return GetExamineSerializer(cost_examine, many=True, context=self.context).data
# #费用审批
# class CostExamineSerializer(serializers.ModelSerializer):
#     cost_examine = serializers.SerializerMethodField()
#     cost_application = serializers.SerializerMethodField()
#     class Meta:
#         model = Cost_examine
#     def get_cost_examine(self, obj):
#         cost_examine = Cost_examine.objects.filter(cost_examine=obj.cost_examine).exclude(id=obj.id)
#         return GetCostExamineSerializer(cost_examine, many=True).data
#     def get_cost_application(self, obj):
#         return GetCostApplicationSerializer(obj.cost_examine).data


# #基础请假审批
# class GetLeaveExamineSerializer(serializers.ModelSerializer):
#     examine_user = serializers.SerializerMethodField()
#     class Meta:
#         model = Leave_examine
#     def get_examine_user(self, obj):
#         examine_user={"id":obj.examine_user.id, "name":obj.examine_user.first_name}
#         return examine_user
#基础请假申请
class GetLeaveManagementSerializer(GetUser, serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Leave_management

#请假申请
class LeaveManagementSerializer(serializers.ModelSerializer):
    examine = serializers.SerializerMethodField()
    start = serializers.DateField(format="%Y/%m/%d", input_formats=["%Y/%m/%d", "%Y-%m-%d"])
    end = serializers.DateField(format="%Y/%m/%d", input_formats=["%Y/%m/%d", "%Y-%m-%d"])
    class Meta:
        model = Leave_management
    def get_examine(self, obj):
        contenttype_obj = ContentType.objects.get_for_model(obj)
        leave_examine = All_Examine.objects.filter(object_id=obj.id, content_type=contenttype_obj)
        return GetExamineSerializer(leave_examine, many=True, context=self.context).data
# #请假审批
# class LeaveExamineSerializer(serializers.ModelSerializer):
#     leave_examine = serializers.SerializerMethodField()
#     leave_management = serializers.SerializerMethodField()
#     class Meta:
#         model = Leave_examine
#     def get_leave_examine(self, obj):
#         leave_examine = Leave_examine.objects.filter(leave_examine=obj.leave_examine).exclude(id=obj.id)
#         return GetLeaveExamineSerializer(leave_examine, many=True).data
#     def get_leave_management(self, obj):
#         return GetLeaveManagementSerializer(obj.leave_examine).data

# #基础出差审批
# class GetTravelExamineSerializer(serializers.ModelSerializer):
#     examine_user = serializers.SerializerMethodField()
#     class Meta:
#         model = Travel_examine
#     def get_examine_user(self, obj):
#         examine_user={"id":obj.examine_user.id, "name":obj.examine_user.first_name}
#         return examine_user
#基础出差申请
class GetTravelApplySerializer(GetUser, serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Travel_apply

#出差申请
class TravelApplySerializer(serializers.ModelSerializer):
    examine = serializers.SerializerMethodField()
    start = serializers.DateField(format="%Y/%m/%d", input_formats=["%Y/%m/%d", "%Y-%m-%d"])
    end = serializers.DateField(format="%Y/%m/%d", input_formats=["%Y/%m/%d", "%Y-%m-%d"])
    class Meta:
        model = Travel_apply
    def get_examine(self, obj):
        contenttype_obj = ContentType.objects.get_for_model(obj)
        travel_examine = All_Examine.objects.filter(object_id=obj.id, content_type=contenttype_obj)
        return GetExamineSerializer(travel_examine, many=True, context=self.context).data
# #出差审批
# class TravelExamineSerializer(serializers.ModelSerializer):
#     travel_examine = serializers.SerializerMethodField()
#     travel_apply = serializers.SerializerMethodField()
#     class Meta:
#         model = Travel_examine
#     def get_travel_examine(self, obj):
#         travel_examine = Travel_examine.objects.filter(travel_examine=obj.travel_examine).exclude(id=obj.id)
#         return GetTravelExamineSerializer(travel_examine, many=True).data
#     def get_travel_apply(self, obj):
#         return GetTravelApplySerializer(obj.travel_examine).data

# #获取所有审批
# class ExamineSerializer(serializers.Serializer):
#     type = serializers.SerializerMethodField()
#     examine = serializers.SerializerMethodField()
#
#     def get_type(self, obj):
#         name = obj.__class__.__name__.lower()
#         if name=="cost_examine":
#             return "cost"
#         elif name=="leave_examine":
#             return "leave"
#         elif name=="travel_examine":
#             return "travel"
#         else:
#             return None
#
#     def get_examine(self, obj):
#         name = obj.__class__.__name__.lower()
#         if name=="cost_examine":
#             return CostExamineSerializer(obj).data
#         elif name=="leave_examine":
#             return LeaveExamineSerializer(obj).data
#         elif name=="travel_examine":
#             return TravelExamineSerializer(obj).data
#         else:
#             return None


class AgentVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent_Version

# class CustomerPendingSerializer(serializers.ModelSerializer):
#     real_purchases_count = serializers.SerializerMethodField()
#     real_purchases_amounts = serializers.SerializerMethodField()
#     products = serializers.SerializerMethodField()
#     class Meta:
#         model = Customer_Pending
#
#     def get_products(self, obj):
#         products = []
#         for product in obj.product_target.all():
#             products.append({"id": product.id, "name":product.abbreviation})
#         return products
#
#     def get_real_purchases_count(self, obj):
#         return Real_purchase.objects.filter(customer=obj, real_agent__user=self.context["request"].user).count()
#
#     def get_real_purchases_amounts(self, obj):
#         real_purchases = Real_purchase.objects.filter(customer=obj, real_agent__user=self.context["request"].user)
#         amounts = 0
#         for real_purchase in real_purchases:
#             amounts += real_purchase.amount
#         return amounts

class CellRecordsCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell_Records_Customer

class CellRecordsPCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell_Records_PCustomer

class DailyToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily_to_do

class TemporaryFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporary_File
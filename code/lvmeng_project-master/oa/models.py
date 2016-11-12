#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import datetime

from api.views import points_deal
from erp.models import *

import logging
logger = logging.getLogger(__name__)

# from push.views import push_to_ios, push_to_android

# Create your models here.
type = (('1',u'签到'),('0',u'签退'))
class CheckWork(models.Model):#考勤
    check_user = models.OneToOneField(User,verbose_name=u"关联用户")
    check_business = models.ForeignKey(Business,verbose_name=u"关联机构")
    type = models.CharField(choices=type, max_length=10, default="1", verbose_name=u"签到类型")
    abscissa = models.CharField(max_length=30,verbose_name=u"横坐标")#经度
    ordinate = models.CharField(max_length=30,verbose_name=u"纵坐标")#纬度
    address = models.CharField(max_length=300,null=True,blank=True,verbose_name=u"地址")
    area = models.CharField(max_length=300,null=True,blank=True,verbose_name=u"地区")
    check_time = models.DateTimeField(verbose_name=u"考勤时间")

    def __unicode__(self):
        return self.check_user.first_name

    # def toJSON(self):
    #     import json
    #     return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class CheckWork_history(models.Model):#考勤历史
    check_history = models.ForeignKey(User,verbose_name=u"关联用户")
    check_business_history = models.ForeignKey(Business,verbose_name=u"关联机构")
    type = models.CharField(choices=type, max_length=10, default="1", verbose_name=u"签到类型")
    abscissa = models.CharField(max_length=30,verbose_name=u"横坐标")
    ordinate = models.CharField(max_length=30,verbose_name=u"纵坐标")
    address = models.CharField(max_length=300,null=True,blank=True,verbose_name=u"地址")
    area = models.CharField(max_length=300,null=True,blank=True,verbose_name=u"地区")
    check_time = models.DateTimeField(verbose_name=u"考勤时间")
    # time_now = models.TimeField(null=True,blank=True,auto_now_add=True)

    def __unicode__(self):
        return self.check_history.first_name

top_choice = (('1',u'否'),('2',u'是'))
publish_choice = (('1',u'不发布'),('2',u'发布'))
class Internal_announcement(models.Model):#通知公告(员工)

    announcement_business = models.ForeignKey(Business,verbose_name=u"所属机构")
    topic = models.CharField(max_length=30,verbose_name=u"主题")

    on_top = models.CharField(choices=top_choice,max_length=1,default="1",verbose_name=u"是否置顶")
    onTop_start = models.DateField(null=True,blank=True,verbose_name=u"置顶开始时间")
    onTop_end = models.DateField(null=True,blank=True,verbose_name=u"置顶结束时间")
    publish = models.CharField(choices=publish_choice,default="1",max_length=1,verbose_name=u"是否发布")
    publish_start = models.DateField(null=True,blank=True,verbose_name=u"发布开始时间")
    publish_end = models.DateField(null=True,blank=True,verbose_name=u"发布结束时间")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)
    add_time = models.DateField(auto_now_add=True,verbose_name=u"添加时间")
    # content = models.TextField(max_length=300,verbose_name=u"通知内容")
    content = HTMLField(null=True,blank=True,verbose_name=u"通知内容")

    class Meta:
        ordering = ['-add_time']

daily_work_type = (('1',u'日报'),('2',u'周报'),('3',u'月报'))

class Daily_work(models.Model):#工作汇报
    business = models.ForeignKey(Business,verbose_name=u"所属机构",null=True,blank=True)
    user = models.ForeignKey(User,null=True,blank=True,verbose_name=u"填报人")
    examine_user = models.ManyToManyField(User,null=True,blank=True,verbose_name=u"审批人",related_name="daily_examine_user")
    topic = models.CharField(max_length=300,verbose_name=u"当天总结")
    content = models.CharField(max_length=300,verbose_name=u"明日计划")
    work_type = models.CharField(choices=daily_work_type,max_length=5,null=True,blank=True,default='1',verbose_name=u"工作汇报类型")
    time = models.DateTimeField(auto_now_add=True,verbose_name=u"填报时间")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)

    class Meta:
        ordering = ['-time']

read_status = (('1',u'未读'),('2',u'已读'))
class Cost_application(models.Model):#费用申请
    business = models.ForeignKey(Business,null=True,blank=True,verbose_name=u"所属机构")
    user = models.ForeignKey(User,null=True,blank=True,verbose_name=u"申请人")
    examine_user = models.ManyToManyField(User,null=True,blank=True,verbose_name=u"审批人",related_name="cost_examine_user")
    topic = models.CharField(max_length=20,verbose_name=u"申请条目")
    content = models.CharField(max_length=100,verbose_name=u"申请内容")
    cost = models.BigIntegerField(verbose_name=u"金额(元)")
    time = models.DateTimeField(auto_now_add=True,verbose_name=u"申请时间")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)

    class Meta:
        ordering = ['-time']


class Leave_management(models.Model):#请假管理
    business = models.ForeignKey(Business,null=True,blank=True,verbose_name=u"所属机构")
    user = models.ForeignKey(User,null=True,blank=True,verbose_name=u"请假人")
    examine_user = models.ManyToManyField(User,null=True,blank=True,verbose_name=u"审批人",related_name="leave_examine_user")
    topic = models.CharField(max_length=20,verbose_name=u"请假类型")
    content = models.CharField(max_length=100,verbose_name=u"请假原因")
    start = models.DateField(verbose_name=u"开始时间")
    end = models.DateField(verbose_name=u"结束时间")
    time = models.DateTimeField(auto_now_add=True,verbose_name=u"申请时间")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)

    class Meta:
        ordering = ['-time']

class Travel_apply(models.Model):#出差申请
    business = models.ForeignKey(Business,null=True,blank=True,verbose_name=u"所属机构")
    user = models.ForeignKey(User,null=True,blank=True,verbose_name=u"申请人")
    examine_user = models.ManyToManyField(User,null=True,blank=True,verbose_name=u"审批人",related_name="travel_examine_user")
    topic = models.CharField(max_length=30,verbose_name=u"出差事由")
    content = models.CharField(max_length=30,verbose_name=u"出差地点")
    cost = models.BigIntegerField(verbose_name=u"金额(元)")
    start = models.DateField(verbose_name=u"开始时间")
    end = models.DateField(verbose_name=u"结束时间")
    time = models.DateTimeField(auto_now_add=True,verbose_name=u"申请时间")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)

    class Meta:
        ordering = ['-time']

class Read_message(models.Model):

    read_business = models.ForeignKey(Business,null=True,blank=True,verbose_name=u"关联机构")
    read_user = models.ForeignKey(User,null=True,blank=True,verbose_name=u"已读用户")
    model_name = models.CharField(max_length=30,null=True,blank=True,verbose_name=u"模块名")
    record_id = models.IntegerField(null=True,blank=True,verbose_name=u"关联记录的ID")
    read_time = models.DateTimeField(auto_now_add=True,verbose_name=u"查看时间")

    def __unicode__(self):
        return self.record_id

examine_status = (('1',u'通过'),('2',u'驳回'),('3',u'待审核'))

class Examine(models.Model):#审批
    examine_business = models.ForeignKey(Business,null=True,blank=True,verbose_name=u"关联机构")
    examine_user = models.ForeignKey(User,null=True,blank=True,verbose_name=u"审批人")
    examine_status = models.CharField(choices=examine_status,default="3",max_length=1,verbose_name=u"审核结果选择")
    read_status = models.CharField(choices=read_status,default="1",max_length=1,verbose_name=u"读取状态")
    examine_message = models.TextField(null=True,blank=True,verbose_name=u"审批备注")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)
    examine_time = models.DateTimeField(null=True,blank=True,verbose_name=u"审批时间")

    class Meta:
        abstract = True

class Cost_examine(Examine):#费用申请审批
    cost_examine = models.ForeignKey(Cost_application,verbose_name=u"关联费用申请")

class Leave_examine(Examine):#请假管理申请审批
    leave_examine = models.ForeignKey(Leave_management,verbose_name=u"关联请假管理申请")

class Travel_examine(Examine):#出差申请审批
    travel_examine = models.ForeignKey(Travel_apply,verbose_name=u"关联出差申请")

class Daily_to_do(models.Model):#每日待办
    todo_user = models.ForeignKey(User,null=True,blank=True,verbose_name=u"待办人")
    topic = models.CharField(max_length=30,verbose_name=u"主题")
    content = models.CharField(max_length=100,verbose_name=u"事件")
    # remark = models.TextField(max_length=300,null=True,blank=True,verbose_name=u"备注")
    remark = HTMLField(null=True,blank=True,verbose_name=u"备注")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name=u"添加时间")
    to_do_time = models.DateTimeField(verbose_name=u"待办事时间")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)

    class Meta:
        ordering = ["to_do_time"]

''' 收款管理 '''

class All_Examine(models.Model):#审批
    content_type = models.ForeignKey(ContentType, related_name="content_type_timelines",null=True,blank=True)
    object_id = models.PositiveIntegerField()
    examine = GenericForeignKey('content_type', 'object_id',)
    examine_business = models.ForeignKey(Business,null=True,blank=True,verbose_name=u"关联机构")
    examine_user = models.ForeignKey(User,null=True,blank=True,verbose_name=u"审批人")
    examine_status = models.CharField(choices=examine_status,default="3",max_length=1,verbose_name=u"审核结果选择")
    read_status = models.CharField(choices=read_status,default="1",max_length=1,verbose_name=u"读取状态")
    examine_message = models.TextField(null=True,blank=True,verbose_name=u"审批备注")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)
    examine_time = models.DateTimeField(null=True,blank=True,verbose_name=u"审批时间")

    class Meta:
        ordering = ["read_status"]

    '''新建审批时推送到审批人,审批结束时推送到申请人'''
    def save(self, *args, **kwargs):
        is_new = False if self.pk else True
        super(All_Examine, self).save(*args, **kwargs)

        from push.views import push_to_ios, push_to_android
        try:
            application = self.examine
            application_type = self.application_type
            extras={
                    "content_type":'',
                    "applicant":self.application_model_name,
                    "application_id":self.examine.id,
                    "examine_id":self.id
            }
            if is_new:#是否新建
                message = u'%s提交了一个新的%s, 点击查看详情' % (self.examine.user.first_name, application_type)
                extras['content_type'] = 'examine'
                push_to_ios(user_list=[self.examine_user], message=message, extra=extras)
                push_to_android(user_list=[self.examine_user], message=message, extras=extras)
            elif '2'==self.read_status and '3'!=self.examine_status:#是否审核结束
                #添加积分
                points_deal(self.examine_user, '7')

                message = u'%s%s您的%s,点击查看详情' % (self.examine_user.first_name, self.get_examine_status_display(), application_type)
                extras['content_type'] = 'application'
                push_to_ios(user_list=[application.user], message=message, extra=extras)
                push_to_android(user_list=[application.user], message=message, extras=extras)
        except Exception, err:
            logger.error(err)

    '''获取申请的类型'''
    @property
    def application_type(self):
        name = self.examine.__class__.__name__.lower()
        if name=="cost_application":
            return u'费用申请'
        elif name=="leave_management":
            return u'请假申请'
        elif name=="travel_apply":
            return u'出差申请'
        elif name=="daily_work":
            return u'工作' + self.examine.get_work_type_display()
        else:
            return u'申请'

    '''获取申请的model name'''
    @property
    def application_model_name(self):
        return self.examine.__class__.__name__.lower()

#考勤时间设定
class Check_Time_Setting(models.Model):
    business = models.ForeignKey(Business,verbose_name=u"关联机构")
    check_in_time = models.TimeField(verbose_name=u"签到时间")
    check_out_time = models.TimeField(verbose_name=u"签退时间")
    check_in_remind = models.TimeField(verbose_name=u"签到提醒")
    check_out_remind = models.TimeField(verbose_name=u"签退提醒")





















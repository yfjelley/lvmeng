#coding:utf-8
from django.db import models

from erp.models import *


class Agent_Version(models.Model):#客户经理app版本号
    version = models.CharField(max_length=10,null=False,blank=False,verbose_name=u'版本号')
    url = models.URLField(verbose_name=u'下载链接')
    context = models.CharField(max_length=100,null=True,blank=True,verbose_name=u'版本信息')
    date = models.DateTimeField(blank=True, null=True, verbose_name=u"添加日期")

    def __unicode__(self):
        return self.version


class Cell_Records_Customer(models.Model):#客户经理和客户通话记录
    agent = models.ForeignKey(Agent, verbose_name=u'客户经理')
    customer = models.ForeignKey(Customer, verbose_name=u'客户')
    start_time = models.DateTimeField(verbose_name=u'通话开始时间')
    end_time = models.DateTimeField(verbose_name=u'通话结束时间')

    def __unicode__(self):
        return self.agent.name

    class Meta:
        ordering = ['-start_time']


class Cell_Records_PCustomer(models.Model):#客户经理和意向客户通话记录
    agent = models.ForeignKey(Agent, verbose_name=u'客户经理')
    customer = models.ForeignKey(Customer, verbose_name=u'客户')
    start_time = models.DateTimeField(verbose_name=u'通话开始时间')
    end_time = models.DateTimeField(verbose_name=u'通话结束时间')

    def __unicode__(self):
        return self.agent.name

    class Meta:
        ordering = ['-start_time']


class Temporary_File(models.Model):#临时文件
    file = models.FileField(upload_to='agent/temporary/', verbose_name=u'文件')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name=u'用户')
    upload_time = models.DateTimeField(verbose_name=u'上传时间', auto_now_add=True)

    class Meta:
        ordering = ['-upload_time']

#删除临时文件
def on_delete(sender, instance, **kwargs):
    instance.file.delete(save=False)

models.signals.post_delete.connect(on_delete, sender=Temporary_File)

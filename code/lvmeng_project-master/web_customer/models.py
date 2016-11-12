#coding:utf-8
from django.db import models
from tinymce.models import HTMLField
from erp.models import Business
from django.contrib.auth.models import User
# Create your models here.
class Lv_Announcement(models.Model):#律锰公告
    lv_picture = models.ImageField(upload_to='lvmeng/announcement/', verbose_name=u"机构公告图片(尺寸大小:375*106)", blank=True,null=True)
    title = models.CharField(max_length=30,verbose_name=u"标题")
    date = models.DateField(verbose_name=u"添加时间",auto_now_add=True)
    # text = models.TextField(max_length=3000,null=True,blank=True,verbose_name=u"内容说明")
    text = HTMLField(null=True,blank=True,verbose_name=u"内容说明")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)

''' 客户页面机构轮播图 '''
class business_carousel(models.Model):
    business = models.ForeignKey(Business,null=True,blank=True,verbose_name=u"所属机构")
    carousel = models.ImageField(upload_to='business/carousel/',null=True,blank=True,verbose_name=u"轮播图")
    add_user = models.ForeignKey(User,null=True,blank=True,verbose_name=u"添加人")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name=u"添加时间")

    class Meta:
        ordering = ["-add_time"]
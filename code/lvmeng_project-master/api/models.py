#coding:utf-8
from django.db import models

from erp.models import *
from tinymce.models import HTMLField

# Create your models here.
class Version(models.Model):#版本号
    version = models.CharField(max_length=10,null=False,blank=False,verbose_name=u'版本号')
    url = models.URLField(verbose_name=u'下载链接')
    context = models.CharField(max_length=100,null=True,blank=True,verbose_name=u'版本信息')
    date = models.DateTimeField(blank=True, null=True, verbose_name=u"添加日期")

    def __unicode__(self):
        return self.version


class Headline(models.Model):#金融头条,,按照时间排序
    add_date = models.DateField(blank=True, null=True, verbose_name=u"添加日期",auto_now_add=True)
    register_date = models.DateTimeField(blank=True, null=True, verbose_name=u"时间")
    title = models.CharField(max_length=30,null=False,blank=False, default='',verbose_name=u'标题',unique=True)
    picture = models.ImageField(upload_to='api/headlines/', verbose_name=u"简图", blank=True,null=True)
    # context = models.TextField(max_length=15000,null=True,blank=True,verbose_name=u'内容')
    context = HTMLField(null=True,blank=True,verbose_name=u'内容')
    url = models.URLField(null=True,blank=True,verbose_name=u'详情链接')
    read_num = models.PositiveIntegerField(null=True,blank=True,default=0,verbose_name=u"阅读次数")

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-register_date']

#删除新闻头条的图片
def on_delete(sender, instance, **kwargs):
    instance.picture.delete(save=False)

models.signals.post_delete.connect(on_delete, sender=Headline)


class Comment(models.Model): #金融头条评论
    headline = models.ForeignKey(Headline, verbose_name=u'新闻头条')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name=u'用户')
    praise = models.ManyToManyField(User, related_name="praise", null=True, blank=True, verbose_name=u'点赞')
    content = models.CharField(max_length=1000, verbose_name=u'评论内容')
    time = models.DateTimeField(auto_now_add=True, verbose_name=u'评论时间')
    is_valid = models.BooleanField(default=True, verbose_name=u'是否有效')

    class Meta:
        ordering = ['-time']


class History_Checkin(models.Model):#签到记录
    user = models.ForeignKey(User,null=True,blank=True,verbose_name=u'用户')
    register_date = models.DateField(blank=True, null=True, verbose_name=u"签到日期", auto_now_add=True)
    abscissa = models.CharField(max_length=30,verbose_name=u"横坐标")#经度
    ordinate = models.CharField(max_length=30,verbose_name=u"纵坐标")#纬度

    def __unicode__(self):
        return self.user.first_name

    class Meta:
        ordering = ['-register_date']


class Checkin(models.Model):#签到统计
    user = models.OneToOneField(User,null=True,blank=True,verbose_name=u'用户', unique=True)
    latest_date = models.DateField(blank=True, null=True, verbose_name=u"最后签到日期")
    points = models.PositiveIntegerField(blank=True, null=True, verbose_name=u"积分")
    continuous_days = models.PositiveIntegerField(blank=True, null=True, verbose_name=u"连续登录天数")
    abscissa = models.CharField(max_length=30,blank=True, null=True,verbose_name=u"横坐标")#经度
    ordinate = models.CharField(max_length=30,blank=True, null=True,verbose_name=u"纵坐标")#纬度

    def __unicode__(self):
        return self.user.first_name

    class Meta:
        ordering = ['-latest_date']


class ValidSecond(models.Model):#手机验证码有效时间
    seconds = models.IntegerField(blank=True, null=True, verbose_name=u"验证码有效时间")


purpose = (('0',u'注册验证'),('1',u'修改密码'),('2',u'信息修改'))
class VerificationCode(models.Model):#手机验证码
    phoneNum = models.CharField(max_length=18,null=False,blank=False,verbose_name=u'电话')
    code = models.CharField(max_length=18,null=False,blank=False,verbose_name=u'验证码')
    purpose = models.CharField(choices=purpose, max_length=18,null=True,blank=True,verbose_name=u'用途')
    register_date = models.DateTimeField(blank=False, null=False, verbose_name=u"添加日期")

    class Meta:
        ordering = ['-register_date']


class EmailValidSecond(models.Model):#邮箱验证码有效时间
    seconds = models.IntegerField(blank=True, null=True, verbose_name=u"验证码有效时间")


class EmailCode(models.Model):#邮箱验证码
    email = models.EmailField(max_length=100,null=False,blank=False,verbose_name=u'邮箱')
    code = models.CharField(max_length=18,null=False,blank=False,verbose_name=u'验证码')
    register_date = models.DateTimeField(blank=False, null=False, verbose_name=u"添加日期")

    class Meta:
        ordering = ['-register_date']


class Collection(models.Model):#用户收藏
    customer = models.ForeignKey(Customer,null=True,blank=True,verbose_name=u'用户')
    product = models.ForeignKey(Product,null=True,blank=True,verbose_name=u'产品')
    register_time = models.DateTimeField(blank=True, null=True, verbose_name=u"收藏时间", auto_now_add=True)

    class Meta:
        ordering = ['-register_time']
        unique_together = ('customer', 'product')


class Attention(models.Model):#用户关注
    customer = models.ForeignKey(Customer,null=True,blank=True,verbose_name=u'用户')
    product = models.ForeignKey(Product,null=True,blank=True,verbose_name=u'产品')
    register_time = models.DateTimeField(blank=True, null=True, verbose_name=u"关注时间", auto_now_add=True)

    class Meta:
        ordering = ['-register_time']
        unique_together = ('customer', 'product')


point_types = (('0',u'手机认证'),('1',u'实名认证'),('2',u'邮箱认证'),
               ('3',u'每日签到'),('4',u'连续7天签到'),('5',u'新增客户'),
               ('6', u'分享转发'),('7', u'OA处理'),('8', u'新增产品'))
class Point(models.Model):#用户额外添加的积分
    type = models.CharField(choices=point_types, max_length=10, verbose_name=u'积分类型', unique=True)
    points = models.IntegerField(verbose_name=u"积分")
    max_points = models.IntegerField(blank=True, null=True, verbose_name=u"封顶积分")

#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
import qrcode
from lvmeng.settings import *
from tinymce.models import HTMLField
import pypinyin
# User related:
# first_name is Chinese whole name
# username is phone number

#this method is used to change the unicode representation in django admin
def user_unicode_patch(self):
    return self.first_name
    # return '%s %s' % (self.first_name, self.last_name)
User.__unicode__ = user_unicode_patch

def permission__unicode_patch(self):
    return self.name
Permission.__unicode__ = permission__unicode_patch

import api.views

sex_choice = (('1',u'男'),('2',u'女'))

RISK_PREFERENCE = (
    ('1', u'极低风险型'),
    ('2', u'极低风险型'),
    ('3', u'较低风险型'),
    ('4', u'中等风险型'),
    ('5', u'较高风险型'),
    ('6', u'高风险型'),

)

BUSINESS_TYPE = (('1',u'金融机构'),('2',u'融资企业'))

class Business(models.Model):#机构
    logo = models.ImageField(upload_to="business/logo/",null=True,blank=True,verbose_name=u"机构logo(尺寸大小:50*50,png格式)")
    business_qrcode = models.ImageField(upload_to="business/qrcode/",null=True,blank=True,verbose_name=u"机构微信公众号(展示在客户端首页)")
    business_license_original = models.ImageField(upload_to="business/license",null=True,blank=True,verbose_name=u"营业执照（原件扫描）")
    business_license_copy = models.ImageField(upload_to="business/license",null=True,blank=True,verbose_name=u"营业执照（复印件盖章）")
    idCard_positive = models.ImageField(upload_to="idCard/image",null=True,blank=True,verbose_name=u"法人身份证正面")
    idCard_negative = models.ImageField(upload_to="idCard/image",null=True,blank=True,verbose_name=u"法人身份证反面")
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name=u'关联用户')
    name = models.CharField(max_length=50,null=False,blank=False, default='',verbose_name=u'机构名称')
    business_num = models.CharField(max_length=20,unique=True,verbose_name=u"机构编号")
    phoneNum = models.CharField(max_length=18,null=False,blank=False,verbose_name=u'电话')
    business_phone = models.CharField(max_length=18,verbose_name=u'机构公众电话(展示在客户端首页)')
    email = models.EmailField(verbose_name=u"管理员邮箱(登录用户名)")
    business_email = models.EmailField(null=True,blank=True,verbose_name=u"机构对外邮箱(展示在客户端首页)")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)
    address = models.CharField(max_length=30,verbose_name=u'机构地址')
    work_address = models.CharField(max_length=18,verbose_name=u'机构办公地址(展示在客户端首页)')
    register_date = models.DateField(null=True,blank=True,verbose_name=u'注册日期')
    due_time = models.DateField(null=True,blank=True,verbose_name=u"账户到期时间")
    contact_name = models.CharField(max_length=20,null=True,blank=True,verbose_name=u"直接联系人姓名")
    contact_position = models.CharField(max_length=20,null=True,blank=True,verbose_name=u"直接联系人职位")
    entry_person = models.CharField(max_length=20,null=True,blank=True,verbose_name=u'录入员')
    brief_introduction = models.CharField(max_length=15,null=True,blank=True,verbose_name=u'公司简介(15个字以内,显示在APP首页)')
    # note = models.TextField(max_length=3000,null=True,blank=True,verbose_name=u'公司详情')
    note = HTMLField(null=True,blank=True,verbose_name=u'公司详情')

    # business_type = models.CharField(choices=BUSINESS_TYPE,max_length=2,default=1,verbose_name=u"企业类型")
    def __unicode__(self):
        return self.name

    def meta(self):
        return self._meta

    class Meta:
        ordering = ['-register_date']

class Position(models.Model):#职位
    permissions = models.ManyToManyField(Permission,verbose_name=u"职位权限")
    business = models.ForeignKey(Business,null=True,blank=True,verbose_name=u"所属机构")
    name = models.CharField(max_length=30,verbose_name=u'职位名称')
    department = models.CharField(max_length=20,verbose_name=u"部门")
    register_date = models.DateField(null=True,blank=True,verbose_name=u'添加日期')
    entry_person = models.CharField(max_length=20,null=False,verbose_name=u'录入员')

    def __unicode__(self):
        return self.name

jobType = ((('1',u'兼职'),('2',u'全职')))
class Agent(models.Model):#合并Employee和Agent，统称为员工
    position = models.ForeignKey(Position,verbose_name=u"职位",null=True,blank=True)
    permissions = models.ManyToManyField(Permission,null=True,blank=True,verbose_name=u"职位权限")
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name=u'关联用户',null=True,blank=True)
    avatar = models.ImageField(upload_to='agent/avatar/', verbose_name=u"头像图片(尺寸大小:50*50)", blank=True,null=True)
    name = models.CharField(max_length=30,null=False,blank=False, default='',verbose_name=u'姓名')
    agent_num = models.PositiveIntegerField(null=True,blank=True,verbose_name=u"员工编号(机构编号+员工编号为邀请码)")
    phoneNum = models.CharField(max_length=18,null=False,blank=False,verbose_name=u'电话(登录用户名)')
    email = models.EmailField(max_length=30, verbose_name=u'邮箱')
    sex = models.CharField(choices=sex_choice,max_length=2,verbose_name=u'性别',default=1)
    wechat = models.CharField(max_length=20,null=True,blank=True,verbose_name=u"微信号")
    qq_number = models.PositiveIntegerField(null=True,blank=True,verbose_name=u"QQ号")
    address = models.CharField(max_length=30,verbose_name=u'员工地址')
    entry_person = models.CharField(max_length=20,null=False,verbose_name=u'录入员')
    register_date = models.DateField(null=True,blank=True,verbose_name=u'注册日期')
    idCard_num = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'身份证号')
    job_type = models.CharField(choices=jobType,max_length=2,null=True,blank=True,verbose_name=u"职位类型",default=2)
    salary_num = models.CharField(max_length=30,null=True,blank=True,verbose_name=u"工资卡号")
    bank_account = models.CharField(max_length=30,null=True,blank=True,verbose_name=u"开户银行")
    graduated_school = models.CharField(max_length=30,null=True,blank=True,verbose_name=u"毕业院校")
    graduated_time = models.DateField(null=True,blank=True,verbose_name=u"毕业时间")
    major = models.CharField(max_length=20,null=True,blank=True,verbose_name=u"专业")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)
    business = models.ForeignKey(Business,null=True,blank=True,verbose_name=u'所属机构')#affiliated with one business

    note = models.TextField(max_length=300,null=True,blank=True,verbose_name=u'备注')
    # note = HTMLField(max_length=300,null=True,blank=True,verbose_name=u'备注')

    qrcode = models.ImageField(upload_to='agent/qrcode/', verbose_name=u"员工二维码", blank=True,null=True)
    pinyin = models.CharField(max_length=30,null=True,blank=True,verbose_name=u"姓名拼音")
    first_pinyin = models.CharField(max_length=30,null=True,blank=True,verbose_name=u"姓名拼音首字母")

    device_id = models.CharField(max_length=200, null=True,blank=True,verbose_name=u"DEVICE_ID")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-register_date']

    def save(self, *args, **kwargs):
        self.pinyin = "".join(pypinyin.lazy_pinyin(self.name))
        self.first_pinyin = "".join(pypinyin.lazy_pinyin(self.name, style=pypinyin.FIRST_LETTER))
        super(Agent, self).save(*args, **kwargs)

    def create_qrcode(self, request):
        invitation_code = self.business.business_num + str(self.agent_num)
        # url = "http://www.niujidui.com/api/url_agent/?invitation_code=" + invitation_code
        url = "http://" + request.META['HTTP_HOST'] + "/api/url_agent?invitation_code=" + invitation_code
        file_path = 'agent/qrcode/%s.png' % invitation_code
        qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=200,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image()
        img.save(MEDIA_ROOT + file_path)
        self.qrcode = file_path
        self.save()

    @property
    def invitation_code(self):
        return self.business.business_num + str(self.agent_num)

    #根据邀请码获取agent,存在返回agent,不存在返回False
    @classmethod
    def get_agent(cls, code):
        if len(str(code))<6:
            return False
        business_num = code[0:5]
        try:
            agent_num = int(code[5:])
        except:
            return False
        try:
            agent = cls.objects.get(business__business_num=business_num, agent_num=agent_num, is_active=True)
            return agent
        except:
            return False

    #压缩头像像素(大小),尺寸不变
    def set_avatar_pixel(self, x=128, y=128):
        from PIL import Image
        path = self.avatar.path
        size = os.path.getsize(path)/1024
        if size>300:
            image = Image.open(path)
            image.resize((x,y),Image.ANTIALIAS)
            image.save(path, quality=20)


class Product_Type(models.Model):#产品类型
    typeName = models.CharField(max_length=20,verbose_name=u"产品类型名称")

    def __unicode__(self):
        return self.typeName

class Product(models.Model):#产品
    name = models.CharField(max_length=100, default=u'未命名', verbose_name=u"产品全名(显示在web页)")
    abbreviation = models.CharField(max_length=100, verbose_name=u"产品简称(显示在app页)")
    on_top = models.BooleanField(default=False,verbose_name=u"请选择是否上首页")
    return_expected = models.DecimalField(max_digits=6, decimal_places=4,verbose_name=u"预期年化收益(显示在首页)")
    period = models.IntegerField(verbose_name=u"产品期限/月(显示在首页)")
    mini_sub = models.BigIntegerField(verbose_name=u"认购起点/元(显示在首页)")
    product_sum = models.PositiveIntegerField(null=True,blank=True,verbose_name=u"产品总额(元)")
    product_type = models.ForeignKey(Product_Type,verbose_name=u"产品类型(显示在首页)",default=3)
    manager = models.CharField(max_length=30,verbose_name=u"产品管理人")
    custodian = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"托管机构")
    contract = models.FileField(upload_to="product/contract/",null=True,blank=True,verbose_name=u"产品合同(word或者pdf)")
    term_footnote = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"合同备注")
    province = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"所在省份")
    begin_date = models.DateField(blank=True, null=True, verbose_name=u"募集期限开始日期")
    end_date = models.DateField(blank=True, null=True, verbose_name=u"募集期限结束日期")
    addition = models.BigIntegerField(blank=True, null=True, verbose_name=u"追加额度(元)")
    alert_line = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True,verbose_name=u"预警线")
    clearance_line = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name=u"清盘线")
    subscription_fee = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name=u"认购费")
    custody_fee = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name=u"托管费")
    service_fee = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name=u"综合服务费")
    redemption_fee = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name=u"提前赎回费")
    management_fee = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name=u"管理费")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)
    compensation = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name=u"业绩报酬（盈利部分）")
    risk_preference = models.CharField(choices=RISK_PREFERENCE,default='3',max_length=10, verbose_name=u"风险类型")
    compensation_distribution = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"收益分配（结构化）")
    finished = models.BooleanField(verbose_name=u"已完成(产品状态)",default=False)
    ahead_end = models.BooleanField(default=False,verbose_name=u"可提前结束(产品状态)")
    structure = models.BooleanField(default=False,verbose_name=u"是否结构化(产品类型)")

    business = models.ForeignKey(Business,null=True,blank=True,verbose_name=u'所属机构')#affiliated with one business
    strategy = HTMLField(blank=True, null=True, verbose_name=u"实施策略")
    invest_scope = HTMLField(blank=True, null=True, verbose_name=u"投资范围")
    def __unicode__(self):
        return '%s-%s'%(self.business.name, self.abbreviation)

customer_type = (('1',u'注册客户'),('2',u'意向客户'))
class Customer(models.Model):#客户
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE,verbose_name=u'关联用户')
    portrait = models.ImageField(upload_to='customer/avatar/', verbose_name=u"头像图片(尺寸大小:50*50)", blank=True,null=True)
    name = models.CharField(max_length=30,null=False,blank=False,default='',verbose_name=u'姓名')
    phoneNum = models.CharField(max_length=18,verbose_name=u'电话')
    sex = models.CharField(choices=sex_choice,null=True,blank=True,max_length=2,verbose_name=u'性别',default=1)
    address = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'客户地址')
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)
    register_date = models.DateField(auto_now_add=True,verbose_name=u'注册日期')
    idCard_num = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'身份证号')
    company = models.CharField(max_length=30, verbose_name=u'所属公司', null=True, blank=True)
    risk_preference = models.CharField(max_length=5, choices=RISK_PREFERENCE, verbose_name=u'客户风险偏好', null=True, blank=True)
    product_target = models.ManyToManyField(Product,verbose_name=u'目标购买产品', null=True, blank=True)
    email = models.EmailField(max_length=30, verbose_name=u'邮箱', null=True, blank=True)
    industry = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'行业')
    city = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'城市')
    calling_card = models.ImageField(upload_to='customer/calling_card/', verbose_name=u"名片",blank=True,null=True)
    customer_type = models.CharField(choices=customer_type,max_length=2,default="2",verbose_name=u'客户类型')
    note = models.TextField(max_length=300,null=True,blank=True,verbose_name=u'备注')
    # note = HTMLField(null=True,blank=True,verbose_name=u'备注')
    agents = models.ManyToManyField(Agent,null=True,blank=True,verbose_name=u'所属员工')

    pinyin = models.CharField(max_length=30,null=True,blank=True,verbose_name=u"姓名拼音")
    first_pinyin = models.CharField(max_length=30,null=True,blank=True,verbose_name=u"姓名拼音首字母")


    def __unicode__(self):
        return '%s-%s'%(self.name, self.phoneNum)


    def save(self, *args, **kwargs):
        self.pinyin = "".join(pypinyin.lazy_pinyin(self.name))
        self.first_pinyin = "".join(pypinyin.lazy_pinyin(self.name, style=pypinyin.FIRST_LETTER))
        is_new = False if self.pk else True
        super(Customer, self).save(*args, **kwargs)

        #新注册客户添加手机认证积分
        if is_new and 1==int(self.customer_type):
            api.views.points_deal(self.user, '0')

    class Meta:
        ordering = ['-register_date']


    #压缩头像像素(大小),尺寸不变
    def set_portrait_pixel(self, x=128, y=128):
        from PIL import Image
        path = self.portrait.path
        size = os.path.getsize(path)/1024
        if size>300:
            image = Image.open(path)
            image.resize((x,y),Image.ANTIALIAS)
            image.save(path, quality=20)


class Customer_Pending(models.Model):#意向客户
    calling_card = models.ImageField(upload_to='customer/calling_card/', verbose_name=u"名片(尺寸大小:50*50)", blank=True,null=True)
    name = models.CharField(max_length=30,null=False,blank=False, default='',verbose_name=u'姓名')
    phoneNum = models.CharField(max_length=18,null=False,blank=False,verbose_name=u'电话')
    sex = models.CharField(choices=sex_choice,null=True,blank=True,max_length=2,verbose_name=u'性别',default=1)
    address = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'客户地址')
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)
    register_date = models.DateField(null=True,blank=True,verbose_name=u'注册日期', auto_now_add=True)
    idCard_num = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'身份证号')
    note = models.TextField(max_length=300,null=True,blank=True,verbose_name=u'备注')
    agents = models.ForeignKey(Agent,null=True,blank=True,verbose_name=u'所属员工')
    industry = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'行业')
    city = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'城市')

    company = models.CharField(max_length=30, verbose_name=u'所属公司', null=True, blank=True)
    risk_preference = models.CharField(max_length=5, choices=RISK_PREFERENCE, verbose_name=u'客户风险偏好', null=True, blank=True)
    product_target = models.ManyToManyField(Product, verbose_name=u'目标购买产品', null=True, blank=True)
    estimate_purchase_total = models.IntegerField(verbose_name=u'预计总共可购买规模', null=True, blank=True)
    email = models.EmailField(max_length=30, verbose_name=u'邮箱', null=True, blank=True)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-register_date']


'''
employee, agent
工资卡号，开户银行，职位类型（兼职，全职），职位，毕业院校，毕业时间，专业,籍贯，所在城市
添加这些field
'''
'''
class Employee(models.Model):#员工
    permissions = models.ManyToManyField(Permission,null=True,blank=True,verbose_name=u"角色权限")
    user = models.OneToOneField(User,verbose_name=u'关联用户')
    name = models.CharField(max_length=30,verbose_name=u'姓名')
    phoneNum = models.CharField(max_length=18,verbose_name=u'电话(作为用户名)')
    sex = models.CharField(choices=sex_choice,max_length=2,verbose_name=u'性别',default=1)
    idCard_num = models.CharField(max_length=30,verbose_name=u'身份证号')
    role = models.CharField(max_length=30,verbose_name=u"角色")
    business = models.ForeignKey(Business,null=True,blank=True,verbose_name=u'所属机构')
    address = models.CharField(max_length=30,verbose_name=u'地址')
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)
    register_date = models.DateField(null=True,blank=True,verbose_name=u'注册日期')
    entry_person = models.CharField(max_length=20,null=False,verbose_name=u'录入员')
    remark = models.TextField(max_length=300,null=True,blank=True,verbose_name=u'备注')

    email = models.EmailField(max_length=30, verbose_name=u'邮箱', null=True, blank=True)

    class Meta:
        ordering = ['-register_date']
'''
class Purchase(models.Model):#用户购买
    customer = models.ForeignKey(Customer,verbose_name=u'用户')
    product = models.ForeignKey(Product,verbose_name=u'产品')
    amount = models.IntegerField(verbose_name=u"购买金额(元)")
    start_date = models.DateField(verbose_name=u"开始日期")
    end_date = models.DateField(verbose_name=u"结束日期")
    register_time = models.DateTimeField(verbose_name=u"添加时间",auto_now_add=True)
    brief = models.TextField(max_length=150,null=True,blank=True,verbose_name=u"备注")

    def __unicode__(self):
        return self.product.name

    class Meta:
        ordering = ['-register_time']


pay_choice = (('1',u'现金'),('2',u'汇票'),('3',u'支票'))

class Real_purchase(models.Model):#员工填写客户购买的产品
    real_agent = models.ForeignKey(Agent,verbose_name=u'所属员工')
    business = models.ForeignKey(Business,verbose_name=u'所属机构')
    customer = models.ForeignKey(Customer,verbose_name=u'客户姓名')
    product = models.ForeignKey(Product,verbose_name=u'产品')
    amount = models.IntegerField(verbose_name=u"实收金额(元)")
    income_date = models.DateField(verbose_name=u"收款日期")
    end_date = models.DateField(verbose_name=u"产品结束日期")
    pay_type = models.CharField(choices=pay_choice,max_length=3,default='1',verbose_name=u"付款方式")
    department = models.CharField(max_length=10,null=True,blank=True,verbose_name=u"部门")
    bill_number = models.CharField(max_length=50,null=True,blank=True,verbose_name=u"票据单号")
    register_time = models.DateTimeField(verbose_name=u"添加时间",auto_now_add=True)
    brief = models.TextField(max_length=150,null=True,blank=True,verbose_name=u"简介")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)

    class Meta:
        ordering = ['customer','-register_time']

class Announcement(models.Model):#添加机构公告图片信息
    announce_business = models.ForeignKey(Business,verbose_name=u"关联机构",null=True,blank=True,related_name="announce_business")
    picture = models.ImageField(upload_to='business/pictures/', verbose_name=u"机构公告图片(尺寸大小:375*106)", blank=True,null=True)
    title = models.CharField(max_length=30,verbose_name=u"标题")
    order = models.PositiveIntegerField(verbose_name=u"顺序(数字小的排在前面，大于1的数字)")
    date = models.DateField(verbose_name=u"添加时间")
    show_text = models.BooleanField(verbose_name=u"是否显示在app首页轮播图(需要插入图片)",default=True)
    # text = models.TextField(max_length=500,null=True,blank=True,verbose_name=u"内容说明")
    text = HTMLField(null=True,blank=True,verbose_name=u"内容说明")
    read_num = models.PositiveIntegerField(null=True,blank=True,default=0,verbose_name=u"阅读次数")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=True)

    class Meta:
        ordering = ['-date']


valid_status = (('1',u'通过'),('2',u'驳回'),('3',u'注册审核'))
class Redister_Business(models.Model):#机构
    user = models.OneToOneField(User,null=True,blank=True,verbose_name=u'关联用户')
    logo = models.ImageField(upload_to="business/logo/",null=True,blank=True,verbose_name=u"机构logo(尺寸大小:50*50,png格式)")
    business_qrcode = models.ImageField(upload_to="business/qrcode/",null=True,blank=True,verbose_name=u"机构微信公众号(展示在客户端首页)")
    business_license_original = models.ImageField(upload_to="business/license",null=True,blank=True,verbose_name=u"营业执照（原件扫描）")
    business_license_copy = models.ImageField(upload_to="business/license",null=True,blank=True,verbose_name=u"营业执照（复印件盖章）")
    idCard_positive = models.ImageField(upload_to="idCard/image",null=True,blank=True,verbose_name=u"法人身份证正面")
    idCard_negative = models.ImageField(upload_to="idCard/image",null=True,blank=True,verbose_name=u"法人身份证反面")
    name = models.CharField(max_length=50,null=False,blank=False, default='',verbose_name=u'机构名称')
    phoneNum = models.CharField(max_length=18,null=False,blank=False,verbose_name=u'电话')
    business_phone = models.CharField(max_length=18,verbose_name=u'机构公众电话(展示在客户端首页)')
    email = models.EmailField(verbose_name=u"管理员邮箱(登录用户名)")
    business_email = models.EmailField(null=True,blank=True,verbose_name=u"机构对外邮箱(展示在客户端首页)")
    address = models.CharField(max_length=30,verbose_name=u'机构地址')
    work_address = models.CharField(max_length=18,verbose_name=u'机构办公地址(展示在客户端首页)')
    register_date = models.DateField(null=True,blank=True,verbose_name=u'注册日期')
    contact_name = models.CharField(max_length=20,null=True,blank=True,verbose_name=u"直接联系人姓名")
    contact_position = models.CharField(max_length=20,null=True,blank=True,verbose_name=u"直接联系人职位")
    brief_introduction = models.CharField(max_length=15,null=True,blank=True,verbose_name=u'公司简介(15个字以内,显示在APP首页)')
    note = HTMLField(null=True,blank=True,verbose_name=u'公司详情')
    status = models.CharField(choices=valid_status,max_length=2,default='3',verbose_name=u"审核状态")
    is_active = models.BooleanField(verbose_name=u"是否有效",default=False)
    # business_type = models.CharField(choices=BUSINESS_TYPE,max_length=2,default=1,verbose_name=u"企业类型")

class Online_chat(models.Model):
    sender = models.ForeignKey(User,verbose_name=u"发送人",related_name="sender")
    recipient = models.ForeignKey(User,verbose_name=u"接收人",related_name="recipient")
    business = models.ForeignKey(Business,verbose_name=u"所属机构")
    content = models.CharField(max_length=500,verbose_name=u"内容")
    send_time = models.DateTimeField(auto_now_add=True,verbose_name=u"发送时间")
    read = models.BooleanField(default=False)




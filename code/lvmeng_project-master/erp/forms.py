#coding:utf-8
from django import forms
from django.forms import ModelForm,TextInput,Textarea
import django.forms as df
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import CheckboxSelectMultiple,CheckboxInput,RadioSelect
from localflavor.cn.forms import CNCellNumberField,CNIDCardField
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from tinymce.widgets import TinyMCE
from form_utils.widgets import ImageWidget

from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div,Button
class BusinessModifyForm(ModelForm):#机构修改自己的信息
    phoneNum = CNCellNumberField(label=u"手机号码", error_messages={
        'invalid': u'请输入有效手机号.',
    })
    def __init__(self, *args, **kwargs):
        super(BusinessModifyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                '',#this is head, make it empty
                Div(
                    'logo',
                    css_id = 'picture_field'#this is just an example to add custom class to certain field
                ),
                Div(
                    'business_qrcode',
                    css_id = 'picture_field'#this is just an example to add custom class to certain field
                ),
                'email',
                "business_email",
                "phoneNum",
                "business_phone",
                "work_address",
                "brief_introduction",
                "note"
            )
        )
        self.helper.layout.append(Submit('save',u'保存'))

    class Meta:
        model = Business
        fields = ["logo","business_qrcode","email","business_email","phoneNum","business_phone","work_address","brief_introduction","note"]
        widgets = {
            'note':TinyMCE(attrs={'cols': 150, 'rows': 10}),
            'logo':ImageWidget(template='%(image)s<br />%(input)s'),
            'business_qrcode':ImageWidget(template='%(image)s<br />%(input)s'),
        }

# class BusinessInfoShowForm(ModelForm):#机构查看自己的信息
#
#     class Meta:
#         model = Business
#         # fields = '__all__'
#         exclude = ('user','is_active','register_date','entry_person',)
#         widgets = {
#             'note':TinyMCE(attrs={'cols': 150, 'rows': 10}),
#             'logo':ImageWidget(template='%(image)s<br />%(input)s'),
#             'business_qrcode':ImageWidget(template='%(image)s<br />%(input)s'),
#             'business_license_original':ImageWidget(template='%(image)s<br />%(input)s'),
#             'business_license_copy':ImageWidget(template='%(image)s<br />%(input)s'),
#             'idCard_positive':ImageWidget(template='%(image)s<br />%(input)s'),
#             'idCard_negative':ImageWidget(template='%(image)s<br />%(input)s'),
#         }


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', u'保存'))

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('changed_by','is_active','business')
        widgets = {
            # 'invest_scope': Textarea,
            # 'strategy': Textarea,
            'begin_date' : DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            'end_date': DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            'mini_sub': TextInput(attrs={'min':'0','type':'number','oninput':'ToChinese_mini_sub(this.value);','style':'width:330px;float:left;'}),
            'product_sum': TextInput(attrs={'min':'0','max':'1000000000000','type':'number','oninput':'ToChinese_product_sum(this.value);','style':'width:330px;float:left;'}),
            'addition': TextInput(attrs={'min':'0','type':'number','step':'1','style':'width:330px;float:left;','oninput':'ToChinese_addition(this.value);'}),
            'clearance_line': TextInput(attrs={'min':'0','type':'number','step':'0.0001','style':'width:330px;float:left;','oninput':'ToChinese_decimal_clearance_line(this.value*100);'}),
            'subscription_fee': TextInput(attrs={'min':'0','type':'number','step':'0.0001','style':'width:330px;float:left;','oninput':'ToChinese_decimal_subscription_fee(this.value*100);'}),
            'custody_fee': TextInput(attrs={'min':'0','type':'number','step':'0.0001','style':'width:330px;float:left;','oninput':'ToChinese_decimal_custody_fee(this.value*100);'}),
            'service_fee': TextInput(attrs={'min':'0','type':'number','step':'0.0001','style':'width:330px;float:left;','oninput':'ToChinese_decimal_service_fee(this.value*100);'}),
            'redemption_fee': TextInput(attrs={'min':'0','type':'number','step':'0.0001','style':'width:330px;float:left;','oninput':'ToChinese_decimal_redemption_fee(this.value*100);'}),
            'compensation': TextInput(attrs={'min':'0','type':'number','step':'0.0001','style':'width:330px;float:left;','oninput':'ToChinese_decimal_compensation(this.value*100);'}),
            'alert_line': TextInput(attrs={'min':'0','type':'number','step':'0.0001','style':'width:330px;float:left;','oninput':'ToChinese_decimal_alert_line(this.value*100);'}),
            'management_fee': TextInput(attrs={'min':'0','type':'number','step':'0.0001','style':'width:330px;float:left;','oninput':'ToChinese_decimal_management_fee(this.value*100);'}),
            'period': TextInput(attrs={'min':'0','type':'number','step':'1','style':'width:330px;'}),
            'return_expected': TextInput(attrs={'min':'0','type':'number','step':'0.0001','style':'width:330px;float:left;','oninput':'ToChinese_decimal(this.value*100);'}),
            'strategy':TinyMCE(attrs={'cols': 50, 'rows': 5}),
            'invest_scope':TinyMCE(attrs={'cols': 50, 'rows': 5})
        }

class RealPurchaseForm(ModelForm):#新增购买(没有客户ID)
    def __init__(self, *args, **kwargs):
        super(RealPurchaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'保存'))
    class Meta:
        model = Real_purchase
        fields = "__all__"
        exclude = ('register_time','is_active','real_agent','business')
        widgets = {
            'income_date' : DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            'end_date': DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            'amount': TextInput(attrs={'type':'number','style':'width:230px;','min':'0','max':'1000000000000','oninput':'ToChinese(this.value);'}),
            'note':TinyMCE(attrs={'cols': 150, 'rows': 10})
        }

class PurchaseForm(ModelForm):#新增购买(有客户ID)
    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'保存'))
    class Meta:
        model = Real_purchase
        fields = "__all__"
        exclude = ('register_time','is_active','real_agent','business','customer','pinyin','first_pinyin')
        widgets = {
            'income_date' : DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            'end_date': DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            'amount': TextInput(attrs={'type':'number','style':'width:230px;','min':'0','max':'1000000000000','oninput':'ToChinese(this.value);'}),
            'note':TinyMCE(attrs={'cols': 150, 'rows': 10})
        }

'''
class EmployeeForm(ModelForm):
    phoneNum = CNCellNumberField(label="手机号码")
    idCard_num = CNIDCardField(label="身份证号")
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'保存'))
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = ('user','is_active',)
        widgets = {
           'register_date':TextInput(attrs={'readonly':'readonly'}),
           'entry_person':TextInput(attrs={'readonly':'readonly'}),
           'permissions':CheckboxSelectMultiple,
        }
'''
'''
class EmployeeForm2(ModelForm):
    phoneNum = CNCellNumberField(label="手机号码")
    idCard_num = CNIDCardField(label="身份证号")
    def __init__(self, *args, **kwargs):
        super(EmployeeForm2, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'保存'))
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = ('user','is_active','permissions')
        widgets = {
           'register_date':TextInput(attrs={'readonly':'readonly'}),
           'entry_person':TextInput(attrs={'readonly':'readonly'}),
           # 'permissions':CheckboxSelectMultiple,
        }
'''
class PositionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', u'保存'))
    class Meta:
        model = Position
        fields = "__all__"
        exclude = ('business',)
        widgets = {
           'register_date':TextInput(attrs={'readonly':'readonly'}),
           'entry_person':TextInput(attrs={'readonly':'readonly'}),
           'permissions':CheckboxSelectMultiple,
        }

class Position_permission(ModelForm):
    class Meta:
        model = Position
        fields = ["permissions"]
        widgets = {
           'permissions':CheckboxSelectMultiple,
        }

class BusinessForm(ModelForm):
    phoneNum = CNCellNumberField(label=u"手机号码", error_messages={
        'invalid': u'请输入有效手机号.',
    })
    def __init__(self, *args, **kwargs):
        super(BusinessForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'保存'))
    class Meta:
        model = Business
        fields = "__all__"
        exclude = ('user','is_active')
        widgets = {
           # 'register_date':TextInput(attrs={'readonly':'readonly'}),
           'entry_person':TextInput(attrs={'readonly':'readonly'}),
           'register_date':DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
           'due_time':DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
           'note':TinyMCE(attrs={'cols': 150, 'rows': 10})
        }

class RedisterBusinessForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RedisterBusinessForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'提交注册申请'))
    class Meta:
        model = Redister_Business
        fields = "__all__"
        exclude = ('user','is_active','status','note','brief_introduction','business_email','contact_position','contact_name','register_date')
        widgets = {
           'email':TextInput(attrs={'readonly':'readonly'}),
           'phoneNum':TextInput(attrs={'readonly':'readonly'}),
           'name':TextInput(attrs={'readonly':'readonly'}),
           'logo':ImageWidget(attrs={'required':'required'}),
           'business_qrcode':ImageWidget(attrs={'required':'required'}),
           'business_license_original':ImageWidget(attrs={'required':'required'}),
           'business_license_copy':ImageWidget(attrs={'required':'required'}),
           'idCard_positive':ImageWidget(attrs={'required':'required'}),
           'idCard_negative':ImageWidget(attrs={'required':'required'}),
           'address':TextInput(attrs={'required':'required'}),
           'work_address':TextInput(attrs={'required':'required'}),
           'business_phone':TextInput(attrs={'required':'required'}),
           # 'register_date':DateWidget(attrs={'style':'width:330px;','required':'required'}, usel10n = True, bootstrap_version=2),
        }

class Redister_Business_Save(ModelForm):

    def __init__(self, *args, **kwargs):
        super(Redister_Business_Save, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'通过,并完善信息'))
        self.helper.layout.append(Button('save',u'驳回'))
    class Meta:
        model = Business
        fields = "__all__"
        exclude = ('user','is_active')
        widgets = {
           'entry_person':TextInput(attrs={'readonly':'readonly'}),
           'register_date':DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
           'due_time':DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
           'note':TinyMCE(attrs={'cols': 150, 'rows': 10})
        }

class AgentForm(ModelForm):
    phoneNum = CNCellNumberField(label=u"手机号码", error_messages={
        'invalid': u'请输入有效手机号.',
    })
    idCard_num = CNIDCardField(label=u"身份证号",min_length=0, error_messages={
        'invalid': u'请输入有效身份证号码.',
        'checksum': u'请输入有效身份证号码',
        'birthday': u'请输入有效身份证号码',
        'location': u'请输入有效身份证号码',
    })
    def __init__(self, *args, **kwargs):
        super(AgentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', u'保存'))
    class Meta:
        model = Agent
        fields = "__all__"
        # exclude = ('user','is_active','agent_num')
        exclude = ('user','is_active','agent_num','business','qrcode','pinyin','first_pinyin','device_id')
        widgets = {
            'register_date':TextInput(attrs={'readonly':'readonly'}),
            'entry_person':TextInput(attrs={'readonly':'readonly'}),
            'permissions':CheckboxSelectMultiple,
            'graduated_time':DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            # 'note':TinyMCE(attrs={'cols': 50, 'rows': 5})
        }

class AgentForm2(ModelForm):
    phoneNum = CNCellNumberField(label=u"手机号码", error_messages={
        'invalid': u'请输入有效手机号.',
    })
    idCard_num = CNIDCardField(label=u"身份证号",min_length=0, error_messages={
        'invalid': u'请输入有效身份证号码.',
        'checksum': u'请输入有效身份证号码',
        'birthday': u'请输入有效身份证号码',
        'location': u'请输入有效身份证号码',
    })
    def __init__(self, *args, **kwargs):
        super(AgentForm2, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', u'保存'))
    class Meta:
        model = Agent
        fields = "__all__"
        # exclude = ('user','is_active','agent_num')
        exclude = ('user','is_active','permissions','agent_num','business','qrcode','pinyin','first_pinyin','device_id')
        widgets = {
            'register_date':TextInput(attrs={'readonly':'readonly'}),
            'entry_person':TextInput(attrs={'readonly':'readonly'}),
            'graduated_time':DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            # 'note':TinyMCE(attrs={'cols': 50, 'rows': 5})
        }

class CustomerForm(ModelForm):
    phoneNum = CNCellNumberField(label=u"手机号码", error_messages={
        'invalid': u'请输入有效手机号.',
    })
    # idCard_num = CNIDCardField(label="身份证号")
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', u'保存'))
    class Meta:
        model = Customer
        fields = "__all__"
        # exclude = ('user','is_active','agent_num')
        exclude = ('user','is_active','customer_type','agents','register_date','pinyin','first_pinyin')
        widgets = {
            'register_date':TextInput(attrs={'readonly':'readonly'}),
            'agents':CheckboxSelectMultiple,
            'calling_card':ImageWidget()
        }

# from image_cropping import ImageCropWidget
class PictureForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PictureForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', u'保存'))
    class Meta:
        model = Announcement
        fields = "__all__"
        exclude = ('is_active','announce_business','read_num')
        widgets = {
           'date':TextInput(attrs={'readonly':'readonly'}),
            'text':TinyMCE(attrs={'cols': 150, 'rows': 10})
            # 'show_text':CheckboxInput,
            # 'picture': ImageCropWidget,


        }









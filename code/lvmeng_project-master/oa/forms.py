#coding:utf-8
from django import forms
from django.forms import ModelForm,TextInput,Textarea
import django.forms as df
from models import Internal_announcement,Daily_work,Cost_application,Leave_management,Travel_apply,Daily_to_do,All_Examine,Check_Time_Setting
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import CheckboxSelectMultiple,RadioSelect
from django.contrib.admin import widgets
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from tinymce.widgets import TinyMCE
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
class InternalForm(ModelForm):#通知公告(员工)
    def __init__(self, *args, **kwargs):
        super(InternalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'保存'))
    class Meta:
        model = Internal_announcement
        fields = "__all__"
        exclude = ('announcement_business','is_active','add_time ')
        widgets = {
            'on_top':RadioSelect,
            'publish':RadioSelect,
            'onTop_start': DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            'onTop_end': DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            'publish_start':DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            'publish_end': DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            'content':TinyMCE(attrs={'cols': 50, 'rows': 5})
        }

class DailyForm(ModelForm):#工作汇报
    def __init__(self, *args, **kwargs):
        super(DailyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'提交申请'))
    class Meta:
        model = Daily_work
        fields = "__all__"
        exclude = ('business','time','is_active','user')
        widgets = {'examine_user':CheckboxSelectMultiple,}


class LeaveForm(ModelForm):#请假管理
    def __init__(self, *args, **kwargs):
        super(LeaveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'提交申请'))
    class Meta:
        model = Leave_management
        fields = "__all__"
        exclude = ('business','is_active','time','user')
        widgets = {
           'start': DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
           'end': DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
            'examine_user':CheckboxSelectMultiple,
        }


class CostForm(ModelForm):#费用申请
    def __init__(self, *args, **kwargs):
        super(CostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                '',#this is head, make it empty
                'examine_user',
                # 'topic',
                Div(
                    'topic',
                    css_id = 'special-fields'#this is just an example to add custom class to certain field
                ),
                'content',
                'cost',
            )
        )
        self.helper.layout.append(Submit('save',u'提交申请'))
    class Meta:
        model = Cost_application
        fields = "__all__"
        exclude = ('business','is_active','time','read_status','user')
        widgets = {
           'examine_user':CheckboxSelectMultiple,
           'cost': TextInput(attrs={'min':'0','max':'1000000000000','type':'number','oninput':'ToChinese(this.value);','style':'width:330px;'}),
        }


class TravelForm(ModelForm):#出差申请
    def __init__(self, *args, **kwargs):
        super(TravelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'提交申请'))
    class Meta:
        model = Travel_apply
        fields = "__all__"
        exclude = ('business','is_active','time','read_status','user')
        widgets = {
           'start': DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
           'end': DateWidget(attrs={'style':'width:330px;'}, usel10n = True, bootstrap_version=2),
           'examine_user':CheckboxSelectMultiple,
           'cost': TextInput(attrs={'min':'0','max':'1000000000000','type':'number','oninput':'ToChinese(this.value);','style':'width:330px;'}),
        }

class AllExamineForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AllExamineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'提交审核'))
    class Meta:
        model = All_Examine
        fields = "__all__"
        exclude = ('content_type','object_id','examine_business','is_active','read_status','examine_time','examine_user')


class DailyToDoForm(ModelForm):#待办事件
    #input_formats-->输入格式  format-->显示格式
    # to_do_time = forms.DateTimeField(input_formats=["%Y-%m-%dT%H:%M"],widget=forms.DateTimeInput(attrs={'type':'datetime-local'}, format="%Y-%m-%dT%H:%M"), label=u"待办事时间")

    def __init__(self, *args, **kwargs):
        super(DailyToDoForm, self).__init__(*args, **kwargs)
        # self.fields['to_do_time'].widget = widgets.AdminSplitDateTime()
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'保存'))
    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy HH:ii P',
            'autoclose': True,
            'showMeridian' : True
            }
        model = Daily_to_do
        fields = "__all__"
        exclude = ('add_time','is_active','todo_user')
        widgets = {
            'to_do_time': DateTimeWidget(attrs={'id':"id_to_do_time"}, usel10n = True, bootstrap_version=2,options = dateTimeOptions),
            'invest_scope':TinyMCE(attrs={'cols': 50, 'rows': 5})
        }

class CheckTimeSettingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CheckTimeSettingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'保存'))
    class Meta:
        dateTimeOptions = {
            'format': 'HH:ii P',
            'autoclose': True,
            'showMeridian' : True
            }
        model = Check_Time_Setting
        fields = "__all__"
        exclude = ("business",)
        widgets = {
            "check_in_time":TimeWidget(attrs={'id':"id_check_in_time"}),
            "check_out_time":TimeWidget(attrs={'id':"id_check_out_time"}),
            "check_in_remind":TimeWidget(attrs={'id':"id_check_in_remind"}),
            "check_out_remind":TimeWidget(attrs={'id':"id_check_out_remind"}),
        }



#coding:utf-8
from django import forms
from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from form_utils.widgets import ImageWidget

from api.models import *
from tinymce.widgets import TinyMCE

class CaptchaForm(forms.Form):
    captcha = CaptchaField()

''' 新闻头条Form '''
class HeadlineForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HeadlineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'保存'))
    class Meta:
        model = Headline
        fields = "__all__"
        exclude = ('register_date','url','read_num')
        widgets = {
            'context':TinyMCE(attrs={'cols': 50, 'rows': 5}),
            'picture':ImageWidget(template='%(image)s<br />%(input)s'),
        }

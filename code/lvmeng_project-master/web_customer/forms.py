#coding:utf-8
from django.forms import ModelForm,TextInput,Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from web_customer.models import Lv_Announcement,business_carousel
from tinymce.widgets import TinyMCE

class Lv_announcement_Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Lv_announcement_Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'保存'))
    class Meta:
        model = Lv_Announcement
        fields = "__all__"
        exclude = ('data','is_active',)
        widgets = {
            'text':TinyMCE(attrs={'cols': 150, 'rows': 10})
        }

class Business_Carousel_Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Business_Carousel_Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save',u'保存'))
    class Meta:
        model = business_carousel
        fields = "__all__"
        exclude = ('business','add_user','add_time')



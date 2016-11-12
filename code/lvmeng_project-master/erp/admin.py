from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin
from models import *
from django.contrib.auth.models import Permission

# Register your models here.

admin.site.register(Customer)
admin.site.register(Customer_Pending)
admin.site.register(Agent)
admin.site.register(Business)
admin.site.register(Product)
admin.site.register(Permission)
admin.site.register(Product_Type)
admin.site.register(Announcement)

# from image_cropping import ImageCroppingMixin
#
# class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
#     pass
#
# admin.site.register(Announcement, MyModelAdmin)
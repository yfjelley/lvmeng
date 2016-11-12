from django.contrib import admin

from models import *


# Register your models here.
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'url', 'date')

class HeadlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'register_date')

class CheckinAdmin(admin.ModelAdmin):
    list_display = ('user', 'latest_date', 'points', 'continuous_days')

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'amount', 'register_time')

class ValidSecondAdmin(admin.ModelAdmin):
    list_display = ('seconds',)

class EmailValidSecondAdmin(admin.ModelAdmin):
    list_display = ('seconds',)

class PointAdmin(admin.ModelAdmin):
    list_display = ('type', 'points', 'max_points')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('headline', 'user', 'time')

admin.site.register(Version, VersionAdmin)
admin.site.register(Headline, HeadlineAdmin)
admin.site.register(Checkin, CheckinAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(ValidSecond, ValidSecondAdmin)
admin.site.register(EmailValidSecond, EmailValidSecondAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Comment, CommentAdmin)
from django.contrib import admin
from models import CheckWork,CheckWork_history,Internal_announcement,Daily_work,Travel_apply,Leave_management,Cost_application,Daily_to_do
# Register your models here.


admin.site.register(CheckWork)
admin.site.register(CheckWork_history)
admin.site.register(Internal_announcement)
admin.site.register(Cost_application)
admin.site.register(Leave_management)
admin.site.register(Travel_apply)
admin.site.register(Daily_work)
admin.site.register(Daily_to_do)
from django.contrib import admin

from models import *


# Register your models here.
class CellRecordsCustomerAdmin(admin.ModelAdmin):
    list_display = ('agent', 'customer', 'start_time', 'end_time')

class CellRecordsPCustomerAdmin(admin.ModelAdmin):
    list_display = ('agent', 'customer', 'start_time', 'end_time')

class AgentVersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'url', 'date')

class TemporaryFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'user', 'upload_time')

admin.site.register(Cell_Records_Customer, CellRecordsCustomerAdmin)
admin.site.register(Cell_Records_PCustomer, CellRecordsPCustomerAdmin)
admin.site.register(Agent_Version, AgentVersionAdmin)
admin.site.register(Temporary_File, TemporaryFileAdmin)
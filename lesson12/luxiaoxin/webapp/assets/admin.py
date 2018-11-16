from django.contrib import admin
from .models import Assets
# Register your models here.

class AssetsAdmin(admin.ModelAdmin):
    admin.site.site_title = '设备资产管理'
    admin.site.site_header = '设备资产管理'

    list_display = ['id', 'hostname', 'cpu_num', 'cpu_model', 'mem_total', 'disk', 'status', 'os_system', 'frame', 'op', 'remark']

    list_per_page = 10

    ordering = ('id', '-cpu_num')

    #list_editable = ['cpu_model', 'os_system']

    list_display_links = ('hostname', )

    search_fields =('hostname', ) #搜索字段



admin.site.register(Assets, AssetsAdmin)

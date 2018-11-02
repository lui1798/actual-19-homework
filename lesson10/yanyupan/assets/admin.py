from django.contrib import admin
from .models import Assets

# Register your models here.

class AssetsAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ('id', 'hostname', 'cpu_num', 'cpu_model', 'mem_total', 'remark')
    # 排序
    ordering = ('id', '-cpu_num')
    # 设置默认可编辑字段
    list_editable = ['cpu_num', 'cpu_model']
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'hostname')
    # 设置每页显示多少条记录，默认是100
    list_per_page = 10

admin.site.register(Assets, AssetsAdmin)
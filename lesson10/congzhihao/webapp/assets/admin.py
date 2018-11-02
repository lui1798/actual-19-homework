from django.contrib import admin
from .models import Assets

# Register your models here.
class AssetsAdmin(admin.ModelAdmin):

    #界面显示的字段有哪些
    list_display = ('id', 'host_name','cpu_num','cpu_model','disk','status','use_date','update_date','remark')

    #每页显示最大记录数，默认为100
    list_per_page = 50

    #排序字段，负号表示倒序，可以是list或tuple,tuple里只有一个值的时候必须加上逗号
    ordering = ('-id',)

    #查询界面可直接修改的字段
    list_editable = ['cpu_num','status']




admin.site.register(Assets,AssetsAdmin)
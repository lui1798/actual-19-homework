from django.contrib import admin

# Register your models here.
from .models import Assets #导入自定义数据库
class AssetsAdmin(admin.ModelAdmin):
    #显示的字段
    list_display=['id','hostname','cpu_num','cpu_model','mem_total','disk','public_ip','private_ip','remote_ip','op','status','os_system','service_line','frame','remark','create_time','update_time']  #也可以用元组，最好用元组
    # ordering设置默认排序字段，负号表示降序排序
    ordering=('id',)
    # list_editable 设置默认可编辑字段
    list_editable = ['cpu_num', 'cpu_model']
    #fk_fields 设置显示外键字段
    fk_fields = ('mem_total',)
    #筛选器
    #list_filter =('id','hostname','cpu_num','cpu_model','remark','mem_total') #过滤器
    #search_fields =('id','hostname','cpu_num') #搜索字段
    #date_hierarchy = 'go_time'    # 详细时间分层筛选
# 在admin中注册绑定
admin.site.register(Assets,AssetsAdmin)   #把models注册进去
from django.contrib import admin

# Register your models here.

from .models import Users

class UsersAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id','hostname','cpu_num','cpu_model','mem','disk','ip','op',
    #                 'host_status','system','line','create_time','update_time','remark']
    # ordering = ['id']
    # # list_editable = ['disk']
    # list_display_links = ('id', 'hostname')
    # search_fields = ('id', 'hostname', 'ip')  # 搜索字段

admin.site.register(Users,UsersAdmin)

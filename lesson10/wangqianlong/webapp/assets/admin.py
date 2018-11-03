from django.contrib import admin


from .models import Assets

# Register your models here.
class AssetsAdmin(admin.ModelAdmin):
    # list_display = ['id','hostname','cpu_num','cpu_model','mem_total','disk','public_ip','private_ip','remote_ip',...
    # 'status','os_system','service_line','frame','remark']
    list_display = ['id', 'hostname', 'cpu_num', 'cpu_model', 'mem_total', 'disk', 'public_ip', 'private_ip','remote_ip','status', 'os_system', 'service_line', 'frame', 'remark']

    # ordering = ('-id',)
    #
    # list_editable = ['cpu_num', 'cpu_model']
    #
    # list_display_links = ('hostname',)
    #
    # search_fields = ('hostname',)




admin.site.register(Assets,AssetsAdmin)
from django.contrib import admin

from .models import Assets

class AssetsAdmin(admin.ModelAdmin):
    list_display = ['id', 'hostname','cpu_num','cpu_model','mem_total','disk','public_ip','private_ip','remote_ip','op','status','os_system']
    list_per_page = 10
    ordering = ('id',)
    list_filter = ('id', 'hostname', 'cpu_num', 'cpu_model')
    search_fields = ('id', 'hostname', 'cpu_num', 'cpu_model', )
    #readonly_fields = ('cpu_num','cpu_model')

admin.site.register(Assets, AssetsAdmin)

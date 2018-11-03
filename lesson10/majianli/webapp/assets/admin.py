from django.contrib import admin

# Register your models here.

from .models import Assets


class AssetsAdmin(admin.ModelAdmin):
    list_display = ['id', 'hostname', 'cpu_num','cpu_model','remark','private_ip','op','status']
    ordering = ('id',)
    # list_editable = ['hostname','cpu_model']

    # list_display_links = ('hostname',)
    search_fields =('cpu_model', 'hostname')
    list_filter =('cpu_num','cpu_model')
admin.site.register(Assets, AssetsAdmin)

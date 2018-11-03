from django.contrib import admin
from .models import Assets

class AssetsAdmin(admin.ModelAdmin):
    list_display = ['id','hostname','cpu_num','cpu_model','remark','public_ip','mem_total','disk']
    ording = ('-id',)
    search_fields = ('hostname',)
    list_editable = ('hostname',)
    list_per_page = 10

admin.site.register(Assets,AssetsAdmin)

# Register your models here.

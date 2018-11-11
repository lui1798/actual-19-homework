from django.contrib import admin

from .models import Assets

class AssetsAdmin(admin.ModelAdmin):

    # 显示的字段
    list_display = ('id', 'hostname', 'cpu_num', 'cpu_model', 'public_ip', 'disk', 'remark')

    ordering = ('-id', )

    # list_editable = ['cpu_model', 'disk', 'hostname']

    # list_display_links = ('hostname',)
    list_per_page = 10

    search_fields = ('hostname', )

    # date_hierarchy = 'go_time'



admin.site.register(Assets, AssetsAdmin)


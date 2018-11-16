from django.contrib import admin
from .models import Users

class UserAdmin(admin.ModelAdmin):
    admin.site.site_title = '用户管理'
    admin.site.site_header = '用户管理'

    list_display = ['id', 'username', 'sex', 'age', 'city']

    list_per_page = 10

    #ordering = ('id', '-cpu_num')

    #list_editable = ['cpu_model', 'os_system']

    #list_display_links = ('hostname', )

    search_fields =('username', ) #搜索字段



admin.site.register(Users, UserAdmin)

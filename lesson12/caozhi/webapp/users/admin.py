from django.contrib import admin
from .models import Users

class UserAdmin(admin.ModelAdmin):
    list_play = ['id', 'name', 'sex', 'age', 'city', ]


admin.site.register(Users, UserAdmin)

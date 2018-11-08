from django.contrib import admin
from .models import Users
# Register your models here.
class UserAdmin(admin.ModelAdmin):

    list_display = ["username",
                    "gender",
                    "id_card",
                    "age",
                    "address",
                    "remark",
                    "create_time",
                    "update_time"]

admin.site.register(Users,UserAdmin)
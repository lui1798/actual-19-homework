from django.contrib import admin
from .models import Users
from .models import Photo



class UsersAdmin(admin.ModelAdmin):
    pass



class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
        'thumbnail',
    ]



admin.site.register(Users, UsersAdmin)
admin.site.register(Photo, PhotoAdmin)



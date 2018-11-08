"""umapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from user.views import user_home,user_list,user_detail,user_delete,user_update,user_add,user_export

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #user
    url(r'^user/$',user_home),
    url(r'^user/add$', user_add),
    url(r'^user/list$', user_list),
    url(r'^user/detail', user_detail),
    url(r'^user/delete', user_delete),
    url(r'^user/update', user_update),
    url(r'^user/export', user_export),
]

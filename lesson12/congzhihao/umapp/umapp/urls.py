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
from account.views import account_login,account_logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #account
    url(r'^account/login',account_login),
    url(r'^account/logout', account_logout),
    #user
    url(r'^user/home',user_home),
    url(r'^user/add', user_add),
    url(r'^user/list', user_list),
    url(r'^user/detail', user_detail),
    url(r'^user/delete/(?P<id>[0-9]+)/$', user_delete),
    url(r'^user/update/(?P<id>[0-9]+)/$', user_update),
    url(r'^user/export', user_export),
]

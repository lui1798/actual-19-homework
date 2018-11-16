"""webapp URL Configuration

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
#from django.urls import path, include
from dashboard.views import index
from assets.views import AssetsListView, AssetsAddView, AssetsEditView, AssetsDetailView, AssetsDeleteView, AssetsExportView
from account.views import AccountLoginView, AccountLogoutView
from user.views import UserListView, UserAddView, UserEditView, UserDetailView, UserDeleteView, UserExportView
from loganalysis.views import Testmul, Loganalysis

urlpatterns = [
    #admin
    url(r'^admin/', admin.site.urls),

    #assets
    url(r'^assets/list/$', AssetsListView),
    url(r'^assets/add/$', AssetsAddView),
    url(r'^assets/edit/(?P<pk>[0-9]+)/$', AssetsEditView),
    url(r'^assets/detail/$', AssetsDetailView),
    url(r'^assets/delete/(?P<pk>[0-9]+)/$', AssetsDeleteView),
    url(r'^assets/export/$', AssetsExportView),

    #user
    url(r'^user/list/$', UserListView),
    url(r'^user/add/$', UserAddView),
    url(r'^user/edit/(?P<pk>[0-9]+)/$$', UserEditView),
    url(r'^user/detail/$', UserDetailView),
    url(r'^user/delete/(?P<pk>[0-9]+)/$', UserDeleteView),
    url(r'^user/export/$', UserExportView),

    #loganalysis
    url(r'^test/mul/$', Testmul),
    url(r'^log/analysis/$', Loganalysis),

    #account
    url(r'^account/login/$', AccountLoginView),
    url(r'^account/logout/$', AccountLogoutView),

    #dashboard
    url(r'^$', index),
]

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
from api.views import hello
from api.views import commond,ccommond_v1,cssum,page,cat_cat,pagesum,pagesum_v2
from dashboard.views import index, command, hessum
from assets.views import assetsView, deleteAssetsView, AssetsListView, AssetsDeleteView, favicon, AssetsAddView, AssetsExportView, AssetsDetailView
from account.views import AccountLoginView, AccountLogoutView
from users.views import UserListView, UserDeleteView, UserAddView, UserDetailView, UserEditView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard', index),
    url(r'^assets$', assetsView),
    url(r'^assets/list$', AssetsListView),
    url(r'^assets/add', AssetsAddView),
    url(r'^assets/export', AssetsExportView),
    url(r'^assets/detail', AssetsDetailView),
    url(r'^assets/delete/(?P<pk>[0-9]+)/$', AssetsDeleteView),
    url(r'^index', index),
    url(r'^account/login', AccountLoginView),
    url(r'^account/logout', AccountLogoutView),

# user
    url(r'^users/list', UserListView),
    url(r'^users/add', UserAddView),
    url(r'^users/delete/(?P<pk>[0-9]+)/$', UserDeleteView),
    url(r'^users/detail/', UserDetailView),
    url(r'^users/edit/(?P<pk>[0-9]+)/$', UserEditView),

]

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
from django.conf.urls import url,include
from django.contrib import admin
from dashboard.views import index,command,s_sum
from assets.views import *
# from assets.views import assertView, AssetDeleteView,AssertAddView,AssetEditView,AssetListView,AssetDetailView, AssetsExportView
from api.views import hello,command_v1,command_v2,command_v3,ssum,pageSum,file,pageSum_v3,pageSum_v2
from account.views import AccountLoginView,AccountLogoutView
urlpatterns = [
    url(r'^$', index),
    # url(r'^command/', command),
    # url(r'^sum/', s_sum),

    url(r'^admin/', admin.site.urls),
    # url(r'^hello/',hello),
    # url(r'^command_v1/',command_v1),
    # url(r'^command_v2/',command_v2),
    # url(r'^command_v3/',command_v3),
    # url(r'^ssum/',ssum),
    # url(r'^pageSum/',pageSum),
    # url(r'^file/',file),
    # url(r'^pageSum_v2/',pageSum_v2),
    # url(r'^pageSum_v3/',pageSum_v3),
    url(r'^Assets/$',assertView),
    # url(r'^assets/delete/', AssetDeleteView),


    # url(r'^Assets/addView', addAssetView),
    url(r'^assets/add/', AssertAddView),
    url(r'^assets/list', AssetListView),
    url(r'^assets/delete/(?P<pk>[0-9]+)/$', AssetDeleteView),
    url(r'^assets/edit/(?P<pk>[0-9]+)/$', AssetEditView),
    url(r'^assets/detail', AssetDetailView),
    url(r'^assets/Export', AssetsExportView),

    url(r'^account/login/$', AccountLoginView),
    url(r'^account/logout', AccountLogoutView),



]

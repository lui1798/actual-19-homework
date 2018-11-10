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
from api.views import hello,command_v1,command_v3,command_v4,ssum_v1,catFile,pageSum_v1,pageSum
from assets.views import AssetsListView,AssetsDeleteView,AssetsAddView,AssetsDetailView,AssetsExportCsvView,AssetsEditView
from account.views import AccountLoginView,AccountLogoutView
from dashboard.views import index,command,ssum

#uri
urlpatterns = [
    url(r'^$', index),
    #assets
    url(r'^assets/list/$', AssetsListView),
    url(r'^assets/detail/(?P<pk>[0-9]+)/$', AssetsDetailView),
    url(r'^assets/delete/(?P<pk>[0-9]+)/$', AssetsDeleteView),
    url(r'^assets/add/$', AssetsAddView),
    url(r'^assets/edit/$', AssetsEditView),
    url(r'^assets/export/csv/$', AssetsExportCsvView),

    url(r'^ssum/$', ssum),
    url(r'^command/$', command),
    url(r'^ssum_v1/$', ssum_v1),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', hello),
    url(r'^command_v1/$',command_v1),
    url(r'^command_v3/$',command_v3),
    url(r'^command_v4/$', command_v4),

    url(r'^pageSum_v1/$', pageSum_v1),
    url(r'^pageSum/$', pageSum),
    url(r'^file/$', catFile),
    url(r'^dashboard/$', index),

    # url(r'^assets/$', assetsView) ,#$表示以什么结尾，^表示从什么开始
    # url(r'^assets/delete/$',deleteAssetsView ),
    # url(r'^assets/addpage/$', addPageAssetsView),
    # url(r'^assets/add/$',addAssetsView ),

    url(r'^account/login/$',AccountLoginView ),
    url(r'^account/logout/$',AccountLogoutView ),

]

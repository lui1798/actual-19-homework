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

from dashboard.views import IndexView
from account.views import AccountLoginView, AccountLogoutView

from assets.views import AssetsListView, AssetsDeleteView, AssetsEditView, AssetsAddView, AssetsDetailView, AssetsExportCsvView

# uri匹配
urlpatterns = [
    # admin
    url(r'^admin/', admin.site.urls),
    
    # dashboard
    url(r'^$', IndexView),
    
    # account
    url(r'^account/login/$', AccountLoginView),
    url(r'^account/logout/$', AccountLogoutView),
    
    # assets
    url(r'^assets/list/$', AssetsListView),
    url(r'^assets/detail/(?P<pk>\d+)/$', AssetsDetailView),
    url(r'^assets/add/$', AssetsAddView),
    url(r'^assets/edit/$', AssetsEditView),
    url(r'^assets/delete/$', AssetsDeleteView),
    url(r'^assets/export/csv/$', AssetsExportCsvView),
]

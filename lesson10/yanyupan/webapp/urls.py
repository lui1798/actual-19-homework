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
from django.conf.urls import url, include
from django.contrib import admin
from dashboard.views import index, ssum, command
from api.views import cmdView, sumView
from assets.views import assetsView, deleteAssetsView, addAssetsView, getAssetsView, editAssetsView
#
# urlpatterns = [
#     url(r'^$', index),
#     url(r'^api/', include('api.urls')),
#     url(r'^admin/', admin.site.urls),
#     url(r'^sum/', ssum),
#     url(r'^command/', command),
#     url(r'^assets/$', assetsView),
#     url(r'^assets/delete/$', deleteAssetsView),
#     url(r'^assets/add/$', addAssetsView),
#     url(r'^assets/get/$', getAssetsView),
#     url(r'^assets/edit/$', editAssetsView),
# ]

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^sum/', ssum),
    url(r'^command/', command),
    url(r'^assets/$', assetsView),
    url(r'^api/', include([
        url(r'^command/$', cmdView),
        url(r'^sum/$', sumView),
    ])),
    url(r'^assets/', include([
        url(r'^get/$', getAssetsView),
        url(r'^add/$', addAssetsView),
        url(r'^edit/$', editAssetsView),
        url(r'^delete/$', deleteAssetsView),
    ]))
]

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

from api.views import hello,command_v1,command_v2,command_v3,command_v4,file,pageSum,pageSum_v1,pageSum_v2
from dashboard.views import index
from assets.views import assetsView,assetsDelete

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^hello/', hello),
    url(r'^command_v1/', command_v1),
    url(r'^command_v2/', command_v2),
    url(r'^command_v3/', command_v3),
    url(r'^command_v4/', command_v4),
    url(r'^file/', file),

    url(r'^pageSum/', pageSum),
    url(r'^pageSum_v1/', pageSum_v1),
    url(r'^pageSum_v2/', pageSum_v2),
    url(r'^dashboard/', index),

    url(r'^assets/$', assetsView),
    url(r'^assets/delete/$', assetsDelete),


]

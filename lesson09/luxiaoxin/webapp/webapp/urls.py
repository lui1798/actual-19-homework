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
from api.views import login, login_ok, hello, page_command, command_V1, command_V2,  command_V3, pageSum, ssum, readfile
from dashboard.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login),
    url(r'^login_ok/', login_ok),
    url(r'^hello/', hello),
    url(r'^command_V1/', command_V1),
    url(r'^command_V2/', command_V2),
    url(r'^command_V3/', command_V3),
    url(r'^pagecom/', page_command),
    url(r'^pageSum/', pageSum),
    url(r'^ssum/', ssum),
    url(r'^readfile/', readfile),
    url(r'^dashboard/', index),
]

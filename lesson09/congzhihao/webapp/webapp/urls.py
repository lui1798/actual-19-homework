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
from api.views import hello,command_v1,command_v3,sssum,file_read
from api.views import page_sum1,page_sum2,page_sum3,page_sum4
from dashboard.views import index,ssum,cmd1,home



urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^hello/', hello),
    # url(r'^command_v1/', command_v1),
    # url(r'^command_v3/', command_v3),
    # url(r'^sum/', sssum),
    # url(r'^file/', file_read),
    # url(r'^page1/', page_sum1),
    # url(r'^page2/', page_sum2),
    # url(r'^page3/', page_sum3),
    # url(r'^page4/', page_sum4),
    url(r'^$', home),
    url(r'^index/', index),
    url(r'^ssum/', ssum),
    url(r'^cmd/', cmd1),
]

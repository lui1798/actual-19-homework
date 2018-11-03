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
from assets.views import assetsView, deleteAssetsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello', hello),
    url(r'^ccommond_v1', ccommond_v1),
    url(r'^commond', commond),
    url(r'^command', command),
    url(r'^pagesum_v2', pagesum_v2),
    url(r'^pagesum', pagesum),
    url(r'^hessum', hessum),
    url(r'^cssum', cssum),
    url(r'^page', page),
    url(r'^cat_cat', cat_cat),
    url(r'^dashboard', index),
    url(r'^assets$', assetsView),
    url(r'^assets/delete/$', deleteAssetsView),

]

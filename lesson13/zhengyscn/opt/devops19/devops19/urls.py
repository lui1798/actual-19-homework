"""devops19 URL Configuration

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


from ops.views import OpsView, OpsV2View, OpsV3View, OpsV4View

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ops/v1/', OpsView),
    url(r'^ops/v2/', OpsV2View),
    url(r'^ops/v3/', OpsV3View),
    url(r'^ops/v4/', OpsV4View),
]

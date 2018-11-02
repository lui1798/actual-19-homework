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
from dashboard.views import catfile,command,ssum,assetsadd
from api.views import apicatfile,apicommand,apissum
from assets.views import assetsView,assetsDelete,assetsAdd




urlpatterns = [
    url(r'^$', catfile),
    url(r'^ssum/', ssum),
    url(r'^api/ssum/', apissum),
    url(r'^command/', command),
    url(r'^api/command/', apicommand),
    url(r'^catfile', catfile),
    url(r'^api/catfile/', apicatfile),
    url(r'^admin/', admin.site.urls),

    url(r'^assets/$', assetsView),
    url(r'^assets/delete/$', assetsDelete),
    url(r'^assets/addpage/$', assetsadd),
    url(r'^assets/addassets/', assetsAdd),

]

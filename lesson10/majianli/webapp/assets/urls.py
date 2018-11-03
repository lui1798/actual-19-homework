from django.conf.urls import url

from . import assetsView

urlpatterns = [
    url(r'^$', views.assetsView),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^command', views.cmdView),
    url(r'^sum', views.sumView),
]
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^command', views.CmdApi),
    url(r'^sum', views.SumApi),
]


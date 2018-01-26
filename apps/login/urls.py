from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^processReg$', views.processReg, name="processReg"),
    url(r'^$', views.index, name="index")
]
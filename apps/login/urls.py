from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^processReg$', views.processReg, name="processReg"),
    url(r'^processLog$', views.processLog, name='processLog'),
    url(r'^logout$', views.logout),
    url(r'^success$', views.success)
]
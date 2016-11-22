from django.conf.urls import include, url
from . import views
from dbApp.views import *

urlpatterns = (
        url(r'^$', views.index, name='index'),
        url(r'^test/$', views.splashTest , name='new'),
        )

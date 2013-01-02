from django.conf.urls.defaults import *
from django.conf import settings
from django_siteanalytics import views

urlpatterns = patterns('',
    url(r'^test_index/$', views.test_index, name='test_index'),
)


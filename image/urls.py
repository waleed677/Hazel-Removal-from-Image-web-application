
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include 
from . import views

urlpatterns = [
  url(r'^$', views.index,name='index'),
  url(r'replace/$', views.replace, name='replace'),
  url(r'defogging/$', views.open_image, name='defogging')

]

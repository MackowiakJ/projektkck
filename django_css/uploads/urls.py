from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('data_analysis/', views.data_analysis, name='data_analysis'),
    url('petle/', views.petle, name='petle'),
    url('contact/', views.contact, name='contact'),
    url('listy/', views.listy, name='listy'),
    url('liczby/', views.liczby, name='liczby'),
]

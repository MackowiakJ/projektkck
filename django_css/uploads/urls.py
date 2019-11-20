from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('petle/', views.petle, name='petle'),
    url('funkcje/', views.funkcje, name='funkcje'),
    url('listy/', views.listy, name='listy'),
    url('liczby/', views.liczby, name='liczby'),
    url('klasy/', views.klasy, name='klasy'),
]

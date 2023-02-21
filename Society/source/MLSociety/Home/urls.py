from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home', views.home_page, name='home_page1'),
    path('us', views.about_page, name='about_page'),
    path('underconstruction', views.pythonpioneer_under_construction_page, name='underconstruction_page'),
]
from django.contrib import admin
from django.urls import path
from Solutions import views

urlpatterns = [
    path('', views.solutions_page, name='solution_page'),
]
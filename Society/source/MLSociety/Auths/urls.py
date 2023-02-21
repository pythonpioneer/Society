from django.urls import path
from Auths import views

urlpatterns = [
    path('signin', views.signin_page, name='signin_page'),
    path('signup', views.signup_page, name='signup_page'),
    path('profile', views.profile_page, name='profile_page'),
]

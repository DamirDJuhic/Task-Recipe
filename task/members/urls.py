from turtle import ontimer
from django.urls import path
from . import views


urlpatterns = [
    path('loginuser', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('registration', views.registeruser, name='registration'),
    ]

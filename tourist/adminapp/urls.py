from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.loginpage,name='loginpage'),
    path('register/', views.registerpage, name='registerpage'),
    path('about/',views.aboutpage,name='aboutpage'),
]

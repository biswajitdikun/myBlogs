# Inside your_app_name/urls.py
from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('contact',views.contact, name='contact')

]

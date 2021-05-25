"""
Definition of urls for monthlyproject.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('generic1/', views.generic1, name='generic1'),
    path('generic2/', views.generic2, name='generic2'),
    path('generic3/', views.generic3, name='generic3'),
    path('admin/', admin.site.urls),
]

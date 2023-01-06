from django.contrib import admin
from django.urls import path
from app_ecole.views import home



urlpatterns = [
    path('',home.index, name='home'),
    
]
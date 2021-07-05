from django.contrib import admin
from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('send/', views.send),
]

from django.contrib import admin
from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('login/', views.login),
    path('send/', views.send),
    path('getlogs/', views.get_log),
    path('getfriends/', views.getfriends)
]

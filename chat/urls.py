from django.contrib import admin
from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    path('friends/', views.get_friends_list, name='friends'),
    path('<str:dst_name>/', views.show_logs, name='showlog'),
]

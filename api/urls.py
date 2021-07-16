from django.contrib import admin
from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('login/', views.login, name="login"),
    path('send/', views.send, name="send"),
    path('getlogs/', views.get_log, name="getlogs"),
    path('getfriends/', views.getfriends, name="getfriends"),
    path('getrequests/', views.getrequests, name="getrequests"),
    path('allowrequest/', views.allowrequest, name="allowrequest"),
    path('denyrequest/', views.denyrequest, name="denyrequest"),
    path('addfriend/', views.addfriend, name="addfriend"),
]

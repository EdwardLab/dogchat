from django.contrib import admin
from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    path('<int:src_id>/<int:dst_id>/', views.showChatLog, name='showlog')
]

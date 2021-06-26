from django.shortcuts import render
import os 
import socket
import urllib.request
def home(request):
    context          = {}

    return render(request, 'index.html', {"disk":disk,"linux":linux,"username":username,"screenfetch":screenfetch,"ip":ip,"notice":notice})
    


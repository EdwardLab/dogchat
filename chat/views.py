from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from .models import ChatLog

# Create your views here.

def show_logs(request, dst_name):
    if not request.session.get('username'):
        return HttpResponseRedirect(reverse('users:login'))
    src = get_object_or_404(User, username=request.session['username'])
    dst = get_object_or_404(User, username=dst_name)
    return render(request, 'chat/chat.html', {'src':src, 'dst':dst, 'token':src.token})
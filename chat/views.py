from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from .models import ChatLog

# Create your views here.

def show_logs(request, dst_name):
    if not request.session.get('username'):
        return render(request,
            'redirect.html',
            {
                'url': reverse('users:login'),
                'reason': 'please log in first',
                'page_name':'login',
                'time': 3,
            })
    src = get_object_or_404(User, username=request.session['username'])
    dst = get_object_or_404(User, username=dst_name)
    logs1 = ChatLog.objects.filter(src=src, dst=dst)
    logs2 = ChatLog.objects.filter(src=dst, dst=src)
    logs = (logs1 | logs2).order_by('id')
    return render(request, 'chat/chat.html', {'logs':logs, 'src':src, 'dst':dst})

def send_msg(request, dst_name, msg):
    if not request.session.get('username'):
        return render(request,
            'redirect.html',
            {
                'url': reverse('users:login'),
                'reason': 'please log in first',
                'page_name':'login',
                'time': 3,
            })
    src = get_object_or_404(User, username=request.session['username'])
    dst = get_object_or_404(User, username=dst_name)
    ChatLog(src=src, dst=dst, content=msg).save()
    return HttpResponseRedirect(reverse('chat:showlog', args=(dst,)))

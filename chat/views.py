from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import translation
from django.urls import reverse

from users.models import User
from .models import ChatLog, Relation

# Create your views here.

def show_logs(request, dst_name):
    LANG = translation.get_language().replace('-', '_')
    translation.activate(LANG)
    if not request.session.get('username'):
        return HttpResponseRedirect(reverse('users:login'))
    src = get_object_or_404(User, username=request.session['username'])
    dst = get_object_or_404(User, username=dst_name)
    return render(request, 'chat/chat.html', {
        'src':src,
        'dst':dst,
        'token':src.token,
        'lang':LANG,
        'is_login':request.session.get('is_login')
    })

def get_friends_list(request):
    LANG = translation.get_language().replace('-', '_')
    translation.activate(LANG)
    if not request.session.get('username'):
        return HttpResponseRedirect(reverse('users:login'))
    src = get_object_or_404(User, username=request.session['username'])
    friend_list = Relation.objects.filter(src=src, status='friend')
    requests_list = Relation.objects.filter(dst=src, status='request')
    return render(request, 'chat/friends.html', {
        'token':src.token,
        'friends':friend_list,
        'requests':requests_list,
        'lang':LANG,
        'is_login':request.session.get('is_login')
        })

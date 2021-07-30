from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext as _
from django.utils import translation

from .models import User
from chat.models import Relation

# Create your views here.

def register(request):
    LANG = translation.get_language().replace('-', '_')
    translation.activate(LANG)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            return render(request, 'users/register.html', {
                'err_msg':_('No username or password entered'),
            })
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {
                'err_msg':_('User already exists'),
            })
        user = User(username=username, password=password)
        user.save()
        return HttpResponseRedirect(reverse('users:login'))
    else:
        return render(request, 'users/register.html', {
            'lang':LANG,
            'is_login':request.session.get('is_login')
            })

def login(request):
    LANG = translation.get_language().replace('-', '_')
    translation.activate(LANG)
    if request.session.get('is_login'):
        return HttpResponseRedirect(reverse('homepage:homepage'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            return render(request, 'users/login.html', {
                'err_msg':_('No username or password entered'),
            })
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'users/login.html', {
                'err_msg':_('wrong user name or password'),
            })
        if check_password(password, user.password):
            request.session['is_login'] = True
            request.session['uid'] = user.pk
            request.session['username'] = user.username
            request.session['password'] = user.password
            return HttpResponseRedirect(reverse('homepage:homepage'))
        return render(request, 'users/login.html', {
            'err_msg':_('wrong user name or password'),
        })
        
    else:
        return render(request, 'users/login.html', {
            'lang':LANG,
            'is_login':request.session.get('is_login')
        })

def logout(request):
    if request.session.get('is_login'):
        request.session.flush()
        return HttpResponseRedirect(reverse('users:login'))
    else:
        return HttpResponseRedirect(reverse('users:login'))

def search(request):
    LANG = translation.get_language().replace('-', '_')
    translation.activate(LANG)
    if request.method == 'GET':
        key = request.GET.get('name')
        if key == None:
            key = ''
        result = User.objects.filter(username__icontains=key)
        return render(request, 'users/search.html', {
            'req': key,
            'result':result,
            'lang':LANG,
            'is_login':request.session.get('is_login')
        })

def info(request, name):
    LANG = translation.get_language().replace('-', '_')
    translation.activate(LANG)
    if not request.session.get('is_login'):
        return HttpResponseRedirect(reverse('users:login'))
    dst = get_object_or_404(User, username=name)
    src = get_object_or_404(User, username=request.session['username'])
    if Relation.objects.filter(src=src, dst=dst, status='friend'):
        is_friend = 1
    else:
        is_friend = 0
    return render(request, 'users/info.html', {
        'lang':LANG,
        'is_login':request.session.get('is_login'),
        'dst':dst,
        'is_friend':is_friend,
        'token':src.token
    })

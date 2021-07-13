import secrets

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password

from .models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            return render(request, 'users/register.html', {
                'err_msg':'No username or password entered',
            })
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {
                'err_msg':'User already exists',
            })
        user = User(username=username, password=password, token=secrets.token_hex(16))
        user.save()
        return HttpResponse('ok')
    else:
        return render(request, 'users/register.html', {})

def login(request):
    if request.session.get('is_login'):
        return HttpResponse('You have already logged in')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            return render(request, 'users/login.html', {
                'err_msg':'No username or password entered',
            })
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'users/login.html', {
                'err_msg':'User does not exist',
            })
        if check_password(password, user.password):
            request.session['is_login'] = True
            request.session['uid'] = user.pk
            request.session['username'] = user.username
            request.session['password'] = user.password
            return HttpResponse('ok')
        return render(request, 'users/login.html', {
            'err_msg':'wrong user name or password',
        })
        
    else:
        return render(request, 'users/login.html', {})

def logout(request):
    if request.session.get('is_login'):
        request.session.flush()
        return HttpResponse('ok')
    else:
        return HttpResponse('You are not logged in')
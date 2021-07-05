from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password

from users.models import User
from chat.models import ChatLog

# Create your views here.

@csrf_exempt
def login(request):
    if request.method != 'GET':
        return JsonResponse({
            'code': 400,
            'msg': 'Wrong request method',
            'data': {}
        })
    try:
        username = request.GET['username']
        password = request.GET['password']
    except KeyError:
        return JsonResponse({
            'code': 400,
            'msg': 'Missing parameters',
            'data':{}
            })
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({
            'code': 404,
            'msg': 'User does not exist',
            'data': {}
        })
    if check_password(password, user.password):
        return JsonResponse({
            'code': 200,
            'msg': 'ok',
            'data': {
                'uid': user.pk,
                'username': user.username,
                'token': user.token
                }
            })
    return JsonResponse({
        'code': 403,
        'msg': 'Incorrect username or password',
        'data': {}
        })

@csrf_exempt
def send(request):
    if request.method != 'POST':
        return JsonResponse({
            'code': 400,
            'msg': 'Wrong request method',
            'data': {}
        })
    try:
        token = request.POST['token']
        dst_name= request.POST['dst_name']
        msg= request.POST['msg']
    except KeyError:
        return JsonResponse({
            'code': 400,
            'msg': 'Missing parameters',
            'data':{}
            })
    try:
        src = User.objects.get(token=token)
    except User.DoesNotExist:
        return JsonResponse({
            'code': 403,
            'msg': 'Incorrect token',
            'data': {}
        })
    try:
        dst = User.objects.get(username=dst_name)
    except User.DoesNotExist:
        return JsonResponse({
            'code': 404,
            'msg': 'User does not exist',
            'data': {}
        })
    ChatLog(src=src, dst=dst, content=msg).save()
    return JsonResponse({
        'code': 200,
        'msg': 'ok',
        'data': {}
    })

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password

from users.models import User
from chat.models import ChatLog, Relation

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
    if (relation := Relation.objects.filter(src=src, dst=dst)):
        if relation[0].status == "friend":
            ChatLog(src=src, dst=dst, content=msg).save()
            return JsonResponse({
                'code': 200,
                'msg': 'ok',
                'data': {}
            })
    else:
        return JsonResponse({
            'code': 403,
            'msg': 'You are not friends yet',
            'data': {}
        })
@csrf_exempt
def get_log(request):
    if request.method != 'GET':
        return JsonResponse({
            'code': 400,
            'msg': 'Wrong request method',
            'data': {}
        })
    try:
        token = request.GET['token']
        dst_name= request.GET['dst_name']
        id= request.GET['id']
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
    if (relation := Relation.objects.filter(src=src, dst=dst)):
        if relation[0].status == "friend":
            log1 = ChatLog.objects.filter(src=src, dst=dst, id__gt=id)
            log2 = ChatLog.objects.filter(src=dst, dst=src, id__gt=id)
            logs = log1 | log2
            log_list = [ {'id':i.pk, 'src':i.src.username, 'dst':i.dst.username, 'msg':i.content} for i in logs ]
            return JsonResponse({
                'code': 200,
                'msg': 'ok',
                'data': {'logs': log_list}
            })
    else:
        return JsonResponse({
            'code': 403,
            'msg': 'You are not friends yet',
            'data': {}
        })

@csrf_exempt
def getfriends(request):
    if request.method != 'GET':
        return JsonResponse({
            'code': 400,
            'msg': 'Wrong request method',
            'data': {}
        })
    try:
        token = request.GET['token']
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
    lists = [ i.dst.username for i in Relation.objects.filter(src=src) ]
    return JsonResponse({
            'code': 200,
            'msg': 'ok',
            'data': {'friends':lists}
        })

@csrf_exempt
def getfriends(request):
    if request.method != 'GET':
        return JsonResponse({
            'code': 400,
            'msg': 'Wrong request method',
            'data': {}
        })
    try:
        token = request.GET['token']
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
    lists = [ i.dst.username for i in Relation.objects.filter(src=src, status='friend') ]
    return JsonResponse({
            'code': 200,
            'msg': 'ok',
            'data': {'friends':lists}
        })

@csrf_exempt
def getrequests(request):
    if request.method != 'GET':
        return JsonResponse({
            'code': 400,
            'msg': 'Wrong request method',
            'data': {}
        })
    try:
        token = request.GET['token']
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
    lists = [ i for i in Relation.objects.filter(dst=src, status='request') ]
    return JsonResponse({
            'code': 200,
            'msg': 'ok',
            'data': {
                'requests': [ {'id': i.pk, 'src': i.src.username} for i in lists]
            }
        })

@csrf_exempt
def allowrequest(request):
    if request.method != 'POST':
        return JsonResponse({
            'code': 400,
            'msg': 'Wrong request method',
            'data': {}
        })
    try:
        token = request.POST['token']
        id = request.POST['id']
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
        request = Relation.objects.get(pk=id)
    except Relation.DoesNotExist:
        return JsonResponse({
            'code': 404,
            'msg': 'The Requests does not exist',
            'data': {}
        })
    request.status = 'friend'
    Relation(src=src, dst=request.src, status='friend').save()
    request.save()
    return JsonResponse({
            'code': 200,
            'msg': 'ok',
            'data': {}
        })

@csrf_exempt
def denyrequest(request):
    if request.method != 'POST':
        return JsonResponse({
            'code': 400,
            'msg': 'Wrong request method',
            'data': {}
        })
    try:
        token = request.POST['token']
        id = request.POST['id']
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
        request = Relation.objects.get(pk=id)
    except Relation.DoesNotExist:
        return JsonResponse({
            'code': 404,
            'msg': 'The Requests does not exist',
            'data': {}
        })
    request.delete()
    return JsonResponse({
            'code': 200,
            'msg': 'ok',
            'data': {}
        })

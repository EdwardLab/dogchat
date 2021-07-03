from django.shortcuts import render, get_object_or_404

from users.models import User
from .models import ChatLog

# Create your views here.

def showChatLog(requests, src_id, dst_id):
    src = get_object_or_404(User, pk=src_id)
    dst = get_object_or_404(User, pk=dst_id)
    logs = ChatLog.objects.filter(src=src, dst=dst)
    return render(requests, 'chat/chat.html', {'logs':logs})

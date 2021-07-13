import json
import time
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import ChatLog, Relation
from users.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.id = 0

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        flag = 0
        data = json.loads(text_data)
        src = await sync_to_async(User.objects.get)(token=data['token'])
        dst=await sync_to_async(User.objects.get)(username=data['dst_name'])
        if (relation := await sync_to_async(Relation.objects.filter)(src=src, dst=dst)):
            print(111)
            if relation.status == "friend":
                flag = 1
        else:
            await self.send(text_data=json.dumps({
                "src": "dogchat",
                "dst": src.username,
                "msg": "You are not friends yet"
                }))
        while flag:
            logs1=await sync_to_async(ChatLog.objects.filter)(src=src, dst=dst)
            logs2=await sync_to_async(ChatLog.objects.filter)(src=dst, dst=src)
            logs = logs1 | logs2
            for i in await sync_to_async(logs.filter)(pk__gt=self.id):
                await self.send(text_data=json.dumps({
                    "src": i.src.username,
                    "dst": i.dst.username,
                    "msg": i.content
                    }))
                self.id=i.id

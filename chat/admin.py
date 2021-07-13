from django.contrib import admin

from chat.models import ChatLog, Relation
# Register your models here.

admin.site.register(ChatLog)
admin.site.register(Relation)
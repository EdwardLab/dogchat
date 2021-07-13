from django.db import models

from users.models import User

# Create your models here.

class ChatLog(models.Model):
    src = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_src')
    dst = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_dst')
    content = models.CharField(max_length=1300)
    
    def save(self, *args, **kwargs):
        self.content = self.content.replace('<', '&lt;').replace('>', '&gt;')
        super(ChatLog, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.src}->{self.dst} {self.content[:5]}..."

class Relation(models.Model):
    src = models.ForeignKey(User, on_delete=models.CASCADE, related_name='relation_src')
    dst = models.ForeignKey(User, on_delete=models.CASCADE, related_name='relation_dst')
    status = models.CharField(max_length=1300)

    def __str__(self):
        return f"{self.src} ->{self.dst} {self.status}"

from django.db import models

from users.models import User

# Create your models here.

class ChatLog(models.Model):
    src = models.ForeignKey(User, on_delete=models.CASCADE, related_name='src')
    dst = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dst')
    content = models.CharField(max_length=1300)

    def __str__(self):
        return f"{self.src}->{self.dst} {self.content[:5]}..."

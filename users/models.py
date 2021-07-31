import secrets

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    token = models.CharField(max_length=32)
    email = models.EmailField()
    active = models.CharField(max_length=4)
    tmp_token = models.CharField(max_length=32)

    def save(self, *args, **kwargs):
        self.token = secrets.token_hex(16)
        self.tmp_token = secrets.token_hex(16)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

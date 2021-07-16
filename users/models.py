import secrets

from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    token = models.CharField(max_length=32)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password, None, 'pbkdf2_sha256')
        self.token = secrets.token_hex(16)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

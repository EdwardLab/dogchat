from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from .models import User

# Create your tests here.

def CreateUser(username, password):
    return User.objects.create(username=username, password=password)

class LoginTest(TestCase):
    def test_login(self):
        user = CreateUser('test', 'test')
        data = {'username':'test', 'password':'test'}
        res = self.client.post(reverse('users:login'), data=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context, None)
        self.assertEqual(self.client.session['is_login'], True)
        self.assertEqual(self.client.session['uid'], user.pk)
        self.assertEqual(self.client.session['password'], user.password)

    def test_login_without_username(self):
        data = {'username':'', 'password':'test'}
        res = self.client.post(reverse('users:login'), data=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context.get('err_msg'), "No username or password entered")

    def test_login_without_password(self):
        data = {'username':'test', 'password':''}
        res = self.client.post(reverse('users:login'), data=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context.get('err_msg'), "No username or password entered")
    
    def test_login_does_not_exist_user(self):
        data = {'username':'test', 'password':'test'}
        res = self.client.post(reverse('users:login'), data=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context.get('err_msg'), "User does not exist")
    
    def test_login_with_wrong_password(self):
        user = CreateUser('test', 'test')
        data = {'username':'test', 'password':'test1'}
        res = self.client.post(reverse('users:login'), data=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context.get('err_msg'), "wrong user name or password")

class RegisterTest(TestCase):
    def test_register(self):
        data = {'username':'test', 'password':'test1'}
        res = self.client.post(reverse('users:register'), data=data)
        self.assertEqual(res.context, None)
        users = User.objects.all()
        self.assertEqual(users[0].username, 'test')

    def test_register_without_username(self):
        data = {'username':'', 'password':'test'}
        res = self.client.post(reverse('users:register'), data=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context.get('err_msg'), "No username or password entered")

    def test_register_without_password(self):
        data = {'username':'test', 'password':''}
        res = self.client.post(reverse('users:register'), data=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context.get('err_msg'), "No username or password entered")

    def test_register_existing_user(self):
        CreateUser('test', 'test')
        data = {'username':'test', 'password':'test'}
        res = self.client.post(reverse('users:register'), data=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context.get('err_msg'), "User already exists")
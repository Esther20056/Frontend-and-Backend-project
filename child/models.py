from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

#  Create your models here.
class Post(models.Model):
    
    description = models.TextField()
    title = models.CharField(max_length=40)
    datePosted = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="post")
    other = models.ImageField(upload_to="post", default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name="reguser")
    active = models.BooleanField(default= False)

class students(models.Model):
    firstname = models.CharField(max_length=20, null=False, default="")
    email = models.EmailField(unique =True)
    age = models.IntegerField()
    active = models.BooleanField(default =True)
    photo = models.ImageField()
    video = models.FileField
    date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    fees = models.DecimalField(max_digits=5, decimal_places=2)
    about = models.TextField()

class login(models.Model):
    first_name =models.CharField(max_length=50, default="")
    passsword = models.CharField(max_length=50)


class User(AbstractUser):
    photo = models.ImageField(upload_to='profile')
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
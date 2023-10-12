from django.db import models
from django.conf import settings

# Create your models here.
class post(models.Model):
    
    description = models.TextField()
    title = models.CharField(max_length=40)
    datePosted = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="post")
    other = models.ImageField(upload_to="post", default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    active = models.BooleanField(default= True)

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    body = models.TextField()
    image= models.ImageField(upload_to='images/')
    created_on=models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
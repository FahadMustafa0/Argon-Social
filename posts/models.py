from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone, tree
from profiles.models import profile

class Post(models.Model):
    body = models.TextField()
    image= models.ImageField(upload_to='images/')
    created_on=models.DateTimeField(default=timezone.now)
    private = models.BooleanField(default=False)
    # author= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    author1= models.ForeignKey(profile, on_delete=models.CASCADE,null=True)
    # auth=models.CharField( default=User , max_length=200, null=True , blank=True)

    class Meta:
        ordering = ('-created_on',)
    
    def __str__(self):
        return str(self.body)[:30]
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import RelatedField
from django.utils import timezone
from .utils import get_random_code
from django.template.defaultfilters import slugify

class profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    followers = models.ManyToManyField(User, related_name='follower', blank=True)


    bio = models.TextField(default="no bio...",max_length=300)
    email = models.EmailField(blank=True,max_length=200)
    country = models.TextField(blank=True,max_length=200, default='Pakistan')
    avatar = models.ImageField(default='avatar.png',upload_to='avatars/')
    # friends = models.ManyToManyField(User,blank=True,related_name='firends')
    slug = models.SlugField(unique=True , blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # ---------new------------
    def profile_posts(self):
        return self.post_set.all()
    class Meta:
        ordering = ('-created',)

   

    def get_following(self):
        return self.following.all()
    
    def get_followers(self):
        return self.followers.all()


    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"

    def save(self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
                to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
                ex = profile.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    ex = profile.objects.filter(slug=to_slug).exists()
        else:
                to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs) 



STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class Relationship(models.Model):
    sender = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # is_active = models.BooleanField(label='Active?')
    

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
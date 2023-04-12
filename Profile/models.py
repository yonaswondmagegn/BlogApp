from django.db import models
from django.conf import settings
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(default='profile_default.jpg',upload_to='profile_pics')
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="followers")
    profetion = models.CharField(max_length=225)
    date = models.DateTimeField(default=timezone.now)

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class BlogImageFragment(models.Model):
    first = (
        ('T','TEXT'),
        ('I','IMAGE')
    )
    text = models.TextField(null=True)
    image = models.ImageField(upload_to='fragment_images',null=True)
    image_link = models.TextField(null=True,blank=True)
    first_is = models.CharField(max_length=1,choices=first,default='T')
    order = models.IntegerField(null=True)
    date = models.DateTimeField(default=timezone.now)


class BlogVideoFragment(models.Model):
    first = (
        ('T','TEXT'),
        ('V','VIDEO')
    )
    text = models.TextField()
    video = models.FileField(
        upload_to='fragment_videos',
        validators=[FileExtensionValidator(allowed_extensions=['MP4'])],
        null=True,
        blank=True
        )
    video_link = models.TextField(null=True,blank=True)
    order = models.IntegerField()
    date  = models.DateTimeField(default=timezone.now)


class BlogLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


class Blog(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    images = models.ManyToManyField(
        BlogImageFragment,
        related_name="images_fragments",
        blank=True
        )
    likes = models.ManyToManyField(BlogLike,blank=True,related_name='likes')
    videos = models.ManyToManyField(BlogVideoFragment,related_name='video_fragments',blank=True)
    gener = models.CharField(max_length=225,null=True)
    
    date = models.DateTimeField(default=timezone.now)



# the review model for the blog model 

class CommentLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


class BlogComment(models.Model):
    type = (
        ('O','ORIGINALCOMMENT'),
        ('R','REPLAY')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,null=True)
    comment_type = models.CharField(choices=type,max_length=1)
    replay_for = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    text = models.TextField()
    likes = models.ManyToManyField(CommentLike,blank=True,related_name='comment_likes')
    date = models.DateTimeField(default=timezone.now)





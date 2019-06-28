from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES=[['draft','Draft'],['published','Published']]
    title = models.CharField(max_length=75)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    publish = models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Draft')
    tag=TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_details',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])

    # def total_absolute_url(self):
    #     url=build_absolute_uri(self.get_absolute_url)
    #     return url

class Comment(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    body=models.CharField(max_length=120)
    email=models.EmailField()
    active=models.BooleanField(default=True)
    name=models.CharField(max_length=80)

    def __str__(self):
        return "Comment by {} at {}".format(self.name,self.created)

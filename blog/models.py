from operator import mod
from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    content = models.TextField(max_length=250)
    created_at =models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'blogs/' )
    category = models.ForeignKey("Category" , related_name='blog' , on_delete=models.CASCADE , blank=True , null=True)
    tags = models.ManyToManyField("Tag" , related_name='tag', blank=True)
    def __str__(self):
        return self.title
    

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    published_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField( max_length=50) 
    slug = models.SlugField()
    published_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title   

class Comments(models.Model):
    blog = models.ForeignKey("Blog" , related_name="comments" , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
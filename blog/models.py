from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)  
class Category(models.model):
    name = models.CharField(max_length=50)    

    def __str__(self):
        return self.name
class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status='published')
        
    options = (
         ('draft', 'Draf')
         ('published', 'Published'),
     )   
        


    Category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    tittle = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    Content = models.TextField()
    slug = models.SlugField(max_length=250,unique_for_date='published', null=False, unique=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.manager()
    PostObjects = PostObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.tittle
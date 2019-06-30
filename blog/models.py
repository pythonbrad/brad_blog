from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    contains = models.TextField(default='')
    pub_date = models.DateTimeField(default=timezone.now)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/', default=None)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    contains = models.TextField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/', default=None)

    def __str__(self):
        return self.contains

    class Meta:
        ordering = ['-pub_date']

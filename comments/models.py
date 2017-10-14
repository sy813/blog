from django.db import models
from django import forms


# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    article = models.ForeignKey('myblog.Article')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        verbose_name = '文章'
        return self.text[:20]

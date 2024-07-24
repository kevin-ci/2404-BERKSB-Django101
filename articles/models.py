from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    headline = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    copy = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'"{self.headline}" by {self.author}'
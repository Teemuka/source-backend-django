from django.db import models
from django.contrib.auth.models import User


class NewsText(models.Model):
    title = models.CharField(max_length=50, unique=True)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(editable=True)

    def __str__(self):
        return self.title


class Happening(models.Model):
    title = models.CharField(max_length=50, unique=True)
    date = models.DateField(editable=True)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(editable=True)

    def __str__(self):
        return self.title


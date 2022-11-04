from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Project(models.Model):
    title       = models.CharField(max_length = 200)
    description = models.TextField()
    technology  = models.CharField(max_length = 200)
    created_at  = models.DateTimeField(auto_now_add = True)
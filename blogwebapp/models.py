from django.db import models
from datetime import datetime
# Create your models here.
class blogpage(models.Model):
    title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=datetime.now())
    content = models.TextField()
    def __str__(self):
        return self.title

class nusers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField()
    def __str__(self):
        return self.name
    
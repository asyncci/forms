from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=None)
    price = models.CharField(max_length=10)


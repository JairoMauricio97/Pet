from django.db import models

# Create your models here.

class Perrito(models.Model):
    nombre= models.CharField(max_length=100)
    edad= models.CharField(max_length=100)
    historia=models.TextField()
    imagen=models.FilePathField(path='/img')

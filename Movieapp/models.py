from django.db import models

# Create your models here.

class DataDB(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=10)
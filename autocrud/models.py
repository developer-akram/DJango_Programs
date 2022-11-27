from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=50)
# Create your models here.

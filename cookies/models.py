from django.db import models

class Employee(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    mobile = models.IntegerField()
# Create your models here.

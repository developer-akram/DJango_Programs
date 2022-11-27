from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Faculty(models.Model):
    cfk = models.ForeignKey(Course, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

# Create your models here.

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Faculty(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} [{self.course}]" 

class Student(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    rating = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return f"{self.name} Faculty -> {self.faculty} || rating -> [{self.rating}]" 
# Create your models here.

from django.db import models

class StudentNew(models.Model):
    rno = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 50)
    fees = models.IntegerField()

    def __str__(self):
        return f"Roll : {self.rno}, Name : {self.name}, Branch : {self.branch}, Fees : {self.fees}"

class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    mobile_no = models.CharField(max_length = 50)

class StudentRegistration(models.Model):
    name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50, default='')
    mobile = models.IntegerField()
    country = models.CharField(max_length = 50)
    states = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    qualification = models.CharField(max_length = 50)
    courses = models.CharField(max_length = 50)
    message = models.CharField(max_length = 50)
    
    def __str__(self):
        return f"Name : {self.name}, Gender : {self.gender}, Email : {self.email}, Mobile : {self.mobile}, Country : {self.country} States : {self.states} city : {self.city} Qualification : {self.qualification} Courses : {self.courses} Message : {self.message}"

class Courses(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Faculty(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ------- {self.rating}"
  
# Create your models here.


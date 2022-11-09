from django.db import models

class StudentNew(models.Model):
    rno = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 50)
    fees = models.IntegerField()

    def __str__(self):
        return f"Roll : {self.rno}, Name : {self.name}, Branch : {self.branch}, Fees : {self.fees}"


class StudentRegistration(models.Model):
    name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 50)
    mobile = models.IntegerField()
    country = models.CharField(max_length = 50)
    states = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    qualification = models.CharField(max_length = 50)
    courses = models.CharField(max_length = 50)
    message = models.CharField(max_length = 50)
    
    def __str__(self):
        return f"Name : {self.name}, Gender : {self.gender}, Mobile : {self.mobile}, Country : {self.country} States : {self.states} city : {self.city} Qualification : {self.qualification} Courses : {self.courses} Message : {self.message}"
# Create your models here.

from django.db import models
class Student(models.Model):
    rno = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    fees = models.IntegerField()
    def __str__(self):
        return "rno is " + str(self.rno) + " name is "+str(self.name) + "branch is "+self.branch + "fees is " + str(self.fees)

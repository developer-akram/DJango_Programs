from django.db import models

class StudentNew(models.Model):
    rno = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 50)
    fees = models.IntegerField()

    def __str__(self):
        return f"Roll : {self.rno}, Name : {self.name}, Branch : {self.branch}, Fees : {self.fees}"

# Create your models here.

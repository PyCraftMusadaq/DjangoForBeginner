from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True 

class Student(CommonInfo):
    fees= models.IntegerField()
    date = None

    def __str__(self):
        return self.name  

class Teacher(CommonInfo):
    salary = models.IntegerField()

    def __str__(self):
        return self.name 


class Contractor(CommonInfo):
    date = models.DateTimeField()
    payment = models.IntegerField()

    def __str__(self):
        return self.name 
    
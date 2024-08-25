from django.db import models
from .managers import CustomManager
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    objects = models.Manager()
    

    def __str__(self):
        return self.name 

# We make proxy model to set behavior different for same models    
class ProxyStudent(Student):
    students = CustomManager()
    class Meta:
        proxy = True 
        ordering = ['name']
    
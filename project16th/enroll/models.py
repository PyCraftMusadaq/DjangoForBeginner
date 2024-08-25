from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=70)
    student_email = models.EmailField(max_length=100)
    student_pass = models.CharField(max_length=70)
    
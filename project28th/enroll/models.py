from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50) # add attribute blank=True  if you want to omite the require field in the form.
    email = models.EmailField()
    password = models.CharField(max_length=50)
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE) # write models.PROTECT if you want to prevent the user to delete the posts 
    post_title = models.CharField(max_length=70)
    post_category = models.CharField(max_length=70)
    post_publish_date = models.DateField()


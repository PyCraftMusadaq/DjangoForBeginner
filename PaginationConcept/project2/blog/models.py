from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    publish_date = models.DateTimeField()
    

    def __str__(self):
        return self.title 
    
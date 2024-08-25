from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Page(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE,primary_key=True)
    page_name = models.CharField(max_length=70)
    page_category = models.CharField(max_length=70)
    page_publish_date = models.DateField()

    def __str__(self):
        return self.page_name 
    
class Like(Page):
    page = models.OneToOneField(to=Page,on_delete=models.CASCADE,primary_key=True,parent_link=True)
    likes = models.IntegerField()

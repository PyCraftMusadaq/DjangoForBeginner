from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE,primary_key=True,related_name="mypage")
    page_name = models.CharField(max_length=70)
    page_category = models.CharField(max_length=70)
    page_publish_date = models.DateField()

    def __str__(self):
        return self.page_name 
    
class Post(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="mypost")
    post_title = models.CharField(max_length=70)
    post_category = models.CharField(max_length=70)
    post_publish_date = models.DateField()


    def __str__(self):
        return self.post_title
    
class Song(models.Model):
    singer = models.ManyToManyField(to=User,related_name="mysong")
    song_title = models.CharField(max_length=70)
    song_duration = models.IntegerField()

    def __str__(self):
        return self.song_title 
    
    def written_by(self):
        return ", ".join([str(s) for s in self.singer.all()])
    

from django.shortcuts import render
from django.contrib.auth.models import  User
from .models import Song,Post,Page
# Create your views here.

def home(request):
    return render(request,"myapp/home.html")

def show_user_data(request):
    # apply same filter with other views functions and get that data from template side
    data1 = User.objects.all()
    data2 = User.objects.filter(email='attofa@gmail.com')
    data3 = User.objects.filter(mypage__page_category="Programming")
    data4 = User.objects.filter(post__post_publish_date="2024-04-01")
    data5 = User.objects.filter(song__song_duration=5)
    return render(request,"myapp/user.html",context={"data":data1,"data2":data2,"data3":data3,"data4":data4,"data5":data5})


def getsongs(request):
    songs = Song.objects.all()
    return render(request,"myapp/song.html",context={"songs":songs})

def getposts(request):
    posts = Post.objects.all()
    return render(request,"myapp/post.html",context={"posts":posts})

def getpages(request):
    pages = Page.objects.all()
    return render(request,"myapp/page.html",context={"pages":pages})


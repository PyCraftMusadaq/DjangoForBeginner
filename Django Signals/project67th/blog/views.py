from django.shortcuts import render, HttpResponse 
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from .forms import SignUpForm, LoginForm, DBForm
from django.contrib import messages 
from .models import POST 
from django.contrib.auth.models import Group
from django.core.cache import cache  
# Create your views here.
def home(request):
    posts = POST.objects.all()

    return render(request,"blog/home.html",context={'posts':posts})


def about(request):
    return render(request,"blog/about.html")

def contact(request):
    return render(request,"blog/contact.html")

def dashboard(request):
    if request.user.is_authenticated:
        posts = POST.objects.all()
        user = request.user 
        fname = user.get_full_name()
        groups = user.groups.all()
        ip = request.session.get('ip')
        count = cache.get('count',version=user.pk)
        return render(request,"blog/dashboard.html",{"posts":posts,"fname":fname,"groups":groups,'ip':ip,'count':count})
    else:
        return HttpResponseRedirect('/signin/')

def user_logout(request):
    if request.user.is_authenticated:
       logout(request)
       return  HttpResponseRedirect('/signin/')
    else:
        return HttpResponseRedirect("/signin/")
    
def signin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.add_message(request,messages.SUCCESS,"Successfully Logged In")
                    return HttpResponseRedirect('/dashboard/')
            else:
                messages.add_message(request,messages.ERROR,"Invalid Credentials!")
                return render(request,"blog/login.html",{'form':form})
        else:
            form = LoginForm()
            return render(request,"blog/login.html",{"form":form})
    else:
        return HttpResponseRedirect('/dashboard/')

def signup(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="Authors")
            user.groups.add(group)
            messages.add_message(request,messages.SUCCESS,"You Have Become Author!")
            return HttpResponseRedirect("/signup/")
        else:
            return render(request,"blog/signup.html",{'form':form})
    else:
        form = SignUpForm()
        return render(request,"blog/signup.html",{"form":form})
    


# Add new Post 
def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DBForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = POST(title=title,desc=desc)
                pst.save()
                form = DBForm()
                return HttpResponseRedirect('/dashboard/')
        else:
            form = DBForm()
            return render(request, "blog/addpost.html",{'form':form}) 
    else:
        return HttpResponseRedirect("/signin/")
    
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pst = POST.objects.get(pk=id)
            form = DBForm(request.POST,instance=pst)
            if form.is_valid():
               form.save()
               return HttpResponseRedirect('/dashboard/')
        else:
            post = POST.objects.get(pk=id)
            form = DBForm(instance=post)
        return render(request,"blog/updatepost.html",{'form':form})
    else:
        return HttpResponseRedirect('/signin/')
    
def deletepost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = POST.objects.get(pk=id)
            post.delete()
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponse("Sorry You are not authorized")
    else:
        return HttpResponseRedirect('/signin/')
    
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
# We will use authenticate function to authenticate the use and if it is authenticated then we will use the login function 

# Create your views here.

def signup(request):
    if request.method=='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,"Account created Successfully!!")
    else:
        fm = SignUpForm()
    return render(request,"enroll/index.html",{"title":"Signup","form":fm})


# Login view function 
def login_user(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                print("test")
                uname = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=uname,password=password)
                print("Testing part")
                if user is not None:
                    login(request, user)
                    messages.add_message(request,messages.SUCCESS,"Authentication completed!!")
                    return HttpResponseRedirect('/profile/')
            else:
                messages.add_message(request,messages.ERROR,"Sorry Invalid Credentials!")
                return render(request,"enroll/loginform.html",{"form":fm})
        else:
            fm = AuthenticationForm()
        return render(request,"enroll/loginform.html",{"title":"Login","form":fm})
    else:
        return HttpResponseRedirect('/profile/')


# Loging profile of user 
def user_profile(request):
    if request.user.is_authenticated:  
        return render(request,"enroll/profile.html",{"name":request.user})
    else:
        return HttpResponseRedirect('/signin/')


# Logout view 
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/signin/') 

##  hoorain vsach i


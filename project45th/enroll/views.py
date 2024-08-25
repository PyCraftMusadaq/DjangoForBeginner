from django.shortcuts import render
from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group  
# Create your views here.

# Creating Signup form function 
def signupform(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="Editor")
            user.groups.add(group)
            messages.add_message(request,messages.SUCCESS,"Account Created Successfully!!")
        else:
            messages.add_message(request,messages.ERROR,"Invalid Credentials Detected!")
    else:
        form = SignUpForm()
    return render(request,"enroll/signup.html",{"form":form})


def signinform(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password= upass)
                if user is not None:
                    login(request, user)
                    messages.add_message(request,messages.SUCCESS,"Authentication completed!!")
                    return HttpResponseRedirect('/dashboard/')
            else:
                messages.add_message(request,messages.ERROR,"Sorry invalid Credentials!")
                return render(request,"enroll/signin.html",{"form":form})     
        else:
            form = AuthenticationForm()
            return render(request,"enroll/signin.html",{"form":form})
    else:
        return HttpResponseRedirect('/dashboard/')


def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request,"enroll/dashboard.html",context={"user":request.user.username})
        pass 
    else:
        return HttpResponseRedirect('/signin/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')

# change password with old password 
 

def user_detail(request, id):
    if request.user.is_authenticated:
        user_dt = User.objects.get(pk=id)
        form = EditAdminProfileForm(instance=user_dt)
        return render(request,"enroll/userdetail.html",context={"form":form})
    else:
        return HttpResponseRedirect('/signin/')
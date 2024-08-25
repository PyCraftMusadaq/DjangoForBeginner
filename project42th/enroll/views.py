from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect
# Create your views here.

# Creating Signup form function 
def signupform(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
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
                    return HttpResponseRedirect('/profile/')
            else:
                messages.add_message(request,messages.ERROR,"Sorry invalid Credentials!")
                return render(request,"enroll/signin.html",{"form":form})     
        else:
            form = AuthenticationForm()
            return render(request,"enroll/signin.html",{"form":form})
    else:
        return HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request,"enroll/profile.html",{"name":request.user})
    else:
        return HttpResponseRedirect('/signin/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')

# change password with old password 
def change_password(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = PasswordChangeForm(user = request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.add_message(request,messages.SUCCESS,"Password Changed Successfully")
                return HttpResponseRedirect('/profile/')
            else:
                form = PasswordChangeForm(user=request.user)
                messages.add_message(request,messages.ERROR,"Sory invalid credentials!!")
                return render(request,"enroll/changepassword1.html",{"form":form})
        else:
            form = PasswordChangeForm(user=request.user)
            return render(request,"enroll/changepassword1.html",{"form":form}) 
    else:
        return HttpResponseRedirect('/signin/')
    

def change_password2(request):
    if request.method == "POST":
        form = SetPasswordForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.add_message(request, messages.SUCCESS,"Password updated Successfully")
            return HttpResponseRedirect('/profile/')
        else:
            messages.add_message(request,messages.ERROR,"Sorry invalid Credentials")
        return render(request,"enroll/changgepassword2.html",{"form":form})
    else:
        form = SetPasswordForm(user = request.user)
        return render(request,"enroll/changgepassword2.html",{"form":form})
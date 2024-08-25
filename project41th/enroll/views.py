from django.shortcuts import render
from .forms import SignUpForm, ChangePassword # the changepassword is manual made form 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.http import HttpResponseRedirect
# Create your views here.

# Signup Form 
def SignUp(request):
    if request.method=='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,"User Registered Successfully!")
    else:
        fm = SignUpForm()
    return render(request,"enroll/Signup.html",{"form":fm})


def SignIn(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
            else:
                messages.add_message(request,messages.ERROR,"Sorry Invalid Credentials")
                return render(request,"enroll/login.html",context = {"form":fm})
        else:
            fm = AuthenticationForm()
            return render(request,"enroll/login.html",{"form":fm})        
    else:
        return HttpResponseRedirect('/profile/')

def user_profile(request):
    if request.user.is_authenticated:
        return render(request,"enroll/profile.html",{"name":request.user})
    else:
        return HttpResponseRedirect('/login/')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

 #change password with old password
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # if we change the password it will do auto logout but if we want to main the session we will use following session function 
                update_session_auth_hash(request,fm.user)

                messages.add_message(request, messages.SUCCESS,"Password Changed Successfully!")
                return HttpResponseRedirect('/profile/')
            else:
                messages.add_message(request,messages.ERROR,"Sorry Invalid Credentials!")
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,"enroll/change_password.html",{"form":fm})
    else:
        return HttpResponseRedirect('/login/')
    

# Change password without old password 
def change_pass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
            else:
                messages.add_message(request,messages.ERROR,"Sorry Invalid Credentials ")
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
            return render(request,"enroll/changepassword1.html",{"form":fm})
    else:
        return HttpResponseRedirect('/login/')
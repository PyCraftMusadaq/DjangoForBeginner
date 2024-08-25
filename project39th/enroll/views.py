from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUpForm, UserAuthentication
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout 

# Create your views here.

# SignUp views 
def signup(request):
    if request.method=='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Account Created Successully!!')
    else:
        fm = SignUpForm()
    return render(request,"enroll/index.html",{'form':fm})

# Login View 
def user_login(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            authform = AuthenticationForm(request=request,data=request.POST)
            if authform.is_valid():
                print("Data Validated")
                uname = authform.cleaned_data['username']
                upassword = authform.cleaned_data['password']
                #print(uname,"\n",upassword)
                user = authenticate(username=uname, password=upassword)
                if user is not None:
                    login(request,user)
                    messages.add_message(request,messages.SUCCESS,"Logged In Successfully")
                    return HttpResponseRedirect("/profile/")
                elif user is None:
                    print("Testing else part")
                    messages.add_message(request,messages.ERROR,"Sory Your Credentials Don't Match!")
                    return render(request,"enroll/login.html",{"form":authform}) 
        else:
            authform = AuthenticationForm()        
        return render(request,"enroll/login.html",{'form':authform})
    else:
        return HttpResponseRedirect('/profile/')


def profile_page(request):
    if request.user.is_authenticated:
        data = {"name":request.user}
        return render(request,"enroll/profile.html",context=data)
    else:
        return HttpResponseRedirect('/signin/')


# Logout 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')
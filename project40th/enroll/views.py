from django.shortcuts import render
from.forms import SignUpForm
# Create your views here.

def SignUPForm(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(request,'enroll/index.html',{"form":fm})

def user_login(request):
    return 

def user_logout(request):
    return 

def user_profile(request):
    return 
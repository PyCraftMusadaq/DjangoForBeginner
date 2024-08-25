from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.

def sign_up(request):
    if request.method=='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,"Account created Successfully!!")
    else:
        fm = SignUpForm()
    return render(request,"enroll/index.html",{"title":"SignUp","form":fm})



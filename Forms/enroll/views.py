from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def sign_up(request):
    if request.method=='POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,"User Got Registered Successfully")
            
    else:
        fm = UserCreationForm()
    
    return render(request,"enroll/index.html",{"title":"Sign Up","form":fm})

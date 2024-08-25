from django.shortcuts import render
from .forms import UserRegistration 
# Create your views here.

def register(request):
    fm = UserRegistration()
    return render(request,"enroll/userregistration.html",{"title":"Forms","Form":fm}) 
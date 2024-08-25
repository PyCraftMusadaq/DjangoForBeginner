from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import User



# Create your views here.
def Thankyou(request):
    return render(request,"enroll/success.html")
def showformdata(request):
    if request.method =="POST":
        
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data.get('name')
            email = fm.cleaned_data.get('email')
            password = fm.cleaned_data.get("password")
            print(name)
            print(email)
            print(password)
            reg = User(name=name,email=email,password=password)
            reg.save()
            return HttpResponseRedirect("/enroll/success/")
    else:
        fm = StudentRegistration()
    return render(request,"enroll/index.html",{"form":fm})

def updaterow(request):
    pi = User.objects.get(pk=1)
    fm = StudentRegistration(request.POST,instance=pi)
    if fm.is_valid():
        fm.save()
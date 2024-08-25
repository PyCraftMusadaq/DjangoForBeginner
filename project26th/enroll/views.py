from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.
def Thankyou(request):
    return render(request,"enroll/success.html")
def showformdata(request):
    if request.method =="POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Form validated")
            print(type(fm.cleaned_data))
            print(f"The Name is {fm.cleaned_data.get('name')}")
            print(f"The Email Address is {fm.cleaned_data.get('email')}")
            print(f"The Password Your Entered is {fm.cleaned_data.get("password")}")
            return HttpResponseRedirect("/enroll/success/")
    else:
        fm = StudentRegistration()
    return render(request,"enroll/index.html",{"form":fm})
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,"enroll/home.html")

def contact(request):
    return render(request,"enroll/contact.html")
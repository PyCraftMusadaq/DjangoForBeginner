from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def index(request):
    fm = StudentRegistration()
    return render(request,"enroll/index.html",{"title":"Forms","Form":fm})
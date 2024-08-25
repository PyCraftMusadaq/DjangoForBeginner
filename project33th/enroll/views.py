from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def index(request):
    form = StudentRegistration()
    return render(request,"enroll/index.html",{'form':form})
from django.shortcuts import render
from .forms import StudentRegistration, TeacherRegistration
from .models import User 
# Create your views here.
def Student(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentRegistration()  
    return render(request,"enroll/student.html",{'form':fm})

def Teacher(request):
    if request.method=='POST':
        fm = TeacherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = TeacherRegistration()    
    return render(request,"enroll/teacher.html",{'form':fm})
from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    students = Student.students.all()
    return render(request,"school/home.html",{'students':students})

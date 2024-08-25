from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    students = Student.students.get_stu_roll(101,104)
    return render(request,"school/home.html",{'students':students})

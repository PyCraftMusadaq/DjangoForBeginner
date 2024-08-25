from django.shortcuts import render
from .models import Student, ProxyStudent
# Create your views here.
def home(request):
    students = ProxyStudent.students.all()
    #students = ProxyStudent.students.get_stu_roll(101,104)
    return render(request,"school/home.html",{'students':students})

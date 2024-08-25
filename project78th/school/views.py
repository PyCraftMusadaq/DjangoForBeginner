from django.shortcuts import render
from .models import Student
from django.db.models import Q
# Create your views here.
def home(request):
    student = Student.objects.filter( Q(id=7) & Q(roll=107))
    #negation operator 
    student = Student.objects.filter(~Q(id=4))
    return render(request,"school/index.html",context={'students':student})

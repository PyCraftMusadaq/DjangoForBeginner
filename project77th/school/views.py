from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Sum,Min,Max,Count 
# Create your views here.
def home(request):
    student = Student.objects.all()
    average = student.aggregate(Avg('marks'))
    total = student.aggregate(Sum('marks'))
    Minimum = student.aggregate(Min('marks'))
    Maxium = student.aggregate(Max('marks'))
    count = student.aggregate(Count('id'))
    print(average)
    print(total)
    print(Minimum)
    print(Maxium)
    print(count)
    return render(request,"school/index.html",context={'students':student})

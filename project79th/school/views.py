from django.shortcuts import render
from .models import Student
from django.db.models import Q
# Create your views here.
def home(request):
    # Limiting Queryset objets -> First 5
    student = Student.objects.all()[:5]
    # 
    student = Student.objects.all()[:10:2]
    return render(request,"school/index.html",context={'students':student})

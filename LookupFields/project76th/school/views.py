from django.shortcuts import render
from .models import Student
from datetime import date, time 
# Create your views here.
def home(request):
    #student = Student.objects.all()
    
    #matching exact field name with case sensitive 
    #student = Student.objects.filter(name__exact="Attofa Shaukat")

    #matching exact field name with case insensitive 
    #student = Student.objects.filter(name__iexact='attofa shaukat')

    #contain lookup field 
    # student = Student.objects.filter(name__contains="att")

    #in keyword in lookup field 
    # student = Student.objects.filter(id__in=[1,4,7])

    # in with marks 
    # student = Student.objects.filter(marks__in=[80,100])
    
    #greater than gt 
    # student = Student.objects.filter(marks__gt=90)

    #greather than equal to gte 
#    student = Student.objects.filter(marks__gte=90)

    # Less than lt
    # student = Student.objects.filter(marks__lt=80)

    # less than equal to lte 
    # student = Student.objects.filter(marks__lte=90)

    # Starts with 
    #student = Student.objects.filter(name__startswith="a")

    # endswith 
    #student = Student.objects.filter(name__endswith="i")

    # date range lookup field 
    #student = Student.objects.filter(pass_date__range=('2024-05-10','2024-05-25'))
    # datetime field lookup
    #student = Student.objects.filter(admdatetime__date=date(2023,5,1))
    
    # gt and gte field lookup 
    #student = Student.objects.filter(admdatetime__date__gt=date(2023,5,1))
    
    #year lookup 
    #student = Student.objects.filter(pass_date__year=2024)

    #student = Student.objects.filter(pass_date__year__gt=2023) 
    
    #month 
    #student = Student.objects.filter(admdatetime__month=4)
    
    #greater and and equal to month
    #student = Student.objects.filter(admdatetime__month__gte=4)
    
    #working with day
    #student = Student.objects.filter(pass_date__day=1)
    
    #student = Student.objects.filter(pass_date__day__gt=3)
    
    #week
    #student = Student.objects.filter(pass_date__week__gt=14)
    
    #weekday
    #student = Student.objects.filter(pass_date__week_day=1)
    
    #quarter 
    #student = Student.objects.filter(pass_date__quarter=2)
    
    #time field lookup 
   # student = Student.objects.filter(admdatetime__time__gt=time(6,00))
    #hours
    #student = Student.objects.filter(admdatetime__hour__gt=5)
    #minutes 
    #student = Student.objects.filter(admdatetime__minute__gt=30)
    #seconds 
    #student = Student.objects.filter(admdatetime__second__gt=1)
    
    #checking for null
    student = Student.objects.filter(roll__isnull=False)
    return render(request,"school/index.html",context={'students':student})

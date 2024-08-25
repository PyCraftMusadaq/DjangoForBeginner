from django.shortcuts import render
from .models import Student, Teacher 
from django.db.models import Q 
# Create your views here.
def GetData(request):
    # Getting data of all objects 
    "all() method "
    #student = Student.objects.all()
    # getting data of specific objects based on some condition..
    "filter() method "
    #student = Student.objects.filter(marks=80)
   # condition that does not match
    "Exclude() method " 
    #student = Student.objects.exclude(marks=70)
    # By Default it returns data in the ascending order..
    "Orderby() method field asceding order and -field descending order and ? for randomly order"
    #student = Student.objects.order_by('-city')
    #student = Student.objects.filter(marks=80).order_by('city')
    # reverse method 
    #student = Student.objects.order_by('id').reverse()[:5]
    "values method for total data "
    #student = Student.objects.values()

    "values method with specfic data"
    #student = Student.objects.values("name",'city')
    #student = Student.objects.values_list("name")
    # this will not show in the html because it has no name
    #student = Student.objects.values_list("name","id")
    #student = Student.objects.values_list("name","id",named=True)
    "getting database"
    #student = Student.objects.using('default')
    #student = Student.objects.dates(field_name='pass_date',kind='month') # kind can be month,year,day week order as ACS or DSC etc
    "datetime can also be with additonal attribute of datetz"
    ## Working with second table 
    # qs1 = Student.objects.values_list('id','name',named=True)
    # qs2 = Teacher.objects.values_list('id','name',named=True)
    # # The union query 
    # student = qs2.union(qs1,all=True) # set all=True to get duplicate values too..
    # qs1 = Student.objects.values_list('id','name',named=True)
    # qs2 = Teacher.objects.values_list('id','name',named=True)
    # student = qs2.intersection(qs1)
    # qs1 = Student.objects.values_list('id','name',named=True)
    # qs2 = Teacher.objects.values_list('id','name',named=True)
    # student = qs2.difference(qs1)

    # AND operator , OR operator 
    #student = Student.objects.filter(id=6) & Student.objects.filter(roll_number=106)
    # Alternate way of same query 
    #student = Student.objects.filter(id=6,roll_number=106)
    
    # Another method
    student = Student.objects.filter(Q(id=6) & Q(roll_number=106)) 
    print(student) 
    print("SQL Query: ",student.query)
    return render(request,"school/home.html",{"student":student})
from django.shortcuts import render
from .models import Student, Teacher 
from django.db.models import Q 
# Create your views here.
def GetData(request):
    # Methods that do not return queryset
    "Get() Method"
    #student = Student.objects.get(pk=5)
    "First() method"
    #student = Student.objects.first() 
    # another way to write first method 
    #student = Student.objects.order_by('name').first()
    "Last() method returns last record from the database"
    #student = Student.objects.order_by('name').last()
    "latest() method returns the latest record"
    #student = Student.objects.latest('pass_date') 
    "earlist() is inverse of the latest method"
    #student = Student.objects.earliest('pass_date')
    "exist()"
    #student = Student.objects.all()
    
    #--> CRUD operations using DB methods <--#
    "creating new instace"
    #student = Student.objects.create(name="Umair",roll_number=111,city="Abdul Hakeem",marks=85,pass_date="2024-05-20")
    "get_or_create method "
    #student,created = Student.objects.get_or_create(name="Anees",roll_number=112,city="Abdul Hakeem",marks=85,pass_date="2024-05-20")
    #print(created)
    "update method it only applies on queryset not object"
    #student = Student.objects.filter(id=11).update(name="Umair Shabir")
    #print(student.exists())
    "update or create method"
    #student, created = Student.objects.update_or_create(id=12,name="Anees",defaults={'name':"Anees Habib"})
    #print(created)
    "Bulk created objects"
    objs = [
        Student(name="Saif",roll_number=113,city="Umeed garh",marks=70,pass_date="2024-04-05"),
        Student(name="Usman Mansha",roll_number=114,city="Mian Chanu",marks=70,pass_date="2024-03-15"),
        Student(name="Hamza Ishfaq",roll_number=115,city="Lahore",marks=75,pass_date="2024-05-02"),
        Student(name="Huzaifa",roll_number=116,city="Kot Radha kishan",marks=90,pass_date="2024-10-15"),
    ]
    #student=Student.objects.bulk_create(objs)
    #all_student_data = Student.objects.all()
    #for stu in all_student_data:
    #    stu.city = "Multan"
    #student = Student.objects.bulk_update(all_student_data,fields=['city'])
    #student = Student.objects.in_bulk([1,2])
    #print(student[1].name)
    #print(student[2].name)
    "Deleting the data from the database"
    # if we have to delete more than one record than use queryset method like filter to delete 
    #student = Student.objects.get(pk=4).delete()
    " To delete the whole records"
    #Student.objects.all().delete()
    "count"
    student = Student.objects.all()
    print(student.count())
    student = Student.objects.none()

    print(student)
    

    return render(request,"school/home.html",{"record":student})


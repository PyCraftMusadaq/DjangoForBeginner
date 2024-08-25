from django.shortcuts import render
from datetime import datetime 
# Create your views here.
def learn_python(request):
    startdate = datetime.now()
    course = "Python"
    duration = "20 Hours"
    seats = 50

    data = {
        "course":course,"duration":duration,"seats":seats,"st":startdate
    }
    return render(request,"course/courseone.html",context=data)

def learn_django(request):
    startdate = datetime.now()
    course = "Django"
    duration = "30 Hours"
    seats = 20
    data = {
        "course":course,"duration":duration,"seats":seats,"st":startdate
    }
    return render(request,"course/coursetwo.html",context=data)
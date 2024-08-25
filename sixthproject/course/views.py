from django.shortcuts import render

# Create your views here.

def learn_python(request):
    course = "Python"
    duration = "20 Hours"
    seats = 50
    data = {
        "course":course,"duration":duration,"seats":seats
    }
    return render(request,"course/courseone.html",context=data)

def learn_django(request):
    course = "Django"
    duration = "30 Hours"
    seats = 100
    data = {
        "course":course,"duration":duration,"seats":seats
    }
    
    return render(request,"course/coursetwo.html",context=data)



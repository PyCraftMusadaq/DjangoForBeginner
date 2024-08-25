from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        "course1":"Django",
        "course2":"python",
        "course3":"Javascript"
    }
    return render(request,"course/course.html",context=data)
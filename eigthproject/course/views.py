from django.shortcuts import render

# Create your views here.

def learn_python(request):
    return render(request,"course/courseone.html",context={"title":"Python","Learn":"Learn python"})


def learn_django(request):
    return render(request,"course/coursetwo.html")
from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        "Django":300,
        "Python":200,
        "Javascript":500
    }
    return render(request,"fee/fee.html",context=data)
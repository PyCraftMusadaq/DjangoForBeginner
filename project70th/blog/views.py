from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    print("This is View")
    return HttpResponse("Class Based Middlware Testing...")
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course(request):
    return HttpResponse("<h1>Welcome to Courses Module</h1>")

def mainpage(request):
    return HttpResponse("<h1>Welcome to Learning World of AI</h1>")
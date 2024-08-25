from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def home(request):
    print("i am view")
    return HttpResponse("Middleware is being tested with Hooks")

def excp(request):
    print("I am exception view")
    a = 10/0
    return HttpResponse("Exception View")


def user_info(request):
    print("I am user response template view")
    context = {'name':"Attofa Shoukat"}

    return TemplateResponse(request,"blog/home.html",context=context)

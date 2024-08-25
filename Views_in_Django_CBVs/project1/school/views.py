from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic.base import View 
# Create your views here.
# function based views 
def myviewfn(request):
    return HttpResponse("<h1>Function Based views..</h1>")


#class Based view
class MyViewCl(View):
    # if there is attribute related to class 
    name = "Attofa"
    def get(self,request,*args,**kwargs):
        return HttpResponse(f"<h1>Class Based Views with {self.name} </h1>")


# subclass
class MyViewChild(MyViewCl):
    def get(self,request,*args,**kwargs):
        return HttpResponse(f"{self.name}")
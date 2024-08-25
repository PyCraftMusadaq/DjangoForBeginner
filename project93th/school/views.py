from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
# Create your views here.
# Function based views 
def myview(request):
    return HttpResponse("<h1> This is Simple view </h1>")


#class based views 
class MyView(View):
   name = "Attofa Shaukat"
   def get(self,request):
       return HttpResponse(self.name)
    #    return HttpResponse("<h1> Class Based Views->GET </h1>")
    
class MyViewChild(MyView):
    def get(self,request):
        return HttpResponse(self.name)
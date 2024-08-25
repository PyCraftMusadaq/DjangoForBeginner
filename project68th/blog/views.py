from django.shortcuts import render, HttpResponse
from blog import signals 
# Create your views here.
def home(request):
    signals.notifications.send(sender=None,request=request,user=['Attofa','Shoukat'])
    return HttpResponse("Hello Mam! ")

from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages 

# Create your views here.
def index(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, "Account Created Successfully")
            print(messages.get_level(request))
            messages.add_message(request,messages.INFO,"You will get update soon")
            print(messages.get_level(request))
            messages.set_level(request, messages.DEBUG)
            messages.debug(request,"Debug mode")
            print(messages.get_level(request))
            messages.error(request,"Error message")
            # messages.info(request,"message text") 
    else:
        fm = StudentRegistration()
    return render(request,"enroll/index.html",{'form':fm})
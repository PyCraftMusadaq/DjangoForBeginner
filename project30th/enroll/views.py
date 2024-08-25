from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"enroll/Home.html")

def show_details(request,id):
    if id==1:
        student = {"id":id,"name":"Ali"}
    elif id==2:
        student = {"id":id,"name":"Musadaq"}
    elif id ==3:
        student = {"id":id,"name":"Sameer"}
    return render(request,"enroll/show.html",student)
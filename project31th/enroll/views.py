from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"enroll/Home.html")

def show_details(request,year):
    student = {"id":year}
    return render(request,"enroll/show.html",student)
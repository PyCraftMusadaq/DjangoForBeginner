from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setsession(request):
    request.session['name'] = "Attofa"
    request.session['lname'] = "Shaukat"
    return render(request,"student/set_sessions.html")
def getsession(request):
    name = request.session.get('name',default="Guest")
    lname = request.session.get('lname',default="Guest")
    return render(request,"student/get_session.html",context={"name":name,"lname":lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        return render(request,"student/del_sessions.html") 
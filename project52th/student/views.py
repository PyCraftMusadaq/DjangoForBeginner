from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setsession(request):
    request.session['name'] = "Attofa"
    return render(request,"student/set_sessions.html")


def getsession(request):
    name = request.session['name']
    return render(request,"student/get_session.html",context={"name":name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,"student/del_sessions.html")
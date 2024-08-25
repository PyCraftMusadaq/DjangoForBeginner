from django.shortcuts import render, HttpResponse
from datetime import datetime, timedelta
# Create your views here.
def setsession(request):
    request.session['name'] = "Attofa"
    return render(request,"student/set_sessions.html")


def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True 
        return render(request,"student/get_session.html",context={"name":name})
    else:
        return HttpResponse("You Session Has Expired!")
    

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,"student/del_sessions.html")
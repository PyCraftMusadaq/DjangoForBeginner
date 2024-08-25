from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setsession(request):
    request.session['name'] = "Attofa"
    request.session.set_expiry(10) #it will set the expiry date within seconds 
    return render(request,"student/set_sessions.html")



def getsession(request):
    name = request.session.get('name',default="Guest")
    return render(request,"student/get_session.html",context={"name":name})


def delsession(request): 
    request.session.flush() # this will clear the entire session from server as well as from the client's machine
    #but it will not delete the database's session table 
    request.session.clear_expired() # it will clear the database's expired session table 
    return render(request,"student/del_sessions.html") 
from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setsession(request):
    request.session['name'] = "Attofa"
    return render(request,"student/set_sessions.html")
def getsession(request):
    name = request.session.get('name',default="Guest")
    request.session.setdefault('age','26')
    keys = request.session.keys()
    
    return render(request,"student/get_session.html",context={"name":name,"keys":keys})

def delsession(request):
    # The given below code is used to delete the keys daa not the session 
    #if 'name' in request.session:
    #    del request.session['name']
    # if we want to delete the entire session we will use this method 
    request.session.flush()
    return render(request,"student/del_sessions.html") 
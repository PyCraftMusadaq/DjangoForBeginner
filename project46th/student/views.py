from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setcookie(request):
    response = render(request,"student/set_cookies.html")
    response.set_cookie('name',"Attofa Shoukat",expires=datetime.now()+timedelta(days=2))
    return response 

def getcookie(request):
    cname = request.COOKIES.get('name','Guest')
    return render(request,"student/get_cookies.html",{"name":cname})


def delcookie(request):
    response = render(request,"student/del_cookies.html")
    response.delete_cookie('name')
    return response 
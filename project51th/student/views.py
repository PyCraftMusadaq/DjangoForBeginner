from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,"student/set_sessions.html")


def gettestcookie(request):
    request.session.test_cookie_worked()
    return render(request,"student/get_session.html")

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request,"student/del_sessions.html")
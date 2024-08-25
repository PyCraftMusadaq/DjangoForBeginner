from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.
class MyLogoutView(LogoutView):
    template_name = 'myapp/logout.html'

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

class LogoutUserView(View):
    def get(self,request,*args,**kwargs):
        template_name = "myapp/logout.html"
        return render(request,template_name)
    
    def post(self,request,*args,**kwargs):
        logout(request)
        return HttpResponseRedirect('/')
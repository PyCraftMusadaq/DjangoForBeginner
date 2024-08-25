from django.shortcuts import render,HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.views import View 
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

class UserAddShowView(TemplateView):
    template_name = "student/base.html"

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        form = StudentForm()
        students = Student.objects.all()
        context = {'students':students,'form':form}
        return context 

    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            reg = Student(name=nm,email=em,password=pw)
            reg.save()
            return HttpResponseRedirect('/')
        
class UserDeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self,*args,**kwargs):
        print(kwargs)
        Student.objects.get(pk=kwargs['id']).delete()
        return super().get_redirect_url(*args,**kwargs)
    
class UpdateView(View):
    def get(self,request,id):
        pi = Student.objects.get(pk=id) 

# def deletestudent(request,id):
#     pid = Student.objects.get(pk=id)
#     if pid:
#         pid.delete()
#         return HttpResponseRedirect("/showdata/")
    
# def updatestudent(request,id):
#     if request.method=="POST":
#         pi = Student.objects.get(pk=id)
#         form = StudentForm(request.POST, instance=pi)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/showdata/")
#     else:
#         pi = Student.objects.get(pk=id)
#         form = StudentForm(instance=pi)
#     return render(request,"student/base.html",{'form':form})
from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView,View
from .models import Student
from .forms import ContactForm
# Create your views here.

class UpdateView(View):
    template_name = ""
    def get(self,request,*arg,**kwargs):
        student = Student.objects.get(pk=kwargs['id'])
        form = ContactForm(instance=student)
        return render(request,self.template_name,context={'form':form}) 
    def post(self,request,*args,**kwargs):
        student = Student.objects.get(pk=kwargs['id'])
        form = ContactForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request,'student/home.html',{'form':form}) 
    

class AddandShow(TemplateView):
    template_name = "student/home.html"

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data()
        form = ContactForm()
        students = Student.objects.all()
        context['form'] = form 
        context['students'] = students
        return context 
    
    def post(self,request,*arg,**kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            reg = Student(name=nm,email=em,password=pw)
            reg.save()
            return HttpResponseRedirect('/')

# using redirectview to delete the data and then redirect it main page

class UserDeleteView(RedirectView):
    url = "/"

    def get_redirect_url(self, *args, **kwargs):
        id = kwargs['id']
        stu = Student.objects.get(pk=kwargs['id']).delete()
        return super().get_redirect_url(*args, **kwargs)
# using view class to get and save data 
# class AddandShow(View):
#     def get(self,request):
#         form = ContactForm()
#         students = Student.objects.all()
#         return render(request,"student/home.html",{'form':form,'students':students})
    
#     def post(self,request):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             nm = form.cleaned_data['name']
#             em = form.cleaned_data['email']
#             pw = form.cleaned_data['password']
#             reg = Student(name=nm,email=em,password=pw)
#             reg.save()
#             return HttpResponseRedirect('/getdata/')


# def deletedata(request,id):
#     pid = Student.objects.get(pk=id)
#     if pid:
#         pid.delete()
#         return HttpResponseRedirect('/getdata/')
# def updatedata(request,id):
#     pid = Student.objects.get(pk=id)
#     if request.method == "POST":
#         pid = ContactForm(request.POST,instance=pid)
#         if pid.is_valid():
#             pid.save()
#             return HttpResponseRedirect('/getdata/')
#     else:
#         form = ContactForm(instance=pid)
#         return render(request,"student/update.html",{'form':form}) 
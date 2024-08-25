from django.shortcuts import render
from django.views import View 
from .forms import ContactForms
from django.http import HttpResponse 
# Create your views here.
def functionview(request):
    return render(request,"school/home.html")


class MyView(View):
    def get(self,request):
        return render(request,"school/home.html")
    

###########################################################
def Aboutme(request):
    context = {"data":"Simple function Based View"}
    return render(request,"school/about.html",context=context)

#class based aboutme 
class AboutMe(View):
    def get(self,request):
        context= {"data":"Class Based View"}
        return render(request,"school/about.html",context=context)
    
# forms 
def contactus(request):
    if request.method == 'POST':
        fm = ContactForms(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['email'])
            return HttpResponse("Form Submitted!")
        else:
            return render(request,"school/contact.html",{'form':fm})
    else:
        fm = ContactForms()
        return render(request,"school/contact.html",{'form':fm})
    

class ContactClassView(View):
    def get(self,request):
        form = ContactForms()
        return render(request,"school/contact.html",{"form":form}) 
    def post(self,request):
        form = ContactForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            return HttpResponse("Thank You class Based View Used!") 
        
# function based views with passing parameters of data
def newsfunc(request,template_name):

    return render(request,template_name,context={"info":"She is the most prettiest girl in the world"})


# class based same functionality 
class NewsView(View):
    template_name = ""
    def get(self,request):
        template_name = "school/news2.html"
        return render(request,self.template_name,context={"info":"She is the most prettiest girl in the world"})
    
from django.shortcuts import render, HttpResponse
from django.views.generic.base import View, TemplateView, RedirectView
from .forms import ContactUs
# Create your views here.
def homefun(request,template_name):
    return render(request,template_name)


# class based same function 
class MyView(View):
    def get(self,request,*args,**kwargs) -> any:
        return render(request,"school/home.html")
    


################################################################

def aboutfun(request):
    context = {"msg":"Function Based Views are being called here"}
    return render(request,"school/home.html",context=context)

class AboutMeView(View):
    def get(self,request,*args,**kwargs):
        context = {"msg":"Class Based Views are being called here"}
        return render(request,"school/home.html",context=context)
    
#class contactus
class ContactView(View):
    def get(self,request,*args,**kwargs):
        form = ContactUs()
        return render(request,"school/contact.html",context={"form":form})
    
    def post(self,request,*args,**kwargs):
        form = ContactUs(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            return HttpResponse("Saved!")
        



##################################################################
class NewsView(View):
    template_name = ""
    def get(self,request,*args,**kwargs):
        context = {"news":"She is prettiest girl in the world"}
        return render(request,self.template_name,context=context)
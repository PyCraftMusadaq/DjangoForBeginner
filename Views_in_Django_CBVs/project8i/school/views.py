from django.forms import BaseModelForm
from django.shortcuts import render
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django import forms 
from .forms import StudentForm
# Create your views here.

# creating views 
# class ContactView(CreateView):
#     template_name = "school/contact.html"
#     model = Student
#     fields = ['name','email','password']
#     success_url = "/thankyou/"

#     def form_valid(self, form):
#         form
#         return super().form_valid(form)
    
#     # if we want to apply classes on form then we ca use this method 
#     def get_form(self):
#         form =  super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Your Name"})
#         form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter Your Email"})
#         form.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter Your Password"})
#         return form 
    

# another method to add classes to forms 
class ContactView(CreateView):
    template_name = 'school/contact.html'
    model = Student 
    form_class = StudentForm
    success_url = "/thankyou/"




class MyTemplateview(TemplateView):
    template_name = "school/thankyou.html"


class ContactDetailView(DetailView):
    model = Student
    template_name = "school/detail.html"
    context_object_name = 'students'




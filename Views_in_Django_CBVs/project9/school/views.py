from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import  TemplateView
from .models import Student
from .forms import StudentForm
# Create your views here.

class ContactFormView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "school/AddContact.html"
    success_url = "/"


    
class StudentUpdateView(UpdateView):
    model = Student
    #fields = ['name','email','password']
    form_class = StudentForm
    template_name = "school/AddContact.html"
    success_url = "/"

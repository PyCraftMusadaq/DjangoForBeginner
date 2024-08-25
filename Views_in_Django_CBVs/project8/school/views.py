from django.shortcuts import render
from .models import Student
from django import forms 
#from .forms import StudentForm
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

# Create your views here.
class StudentForm(CreateView):
    model = Student
    fields = ['name','email','password']
    template_name = "school/form.html"
    #success_url = "/thankyou/"
    #either we can use success_url attribute or we can use built-in function in the model 

class GetDetailView(DetailView):
    model=Student
    context_object_name = "student"
    template_name = "school/detail.html"
     
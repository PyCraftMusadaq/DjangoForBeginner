from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.

class ContactFormView(FormView):
    template_name = "school/contact.html"
    form_class = ContactForm
    initial = {'name':"Name",'email':".com",'msg':"I think that.."}
    success_url = "/thankyou/"

    # To get data submitted by user 
    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)
    
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
# def profile(request):
#     return render(request,"registration/profile.html")

class MyProfileView(TemplateView):
    template_name = 'registration/profile.html'
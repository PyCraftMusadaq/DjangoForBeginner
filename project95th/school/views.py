from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
"""
 It just return the simple data as well as we can create view class to render template 
"""
# class HomeView(TemplateView):
#     template_name="school/home.html"

class HomeView(TemplateView):
    template_name="school/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
       context = super().get_context_data(**kwargs)
       "one method "
       context['name'] = "Attofa"
       context['roll'] = 104
       print(context)
       print(kwargs) # it captures the url data 
       #context = {"name":"Attofa","roll":104}
       return context 
    
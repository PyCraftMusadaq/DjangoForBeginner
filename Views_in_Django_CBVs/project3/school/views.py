from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

# Now we make our own child view without context 
# class HomeTemplateView(TemplateView):
#     template_name="school/home.html"

# This one is with the help of context data passed to template 
class HomeTemplateView(TemplateView):
    template_name = "school/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name'] = "Attofa Shoukat"
        context['roll'] = kwargs['id']
        #context = {"name":"Attofa",'roll':4}
        print(kwargs)

        return context 
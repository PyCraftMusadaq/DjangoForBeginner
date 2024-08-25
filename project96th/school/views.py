from typing import Any
from django.shortcuts import render
from django.views.generic.base import RedirectView,TemplateView
# Create your views here.
# by inheritance 
class DjangoDocs(RedirectView):
    url = "https://docs.djangoproject.com/en/5.0/"

class ChildRedirectView(RedirectView):
    pass 

class MyRedirectView(RedirectView):
    pattern_name = "mindex"
    permanent = True 
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print(args, "\n", kwargs)
        return super().get_redirect_url(*args, **kwargs)

# class Redirectwithvalue(RedirectView):
#     pattern_name="mindex"


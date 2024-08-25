from typing import Any
from django.shortcuts import render
from django.views.generic.base import RedirectView, TemplateView 
# Create your views here.

class MyChildView(RedirectView):
    url ="https://github.com/MusadaqTanvir/Resource_Monitor_App"

class MyRedirectView(RedirectView):
    pattern_name = "mindex"
    # status code just changes 
    permanent = True 
    query_string = True 

    def get_redirect_url(self,*args, **kwargs):
        print(args,"\n",kwargs)
        # lets say we want to change the key of url 
        kwargs['id'] = 4
        return super().get_redirect_url(*args, **kwargs)
    





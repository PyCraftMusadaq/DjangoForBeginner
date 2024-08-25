from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 
# Create your views here.

# what if we want to apply mutliple decorators on same class then we will make list of those decorators and then pass that list to method_decorator 
decorators = [login_required, staff_member_required]

# @method_decorator(decorators, name='dispatch') 

@method_decorator(login_required,name='dispatch')
class MyProfileView(TemplateView):
    template_name = 'registration/profile.html'
    
    # @method_decorator(login_required)
    # def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     return super().dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required,name="dispatch")
class MyAboutView(TemplateView):
    template_name = "registration/about.html"

    # @method_decorator(staff_member_required)
    # def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     return super().dispatch(request, *args, **kwargs)
    
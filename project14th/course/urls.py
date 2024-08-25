from django.urls import path 
from . import views 
urlpatterns = [
    path("django/",views.course,name="djangocourse"),
]

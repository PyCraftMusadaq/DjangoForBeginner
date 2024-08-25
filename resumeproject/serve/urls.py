from django.urls import path 
from . import views 
urlpatterns = [
    path("serve/",views.serve,name="service"),
]

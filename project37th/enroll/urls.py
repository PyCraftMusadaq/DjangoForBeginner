from django.urls import path 
from . import views 
urlpatterns = [
    path("student/",views.sign_up,name="index"),
] 
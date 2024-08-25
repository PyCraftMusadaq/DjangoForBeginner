from django.urls import path 
from . import views 

urlpatterns = [
    path("stu/",views.Student,name="student"),
    path("teach/",views.Teacher,name="teacher"),
]

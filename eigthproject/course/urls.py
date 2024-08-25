from django.urls import path 
from . import views 

urlpatterns = [
    path("learnpy/",views.learn_python,name="python"),
    path("learndj/",views.learn_django,name="django"),
]

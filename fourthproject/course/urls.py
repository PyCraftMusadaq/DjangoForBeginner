from django.urls import path 
from . import views 
urlpatterns = [
    path("coursedetail/",views.index,name="coursedetail"),
]
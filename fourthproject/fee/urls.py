from django.urls import path 
from . import views 
urlpatterns = [
    path("feedetail/",views.index,name="feedetail"),
]
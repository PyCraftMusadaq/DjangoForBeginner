from django.urls import path 
from . import views 
urlpatterns = [
    path("",views.add_show,name="index"),
    path("delete/<int:id>/",views.delete_row,name="delete"),
    path("edit/<int:id>/",views.edit_row,name="editdata"),
    
]

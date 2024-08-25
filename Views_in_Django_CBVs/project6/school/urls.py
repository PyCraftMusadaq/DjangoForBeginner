from django.urls import path 
from . import views 
urlpatterns = [
    path("list/",views.StudentListView.as_view(),name="list"),
    path("getdetail/<int:id>/",views.StudentDetailView.as_view(),name="studentdetail"),
]

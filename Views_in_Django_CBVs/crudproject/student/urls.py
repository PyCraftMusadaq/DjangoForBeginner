from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.AddandShow.as_view(),name="addandshow"),
    path("delete/<int:id>/",views.UserDeleteView.as_view(),name="delete"),
    path("updatestudent/<int:id>/",views.UpdateView.as_view(template_name="student/update.html"),name="update"),
]

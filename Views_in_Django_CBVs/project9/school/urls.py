from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.ContactFormView.as_view(),name="contact"),
    path("update/<int:pk>",views.StudentUpdateView.as_view(),name="update"),
]

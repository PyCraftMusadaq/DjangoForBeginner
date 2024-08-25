from django.urls import path 
from . import views 
urlpatterns = [
    path("",views.StudentForm.as_view(),name="createview"),
    path("thankyou/",views.TemplateView.as_view(template_name="school/success.html"),name="thankyou"),
    path("detail/<int:pk>/",views.GetDetailView.as_view(),name="getdetail"),
]


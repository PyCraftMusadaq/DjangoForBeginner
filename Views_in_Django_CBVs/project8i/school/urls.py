from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.ContactView.as_view(),name="contact"),
    path("detail/<int:pk>/",views.ContactDetailView.as_view(),name="detail"),
    path("thankyou/",views.MyTemplateview.as_view(),name="thankyou"),
]

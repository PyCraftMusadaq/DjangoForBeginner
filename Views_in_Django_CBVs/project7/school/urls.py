from django.urls import path 
from . import views 

urlpatterns = [
    path("contact/",views.ContactFormView.as_view(),name="contact"),
    path("thankyou/",views.TemplateView.as_view(template_name="school/thankyou.html")),
]

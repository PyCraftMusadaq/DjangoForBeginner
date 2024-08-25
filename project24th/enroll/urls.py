from django.urls import path 
from . import views 
urlpatterns = [
    path("registration/",views.showformdata,name="Showdata"),
    path("success/",views.Thankyou,name="success"),
]

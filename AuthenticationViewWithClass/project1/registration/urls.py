from django.urls import path 
from . import views 

urlpatterns = [
    path("profile/",views.MyProfileView.as_view(),name="profile"),
]

from django.urls import path 
from . import views 

# There is some problem in this apporach so we will use another approach in the next project
urlpatterns = [
    path("profile/",views.MyProfileView.as_view(),name="profile"),
    path("aboutme/",views.MyAboutView.as_view(),name="about"),
]

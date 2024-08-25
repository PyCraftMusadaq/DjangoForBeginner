from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("logout/",views.user_logout,name="logout"),
    path("addpost/",views.addpost,name="addpost"),
    path("updatepost/<int:id>/",views.updatepost,name="updatepost"),
    path("deletepost/<int:id>/",views.deletepost,name="deletepost"),
]

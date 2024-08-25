from django.urls import path 
from . import views 

urlpatterns = [
    path("signup/",views.signupform,name="signup"),
    path("signin/",views.signinform,name="signin"),
    path("dashboard/",views.user_dashboard,name="dashboard"),
    path("logout/",views.user_logout,name="logout"),
]

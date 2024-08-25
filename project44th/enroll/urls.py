from django.urls import path 
from . import views 

urlpatterns = [
    path("signup/",views.signupform,name="signup"),
    path("signin/",views.signinform,name="signin"),
    path("profile/",views.user_profile,name="profile"),
    path("logout/",views.user_logout,name="logout"),
    path("changepassword1/",views.change_password,name="changepassword1"),
    path("changepassword2/",views.change_password2,name="changepassword2"),
    path("userdetails/<int:id>",views.user_detail,name="user_details")
]

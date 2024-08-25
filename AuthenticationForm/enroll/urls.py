from django.urls import path 
from . import views 

urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path("signin/",views.login_user,name="signin"),
    path("profile/",views.user_profile,name="userprofile"),
    path("logout/",views.logout_user,name="logout"),
]

from django.urls import path 
from . import views 

urlpatterns = [
    path("signin/",views.user_login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("profile/",views.profile_page,name="profile"),
    path("logout/",views.user_logout,name="logout"),
]

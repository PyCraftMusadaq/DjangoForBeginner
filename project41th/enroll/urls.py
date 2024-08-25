from django.urls import path 
from . import views 

urlpatterns = [
    path('signup/',views.SignUp,name="signup"),
    path("login/",views.SignIn,name="signin"),
    path("profile/",views.user_profile,name="profile"),
    path("logout",views.logout_user,name="logout"),
    #path("changepassword/",views.change_password,name="changepassword"),
    #path("changepass/",views.change_pass,name="changepass"),
]
#

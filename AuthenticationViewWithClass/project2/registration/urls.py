from django.urls import path 
from . import views 
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# There is some problem in this apporach so we will use another approach in the next project
urlpatterns = [
    path("profile/",login_required(views.MyProfileView.as_view()),name="profile"),
    path("aboutme/",staff_member_required(views.MyAboutView.as_view()),name="about"),
]

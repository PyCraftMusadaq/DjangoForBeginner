from django.urls import path
from . import views 
urlpatterns = [
    path("",views.home,name="home"),
    path('song/',views.getsongs,name="songs"),
    path("posts/",views.getposts,name="posts"),
    path("pages/",views.getpages,name="pages"),
    path("user/",views.show_user_data,name="user")
]

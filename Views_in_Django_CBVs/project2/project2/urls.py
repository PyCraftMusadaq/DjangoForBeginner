"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("homefun/",views.homefun,{'template_name':'school/home.html'},name="homefun"),
    path("homefun2/",views.homefun,{'template_name':'school/home2.html'},name="homefun2"),
    path("homecl/",views.MyView.as_view(),name="homecl"),
    path('aboutfun/',views.aboutfun,name="aboutfun"),
    path("aboutcl/",views.AboutMeView.as_view(),name="aboutcl"),
    path("form/",views.ContactView.as_view(),name="form"),
    path("news/",views.NewsView.as_view(template_name="school/news.html"),name="news"),
]

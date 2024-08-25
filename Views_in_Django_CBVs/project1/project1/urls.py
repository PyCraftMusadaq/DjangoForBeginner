"""
URL configuration for project1 project.

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
    path("funview/",views.myviewfn,name="funview"),
    # simple call to class view
    #path("clview/",views.MyViewCl.as_view(),name="clview"),
    # call to view with argument 
    path("clview/",views.MyViewCl.as_view(name="Attofa Shoukat"),name="clview"),
    # subclass url
    path("subcl/",views.MyViewChild.as_view(),name="subcl"),
]

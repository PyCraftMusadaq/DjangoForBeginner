from django.urls import path 
from . import views 
urlpatterns = [
    path("feepy/",views.fee_python,name="feepython"),
    path("feedj/",views.fee_django,name="feedjango"),
]

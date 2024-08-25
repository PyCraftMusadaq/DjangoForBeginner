from django.urls import path 
from . import views 
urlpatterns = [
    path("data/",views.MyListView.as_view(),name="Listview"),
]

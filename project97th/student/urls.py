from django.urls import path 
from .import views 
urlpatterns = [
    # path("showdata/",views.showdata,name="data"),
    path("",views.UserAddShowView.as_view(),name="data"),
    path('delete/<int:id>/',views.UserDeleteView.as_view(),name="deletestudent"),
    path("updatestudent/<int:id>/",views.UpdateView.as_view(),name="updatestudent"),
]

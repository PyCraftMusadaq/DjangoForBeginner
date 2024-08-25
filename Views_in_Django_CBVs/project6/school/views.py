from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 

# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = "school/studentlist.html"
    context_object_name = "students"

    # def get_queryset(self) -> QuerySet[Any]:
    #     return Student.objects.values('name')



class StudentDetailView(DetailView):
    model = Student
    template_name = "school/studentdetail.html"
    context_object_name = "student"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['all_data'] = self.model.objects.all().order_by('name')
        return context  



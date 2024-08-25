from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.

class MyListView(ListView):
    model = Student
    template_name = "school/student.html"
    # Use template_name_suffix attribute to get default template
    # ordering data 
    ordering = ['roll']
    # By Default the model object name is object_list or Student_list but we can rename it 
    context_object_name = "students"

    # if we want to apply queryset with some filter than we can do this by query set method 
    
    def get_queryset(self):
        # Here we can specify the condtion...
        return Student.objects.filter(course="AI Engineer")
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['Toper'] = Student.objects.filter(course="AI Engineer")
        return context
    

    # if we want to return dynamic templates then
    def get_template_names(self) -> list[str]:
        if self.request.COOKIES['user'] == "attofa":
            template_name = 'school/attofa.html'
        else:
            template_name = self.template_name 
        return [template_name]
    
    def get_template_names(self) -> list[str]:
        if self.request.user.is_superuser:
            template_name = 'school/superuser.html'
        elif self.request.user.is_staff:
            template_name = 'school/staff.html'
        else:
            template_name = self.template_name
        return [template_name]
    
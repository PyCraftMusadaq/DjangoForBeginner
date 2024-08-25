from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','student_id','student_name','student_email','student_pass')
# Register your models here.
#admin.site.register(Student,StudentAdmin)
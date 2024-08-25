from django.contrib import admin
from .models import POST 
# Register your models here.
@admin.register(POST)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']
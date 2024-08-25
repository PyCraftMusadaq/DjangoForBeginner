from django.contrib import admin
from .models import FormData
# Register your models here.
@admin.register(FormData)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","name",'email',"password")
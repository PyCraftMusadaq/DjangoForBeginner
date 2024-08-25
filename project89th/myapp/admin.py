from django.contrib import admin
from .models import Page, Like 
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['user','page_name','page_category','page_publish_date']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user','page_name','page_category','page_publish_date','page','likes']

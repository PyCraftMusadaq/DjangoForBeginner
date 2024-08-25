from django.contrib import admin
from .models import Post, Song,Page
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['user','page_name','page_category','page_publish_date']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','post_title','post_category','post_publish_date']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id','song_title','song_duration','written_by']

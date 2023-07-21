from django.contrib import admin

# Register your models here.

from .models import User,Page,Post,Song

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['page_name','page_cat','page_post_date','user']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['post_name','post_cat','post_publish_date','user']



@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=['song_title','song_cat','song_publish_date','written_by']

from django.contrib import admin
from .models import Post
# Register your models here.

# admin.site.register(Post) #등록법 1

@admin.register(Post) #등록법3
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']

# admin.site.register(Post, PostAdmin) #등록법2

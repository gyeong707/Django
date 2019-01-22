from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

# Register your models here.

# admin.site.register(Post) #등록법 1

@admin.register(Post) #등록법3
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'created_at', 'updated_at']

    def content_size(self, post): #인자로 인스턴스
        return '{}글자' .format(len(post.content))
        # return mark_safe('<strong>{}</strong>글자' .format(len(post.content))

    content_size.short_description = "글자수"

# admin.site.register(Post, PostAdmin) #등록법2

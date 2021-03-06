from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe

# Register your models here.

# admin.site.register(Post) #등록법 1

@admin.register(Post) #등록법3
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at']

    actions = ['make_published', 'make_Draft']

    def content_size(self, post): #인자로 인스턴스
        # return '{}글자' .format(len(post.content))
        return mark_safe('<strong>{}</strong>글자' .format(len(post.content)))

    content_size.short_description = '글자수'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 Publishing 상태로 변경' .format(updated_count))
    make_published.short_description = "지정 포스팅을 Publishing 상태로 변경."

    def make_Draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft 상태로 변경' .format(updated_count))
    make_Draft.short_description = "지정 포스팅을 Draft 상태로 변경."
# admin.site.register(Post, PostAdmin) #등록법2


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
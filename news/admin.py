from django.contrib import admin
from django.utils.html import format_html

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ContextInline(admin.StackedInline):
    model = Context
    extra = 1

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_preview', 'intro', 'read_time', 'published', 'important', 'views', 'author', 'category', 'created_at')
    list_filter = ('category','published','author','tags','important')
    search_fields = ('title','intro')
    inlines = [ContextInline, CommentInline]

    def cover_preview(self, obj):
        if obj.cover:
            return format_html(
                '<img src="{}" width="120px" height="80px" style="object-fit:cover;" />',
             obj.cover.url
            )
        return "rasm yoq"

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'email', 'text', 'created_at',)
    list_filter = ('email',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

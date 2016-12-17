from django.contrib import admin
from myblog.models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_publish',)

    class Media:
        js = (
            '/static/kindeditor/kindeditor-all-min.js',
            '/static/kindeditor/lang/zh-CN.js',
            '/static/kindeditor/config.js',
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'index',)
    list_editable = ('name', 'index',)
    list_display_links = None


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_editable = ('name', )
    list_display_links = None


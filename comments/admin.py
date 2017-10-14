from django.contrib import admin
from .models import Comment


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'created_time', 'article')
    # list_editable = ('name', 'email')
    list_display_links = ('text',)

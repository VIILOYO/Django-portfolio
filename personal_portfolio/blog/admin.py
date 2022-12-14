from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'text']

admin.site.register(Post, PostAdmin)

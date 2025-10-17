from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'is_published')
    list_filter = ('is_published', 'published_at', 'author')
    search_fields = ('title', 'content', 'author__username', 'tags')
    ordering = ('-published_at',)
    readonly_fields = ('slug', 'published_at')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'is_published')
        }),
        ('Content', {
            'fields': ('content', 'tags')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Timestamps', {
            'fields': ('published_at',),
            'classes': ('collapse',)
        }),
    )

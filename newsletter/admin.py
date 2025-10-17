from django.contrib import admin
from .models import Newsletter

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed', 'is_active')
    list_filter = ('is_active', 'date_subscribed')
    search_fields = ('email',)
    ordering = ('-date_subscribed',)
    readonly_fields = ('date_subscribed',)

    fieldsets = (
        ('Subscriber Information', {
            'fields': ('email', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('date_subscribed',),
            'classes': ('collapse',)
        }),
    )

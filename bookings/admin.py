from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'event_type', 'date', 'location', 'status', 'created_at')
    list_filter = ('status', 'location', 'date', 'created_at')
    search_fields = ('client_name', 'client_email', 'client_phone', 'event_type__title')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Client Information', {
            'fields': ('client_name', 'client_email', 'client_phone')
        }),
        ('Event Details', {
            'fields': ('event_type', 'location', 'date', 'number_of_kids')
        }),
        ('Additional Information', {
            'fields': ('special_requests', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['mark_as_confirmed', 'mark_as_completed']

    def mark_as_confirmed(self, request, queryset):
        queryset.update(status='confirmed')
        self.message_user(request, f"{queryset.count()} booking(s) marked as confirmed.")
    mark_as_confirmed.short_description = "Mark selected bookings as confirmed"

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
        self.message_user(request, f"{queryset.count()} booking(s) marked as completed.")
    mark_as_completed.short_description = "Mark selected bookings as completed"

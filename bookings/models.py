from django.db import models
from django.conf import settings

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    LOCATION_CHOICES = [
        ('kampala', 'Kampala'),
        ('wakiso', 'Wakiso'),
        ('entebbe', 'Entebbe'),
    ]

    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20)
    event_type = models.ForeignKey('services.Service', on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    date = models.DateField()
    number_of_kids = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.event_type.title} ({self.date})"

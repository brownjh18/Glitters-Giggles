from django.db import models
from cloudinary.models import CloudinaryField

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('birthday', 'Birthday Parties'),
        ('corporate', 'Corporate Events'),
        ('school', 'School Activities'),
        ('cultural', 'Cultural Events'),
        ('stem', 'STEM Learning'),
        ('inclusive', 'Inclusive Play'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price_range = models.CharField(max_length=100, help_text="e.g., 'UGX 500,000 - 1,000,000'")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = CloudinaryField('image', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

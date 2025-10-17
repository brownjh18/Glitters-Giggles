from django.db import models
from cloudinary.models import CloudinaryField

class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('birthday', 'Birthday Parties'),
        ('corporate', 'Corporate Events'),
        ('school', 'School Activities'),
        ('cultural', 'Cultural Events'),
        ('stem', 'STEM Learning'),
        ('inclusive', 'Inclusive Play'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = CloudinaryField('image')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.title

from rest_framework import serializers
from django.contrib.auth import get_user_model
from services.models import Service
from bookings.models import Booking
from gallery.models import Gallery
from blog.models import Blog
from newsletter.models import Newsletter
from core.models import Contact

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'phone', 'role', 'date_joined']
        read_only_fields = ['id', 'date_joined']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    event_type_title = serializers.CharField(source='event_type.title', read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        # Send email notification when booking is created
        booking = super().create(validated_data)
        # Email sending logic will be implemented later
        return booking

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
        read_only_fields = ['created_at']

class BlogSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    tags_list = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['slug', 'published_at']

    def get_tags_list(self, obj):
        return obj.get_tags_list()

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'
        read_only_fields = ['date_subscribed']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['created_at']

    def create(self, validated_data):
        # Send email notification when contact form is submitted
        contact = super().create(validated_data)
        # Email sending logic will be implemented later
        return contact
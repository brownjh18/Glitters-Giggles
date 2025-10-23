from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
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

        # Send email notification
        subject = f'New Booking Request from {booking.client_name}'
        message = f'''
        New booking request details:

        Client Name: {booking.client_name}
        Client Email: {booking.client_email}
        Client Phone: {booking.client_phone}
        Location: {booking.location}
        Event Date: {booking.date}
        Number of Children: {booking.number_of_kids}
        Special Requests: {booking.special_requests or 'None'}

        Please contact the client to confirm the booking.
        '''
        recipient_list = [settings.DEFAULT_FROM_EMAIL]

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,
                fail_silently=False,
            )
        except Exception as e:
            # Log the error but don't fail the booking creation
            print(f"Failed to send booking email: {e}")

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

    def create(self, validated_data):
        # Send email notification when newsletter subscription is created
        newsletter = super().create(validated_data)

        # Send confirmation email to subscriber
        subject = 'Welcome to Glitters & Giggles Newsletter!'
        message = f'''
        Thank you for subscribing to our newsletter, {newsletter.email}!

        You'll now receive updates about our latest events, special offers, and parenting tips.

        Best regards,
        The Glitters & Giggles Team
        '''
        recipient_list = [newsletter.email]

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,
                fail_silently=False,
            )
        except Exception as e:
            # Log the error but don't fail the subscription
            print(f"Failed to send newsletter confirmation email: {e}")

        return newsletter

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['created_at']

    def create(self, validated_data):
        # Send email notification when contact form is submitted
        contact = super().create(validated_data)

        # Send email notification
        subject = f'New Contact Form Submission from {contact.name}'
        message = f'''
        New contact form submission:

        Name: {contact.name}
        Email: {contact.email}
        Message: {contact.message}

        Please respond to this inquiry as soon as possible.
        '''
        recipient_list = [settings.DEFAULT_FROM_EMAIL]

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,
                fail_silently=False,
            )
        except Exception as e:
            # Log the error but don't fail the contact creation
            print(f"Failed to send contact email: {e}")

        return contact
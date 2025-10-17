from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth import get_user_model
from services.models import Service
from bookings.models import Booking
from gallery.models import Gallery
from blog.models import Blog
from newsletter.models import Newsletter
from core.models import Contact
from .serializers import (
    UserSerializer, ServiceSerializer, BookingSerializer,
    GallerySerializer, BlogSerializer, NewsletterSerializer, ContactSerializer
)

User = get_user_model()

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def bookings(self, request, pk=None):
        service = self.get_object()
        bookings = Booking.objects.filter(event_type=service)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Booking.objects.all()
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset

    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'confirmed'
        booking.save()
        serializer = self.get_serializer(booking)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'completed'
        booking.save()
        serializer = self.get_serializer(booking)
        return Response(serializer.data)

class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Gallery.objects.all()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.filter(is_published=True)
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['get'])
    def related_posts(self, request, pk=None):
        blog = self.get_object()
        related_posts = Blog.objects.filter(
            tags__icontains=blog.tags.split(',')[0] if blog.tags else '',
            is_published=True
        ).exclude(id=blog.id)[:3]
        serializer = self.get_serializer(related_posts, many=True)
        return Response(serializer.data)

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.filter(is_active=True)
    serializer_class = NewsletterSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']  # Only allow POST for subscriptions

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']  # Only allow POST for contact form

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

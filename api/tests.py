from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from services.models import Service
from bookings.models import Booking
from gallery.models import Gallery
from blog.models import Blog
from newsletter.models import Newsletter
from core.models import Contact

User = get_user_model()

class APITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            name='Test User'
        )

        # Create test service
        self.service = Service.objects.create(
            title='Test Birthday Party',
            description='A fun birthday party service',
            price_range='UGX 500,000 - 1,000,000',
            category='birthday'
        )

        # Create test booking
        self.booking = Booking.objects.create(
            client_name='John Doe',
            client_email='john@example.com',
            client_phone='+256700123456',
            event_type=self.service,
            location='kampala',
            date='2025-12-25',
            number_of_kids=10,
            status='pending'
        )

    def test_service_list(self):
        """Test retrieving list of services"""
        url = reverse('service-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_service_detail(self):
        """Test retrieving service detail"""
        url = reverse('service-detail', kwargs={'pk': self.service.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Birthday Party')

    def test_booking_list(self):
        """Test retrieving list of bookings"""
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_create(self):
        """Test creating a new booking"""
        # Authenticate the client
        self.client.force_authenticate(user=self.user)
        url = reverse('booking-list')
        data = {
            'client_name': 'Jane Smith',
            'client_email': 'jane@example.com',
            'client_phone': '+256700654321',
            'event_type': self.service.id,
            'location': 'wakiso',
            'date': '2025-11-15',
            'number_of_kids': 15,
            'special_requests': 'Vegetarian options needed'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['client_name'], 'Jane Smith')

    def test_newsletter_subscription(self):
        """Test newsletter subscription"""
        url = reverse('newsletter-list')
        data = {'email': 'subscriber@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], 'subscriber@example.com')

    def test_contact_form(self):
        """Test contact form submission"""
        url = reverse('contact-list')
        data = {
            'name': 'Contact User',
            'email': 'contact@example.com',
            'message': 'This is a test message'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Contact User')

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            name='Test User',
            role='client'
        )

        self.service = Service.objects.create(
            title='Test Service',
            description='Test description',
            price_range='UGX 300,000 - 500,000',
            category='school'
        )

    def test_user_creation(self):
        """Test user model creation"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.role, 'client')
        self.assertEqual(str(self.user), 'testuser')

    def test_service_creation(self):
        """Test service model creation"""
        self.assertEqual(self.service.title, 'Test Service')
        self.assertEqual(self.service.category, 'school')
        self.assertTrue(self.service.is_active)
        self.assertEqual(str(self.service), 'Test Service')

    def test_booking_creation(self):
        """Test booking model creation"""
        booking = Booking.objects.create(
            client_name='Test Client',
            client_email='client@example.com',
            client_phone='+256700123456',
            event_type=self.service,
            location='entebbe',
            date='2025-10-30',
            number_of_kids=8
        )
        self.assertEqual(booking.client_name, 'Test Client')
        self.assertEqual(booking.status, 'pending')
        self.assertEqual(str(booking), 'Test Client - Test Service (2025-10-30)')

    def test_newsletter_creation(self):
        """Test newsletter subscription creation"""
        newsletter = Newsletter.objects.create(
            email='test@example.com'
        )
        self.assertEqual(newsletter.email, 'test@example.com')
        self.assertTrue(newsletter.is_active)
        self.assertEqual(str(newsletter), 'test@example.com')

    def test_contact_creation(self):
        """Test contact form creation"""
        contact = Contact.objects.create(
            name='Test Contact',
            email='contact@example.com',
            message='Test message'
        )
        self.assertEqual(contact.name, 'Test Contact')
        self.assertEqual(str(contact), 'Test Contact - contact@example.com')

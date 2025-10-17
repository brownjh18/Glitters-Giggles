from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from bookings.models import Booking
from services.models import Service
from newsletter.models import Newsletter
from core.models import Contact

def is_staff_or_admin(user):
    return user.role in ['admin', 'staff']

@login_required
@user_passes_test(is_staff_or_admin)
def dashboard(request):
    # Get current month
    now = timezone.now()
    start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    # Analytics data
    total_bookings = Booking.objects.count()
    pending_bookings = Booking.objects.filter(status='pending').count()
    confirmed_bookings = Booking.objects.filter(status='confirmed').count()
    completed_bookings = Booking.objects.filter(status='completed').count()

    # Monthly stats
    monthly_bookings = Booking.objects.filter(created_at__gte=start_of_month).count()
    monthly_contacts = Contact.objects.filter(created_at__gte=start_of_month).count()

    # Recent bookings
    recent_bookings = Booking.objects.select_related('event_type').order_by('-created_at')[:5]

    # Popular services
    popular_services = Service.objects.annotate(
        booking_count=Count('booking')
    ).order_by('-booking_count')[:5]

    # Newsletter subscribers
    total_subscribers = Newsletter.objects.filter(is_active=True).count()

    context = {
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'confirmed_bookings': confirmed_bookings,
        'completed_bookings': completed_bookings,
        'monthly_bookings': monthly_bookings,
        'monthly_contacts': monthly_contacts,
        'recent_bookings': recent_bookings,
        'popular_services': popular_services,
        'total_subscribers': total_subscribers,
    }

    return render(request, 'dashboard/dashboard.html', context)

@login_required
@user_passes_test(is_staff_or_admin)
def analytics(request):
    # More detailed analytics
    now = timezone.now()
    last_30_days = now - timedelta(days=30)
    last_7_days = now - timedelta(days=7)

    # Booking trends
    daily_bookings = []
    for i in range(7):
        date = now - timedelta(days=i)
        count = Booking.objects.filter(
            created_at__date=date.date()
        ).count()
        daily_bookings.append({
            'date': date.strftime('%Y-%m-%d'),
            'count': count
        })

    # Service performance
    service_performance = Service.objects.annotate(
        total_bookings=Count('booking'),
        pending_bookings=Count('booking', filter=Q(booking__status='pending')),
        completed_bookings=Count('booking', filter=Q(booking__status='completed'))
    ).order_by('-total_bookings')

    context = {
        'daily_bookings': daily_bookings,
        'service_performance': service_performance,
    }

    return render(request, 'dashboard/analytics.html', context)

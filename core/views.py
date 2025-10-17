from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from services.models import Service
from gallery.models import Gallery
from blog.models import Blog

def home(request):
    # Get featured services and recent gallery items
    services = Service.objects.filter(is_active=True)[:6]
    gallery_items = Gallery.objects.all()[:8]
    recent_blogs = Blog.objects.filter(is_published=True)[:3]

    context = {
        'services': services,
        'gallery_items': gallery_items,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        contact = Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email notification
        try:
            send_mail(
                f'New Contact Form Submission from {name}',
                f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
        except Exception as e:
            # Log error but don't show to user
            pass

        messages.success(request, 'Thank you for your message! We\'ll get back to you soon.')
        return redirect('contact')

    return render(request, 'core/contact.html')

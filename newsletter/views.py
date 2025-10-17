from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Newsletter
from .forms import NewsletterForm

def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if email already exists
            if Newsletter.objects.filter(email=email, is_active=True).exists():
                messages.warning(request, 'You are already subscribed to our newsletter!')
                return redirect('home')

            # Create new subscription
            Newsletter.objects.create(email=email)

            # Send welcome email (optional)
            try:
                send_mail(
                    'Welcome to Glitters & Giggles Newsletter!',
                    f'Thank you for subscribing to our newsletter, {email}! We\'ll keep you updated with the latest news and events.',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=True,
                )
            except:
                pass  # Email sending is optional

            messages.success(request, 'Successfully subscribed to our newsletter!')
            return redirect('home')
    else:
        form = NewsletterForm()

    return render(request, 'newsletter/subscribe.html', {'form': form})

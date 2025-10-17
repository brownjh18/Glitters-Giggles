from django.shortcuts import render, get_object_or_404
from .models import Service

def services_list(request):
    services = Service.objects.filter(is_active=True)
    context = {
        'services': services,
    }
    return render(request, 'services/services_list.html', context)

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id, is_active=True)
    context = {
        'service': service,
    }
    return render(request, 'services/service_detail.html', context)

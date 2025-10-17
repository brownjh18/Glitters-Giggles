from django.shortcuts import render
from .models import Gallery

def gallery_list(request):
    # Get all gallery items, ordered by creation date
    gallery_items = Gallery.objects.all()

    # Get unique categories for filtering
    categories = Gallery.objects.values_list('category', flat=True).distinct()

    # Filter by category if provided
    category_filter = request.GET.get('category')
    if category_filter:
        gallery_items = gallery_items.filter(category=category_filter)

    context = {
        'gallery_items': gallery_items,
        'categories': categories,
        'selected_category': category_filter,
    }
    return render(request, 'gallery/gallery_list.html', context)

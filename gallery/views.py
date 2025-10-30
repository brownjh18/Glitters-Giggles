from django.shortcuts import render
from .models import Gallery

def gallery_list(request):
    # Get all gallery items, ordered by pk to match fixture order
    gallery_items = Gallery.objects.all().order_by('pk')

    # Get unique categories for filtering
    categories = Gallery.objects.values_list('category', flat=True).distinct()

    # Filter by category if provided
    category_filter = request.GET.get('category')
    if category_filter:
        gallery_items = gallery_items.filter(category=category_filter)

    # Add index to gallery items for proper image mapping (using pk as index)
    gallery_items_with_index = []
    for item in gallery_items:
        gallery_items_with_index.append((item, item.pk))

    context = {
        'gallery_items': gallery_items,
        'gallery_items_with_index': gallery_items_with_index,
        'categories': categories,
        'selected_category': category_filter,
    }
    return render(request, 'gallery/gallery_list.html', context)

def gallery_detail(request, pk):
    gallery_item = get_object_or_404(Gallery, pk=pk)

    # Use pk as index for proper image mapping
    gallery_index = gallery_item.pk

    # Get related gallery items from the same category
    related_gallery_items = Gallery.objects.filter(
        category=gallery_item.category
    ).exclude(pk=gallery_item.pk)[:4]

    # Add index to related gallery items for proper image mapping (using pk)
    related_gallery_items_with_index = []
    for related_item in related_gallery_items:
        related_gallery_items_with_index.append((related_item, related_item.pk))

    context = {
        'gallery_item': gallery_item,
        'gallery_index': gallery_index,
        'related_gallery_items': related_gallery_items_with_index,
    }
    return render(request, 'gallery/gallery_detail.html', context)

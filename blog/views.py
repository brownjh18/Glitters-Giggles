from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    # Get all published blog posts
    blogs = Blog.objects.filter(is_published=True)

    # Filter by tags if provided
    tag_filter = request.GET.get('tag')
    if tag_filter:
        blogs = blogs.filter(tags__icontains=tag_filter)

    context = {
        'blogs': blogs,
        'selected_tag': tag_filter,
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, is_published=True)

    # Get related blogs (same tags or author)
    related_blogs = Blog.objects.filter(is_published=True).exclude(id=blog.id)[:3]

    context = {
        'blog': blog,
        'related_blogs': related_blogs,
    }
    return render(request, 'blog/blog_detail.html', context)

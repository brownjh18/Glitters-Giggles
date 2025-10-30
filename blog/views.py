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

    # Get the blog's position in the list for image numbering
    all_blogs = list(Blog.objects.filter(is_published=True).order_by('-published_at'))
    blog_index = all_blogs.index(blog) + 1

    # Add index to related blogs for proper image mapping
    related_blogs_with_index = []
    for related_blog in related_blogs:
        related_index = all_blogs.index(related_blog) + 1
        related_blogs_with_index.append((related_blog, related_index))

    context = {
        'blog': blog,
        'related_blogs': related_blogs,
        'related_blogs_with_index': related_blogs_with_index,
        'blog_index': blog_index,
    }
    return render(request, 'blog/blog_detail.html', context)

from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category 

def category_list(request):
    categories = Category.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/category_list.html', {'categories': categories})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/post_detail.html', {'category': category})


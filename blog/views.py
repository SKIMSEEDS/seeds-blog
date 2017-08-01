from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category 
from .forms import PostForm
from django.shortcuts import redirect

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

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
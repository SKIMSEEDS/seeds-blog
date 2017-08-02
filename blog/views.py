from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category 
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


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
    return render(request, 'blog/category_detail.html', {'category': category})
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

class PolHomePageView(TemplateView):
    template_name = "blog/politicalhome.html"

class SociHomePageView(TemplateView):
    template_name = "blog/socialhomepage.html"

class EnviHomePageView(TemplateView):
    template_name = "blog/environmentalhome.html"


class SeedsHomePageView(TemplateView):
    template_name = "blog/base.html"

class GlobalWarmingPageView(TemplateView):
     template_name = "blog/envisubtopic1.html"

class AnimalRightsPageView(TemplateView):
     template_name = "blog/envisubtopic2.html"

class OtherPageView(TemplateView):
     template_name = "blog/envisubtopic3.html"


class GovernmentPageView(TemplateView):
     template_name = "blog/polisubtopic1.html"

class ActivismPageView(TemplateView):
     template_name = "blog/polisubtopic2.html"

class RightsPageView(TemplateView):
     template_name = "blog/polisubtopic3.html"


class LGBTQPageView(TemplateView):
     template_name = "blog/socisubtopic1.html"

class HealthPageView(TemplateView):
     template_name = "blog/socisubtopic2.html"

class SociOtherPageView(TemplateView):
     template_name = "blog/socisubtopic3.html"

class AboutUsPageView(TemplateView):
     template_name = "blog/about.html"

class ContactUsPageView(TemplateView):
     template_name = "blog/contactus.html"

class MeetTheTeamPageView(TemplateView):
     template_name = "blog/meettheteam.html"




    
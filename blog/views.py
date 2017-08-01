from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})

def category_list(request):
    return render(request, 'blog/category_list.html', {})

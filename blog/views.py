from django.shortcuts import render,get_object_or_404
from .models import Blog

def home(request):
    ps = Blog.objects.all
    return render(request, 'blog/home.html',{'posts':ps})

def post(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/post.html',{'post':post})

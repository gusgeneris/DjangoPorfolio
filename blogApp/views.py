from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def render_posts(request):
    posts = Post.objects.all()
    return render(request,'blog.html', {'posts':posts})

def post(request,id_post):
    post = get_object_or_404(Post, pk=id_post)
    return render(request,'post.html',{'post': post})
    
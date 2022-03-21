from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def render_posts(request):
    
    posts = Post.objects.all().order_by('-date')
    return render(request,'blog.html', {'posts':posts})

def post(request,id_post):
    
    post = get_object_or_404(Post, pk=id_post)
    return render(request,'post.html',{'post': post})

def list_post_categoria(request,id_categoria):
    
    posts = Post.objects.filter(categorias=id_categoria).order_by('-date')
    categoria = Categoria.objects.get(pk=id_categoria)
    return render(request,'categoria.html',{'posts' : posts,'categoria' : categoria})
    
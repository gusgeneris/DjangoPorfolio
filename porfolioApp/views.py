from django.shortcuts import render
from .models import *
from blogApp.models import Post

# Create your views here.
def home(request):
    """Home Page"""
    posts = Post.objects.order_by('-date')[0:6]
    return render(request,'home.html',{'posts':posts})

def list_projects(request):
    """List Projects"""
    
    projects = Project.objects.all()
    return render (request,'projects.html',{'projects':projects})

def about_me(request):
    return render (request,'about.html')
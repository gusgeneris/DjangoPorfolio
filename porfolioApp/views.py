from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    """Home Page"""
    return render(request,'home.html')

def list_projects(request):
    """List Projects"""
    
    projects = Project.objects.all()
    return render (request,'projects.html',{'projects':projects})

def about_me(request):
    return render (request,'about.html')
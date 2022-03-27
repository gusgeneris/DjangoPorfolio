from django.shortcuts import render
from .models import *
from blogApp.models import Post
from django.core.mail import send_mail
from DjangoPorfolio.settings import dev

# Create your views here.
def home(request):
    """Home Page"""
    posts = Post.objects.order_by('-date')[0:6]  
    
    
    """Formulario de Contacto"""
    if request.method == 'POST':
            
        subjet=request.POST['asunto']
        message=request.POST['mensaje'] +" "+request.POST['email']
        
        email_form=dev.EMAIL_HOST_USER
        
        recipient_list=['gusgeneris92@gmail.com']
        
        send_mail(subjet,message,email_form,recipient_list)
          
    return render(request,'home.html',{'posts':posts})

def list_projects(request):
    """List Projects"""
    
    projects = Project.objects.all()
    return render (request,'projects.html',{'projects':projects})

def about_me(request):
    return render (request,'about.html')

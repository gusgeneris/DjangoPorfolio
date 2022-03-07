from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='blog/imagenes')
    date = models.DateTimeField(auto_now_add=True)
    
    
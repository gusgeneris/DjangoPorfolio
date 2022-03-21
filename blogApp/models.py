from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='blog/imagenes')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nombre
  

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Categoria)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.titulo
    
    
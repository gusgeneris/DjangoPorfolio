from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to="porfolioApp/image/")
    git_dir = models.URLField(blank=True, null=True)
    demo_dir = models.URLField(blank=True, null=True)

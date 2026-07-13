from django.db import models

# from local apps
from applications.autor.models import Autor
# Import managers
from .managers import LibroManager

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(
        max_length=30
    )
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(
        max_length=50
    )
    fecha = models.DateField('Fechad de lanzamiento')
    portada = models.ImageField(upload_to='portada', blank=True)
    visitas = models.PositiveIntegerField()
    
    objects = LibroManager()
    
    def __str__(self):
        return self.titulo
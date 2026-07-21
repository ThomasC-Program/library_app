from django.db import models

# Create your models here.
from applications.libro.models import Libro
from applications.autor.models import Persona

# from managers
from .managers import PrestamoManager

class Lector(Persona):
    
    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

class Prestamo(models.Model):
    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE,
        related_name='libro_prestamo'
    )
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE
    )
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(
        blank=True,
        null=True,
    )
    
    devuelto = models.BooleanField()
    
    objects = PrestamoManager()
    
    def save(self, *args, **kwargs):
        
        print('=============')
        self.libro.stok = self.libro.stok -1
        self.libro.save()
        
        super(Prestamo, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.libro.titulo
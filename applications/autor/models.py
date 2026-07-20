from django.db import models

# managers

from .managers import AutorManager



class Autor(models.Model):
    nombres = models.CharField(
        max_length=50
    )
    apellidos = models.CharField(
        max_length=50
    )
    nacionalidad = models.CharField(
        max_length=20
    )
    edad = models.PositiveIntegerField(default=0)
    
    objects = AutorManager()
    
    def __str__(self):
        return str(self.id) + '-' + self.nombres + '-' + self.apellidos
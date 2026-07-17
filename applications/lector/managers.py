import datetime

from django.db import models

from django.db.models import Q, Count


class PrestamoManager(models.Manager):
    """ procedimientos para prestamo """
    
    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id='1'
        )
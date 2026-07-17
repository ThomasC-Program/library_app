import datetime

from django.db import models

from django.db.models import Q, Count, Avg, Sum


class PrestamoManager(models.Manager):
    """ procedimientos para prestamo """
    
    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id='2'
        ).aggregate(
            promedio_edad=Avg('lector__edad'),
            suma_edad=Sum('lector__edad'),
        )
        return resultado
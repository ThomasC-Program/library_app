import datetime

from django.db import models

from django.db.models import Q

class LibroManager(models.Manager):
    """managers para el modelo autor"""
    
    def listar_libros(self, kword):
        
        resultado = self.filter(
            titulo__icontains = kword,
            fecha__range = ('2025-01-01','2026-12-12'),
        )
        
        return resultado
    
    def listar_libros2(self, kword, fecha1, fecha2):
        
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        
        resultado = self.filter(
            titulo__icontains = kword,
            fecha__range = (date1, date2),
        )
        
        return resultado
    
    def listar_libros_categoria(self, categoria):
        
        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')
        
class CategoriaManager (models.Manager):
    """ managers para el modelo autor """
    
    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()
from django.db import models

from django.db.models import Q

class AutorManager(models.Manager):
    """managers para el modelo autor"""
    
    def buscar_autor(self, kword):
        
        resultado = self.filter(
            nombre__icontains = kword
        )
        
        return resultado
    
    def buscar_autor2(self, kword):
        
        resultado = self.filter(
            Q(nombre__icontains = kword) | Q(apellidos__icontains = kword)
        ) 
        
        return resultado
    
    def buscar_autor3(self, kword):
        
        resultado = self.filter(
            nombre__icontains = kword
        ).exclude(
            Q(edad__icontains=21) | Q(edad__icontains=23)
        )
        
        return resultado
    
    def buscar_autor4(self, kword):
        
        resultado = self.filter(
            edad__gt =18, #Mayor que
            edad__lt=30,  #Menor que
        ).order_by('apellidos','nombre', 'id')
        
        return resultado
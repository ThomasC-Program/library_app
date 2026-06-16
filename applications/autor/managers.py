from django.db import models

class AutorManager(models.Manager):
    """managers para el modelo autor"""
    
    def listar_autores(self):
        
        return self.all()
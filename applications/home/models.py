from django.db import models

# Create your models here.
class Persona(models.Model):
    
    full_name = models.CharField('nombres', max_length=50)
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=10)
    
    class Meta:
        
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'
        unique_together = ['pais','apelativo']
        constraints = [
            models.CheckConstraint(condition=models.Q(edad__gte=18), name='edad_mayor_18')
        ]
        # abstract = True Para que no se tome en cuenta como parte del modelo de datos en la base de datos
    def __str__(self):
        
        return self.full_name

class Empleados(Persona):
    empleado = models.CharField('Empleo', max_length=50)
    
class Cliente(Persona):
    email = models.EmailField('Email')
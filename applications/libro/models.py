from django.db import models
from django.db.models.signals import post_save

# apps tercer
from PIL import Image
# from local apps
from applications.autor.models import Autor
# Import managers
from .managers import LibroManager, CategoriaManager

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(
        max_length=30
    )
    objects = CategoriaManager()
    
    def __str__(self):
        return str(self.id) + ' - ' + self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria_libro'
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(
        max_length=50
    )
    fecha = models.DateField('Fechad de lanzamiento')
    portada = models.ImageField(upload_to='portada', blank=True)
    visitas = models.PositiveIntegerField()
    stok = models.PositiveIntegerField(default=0)
    
    objects = LibroManager()
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo', 'fecha']
    
    def __str__(self):
        return str(self.id) + '-' + self.titulo

#Optimizar la imagen que esta cargada en servidor para que al momento de cargar sea los mas optimo posible
def optimize_image(sender, instance, **kwargs):
    print("====")
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimaze=True)
    
    print(instance)
    
post_save.connect(optimize_image, sender=Libro)


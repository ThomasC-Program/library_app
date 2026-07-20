from django.contrib import admin
from .models import Persona, Empleados, Cliente

# Register your models here.
admin.site.register(Persona)
admin.site.register(Empleados)
admin.site.register(Cliente)
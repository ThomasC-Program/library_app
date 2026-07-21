from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic.edit import FormView

# local apps
from .models import Prestamo, Lector

# forms
from .forms import PrestamoForm, MultiplePrestamoForm
# Create your views here.

class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html' #Crear URL y template para acceder a esta vista
    form_class = PrestamoForm
    success_url = '.'
    
    def form_valid(self, form):
        
        # 1ra forma de hacer un registro
        #Prestamo.objects.create(
        #   lector=form.cleaned_data['lector'],
        #    libro=form.cleaned_data['libro'],
        #    fecha_prestamo=date.today(),
        #    devuelto=False,
        #)
        # 2da forma de hacer un registro
        prestamo = Prestamo(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False,
        )
        prestamo.save()
        
        libro = form.cleaned_data['libro']
        libro.stok = libro.stok - 1
        libro.save()
        
        return super(RegistrarPrestamo, self).form_valid(form)
    
class AddPrestamo(FormView):
    template_name = "lector/add_prestamo.html"
    form_class = PrestamoForm
    success_url = '.'
    
    def form_valid(self, form):
        
        obj, created = Prestamo.objects.get_or_create( #Probar tambien con update_or_create
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            devuelto = False,
            defaults={
                'fecha_prestamo': date.today()
            }
        )
        
        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')

class AddMultiplePrestamo(FormView):
    template_name = "lector/add_multiple_prestamo.html"
    form_class = MultiplePrestamoForm
    success_url = '.'
    def form_valid(self, form):
        
        lector = form.cleaned_data['lector']
        
        libros_ya_prestados = Prestamo.objects.filter(
            lector=lector,
            devuelto=False
        ).values_list('libro_id', flat=True)
        #Registrar y guardar multiples de datos en solo una consulta
        prestamos = []
        for l in form.cleaned_data['libros']:
            if l.id not in libros_ya_prestados:
                
                prestamo = Prestamo(
                    lector = lector,
                    libro = l,
                    fecha_prestamo = date.today(),
                    devuelto = False,
                )
                prestamos.append(prestamo)
                l.stok = l.stok -1
                l.save()
        
        Prestamo.objects.bulk_create(
            prestamos
        )
        
        return super(AddMultiplePrestamo, self). form_valid(form)

# Vista para añadir multiples prestamos pero sin validacion de stock
# class AddMultiplePrestamo(FormView):
#     template_name = "lector/add_multiple_prestamo.html"
#     form_class = MultiplePrestamoForm
#     success_url = '.'
#     def form_valid(self, form):
        
#         #Registrar y guardar multiples de datos en solo una consulta
#         prestamos = []
#         for l in form.cleaned_data['libros']:
#             prestamo = Prestamo(
#                 lector = form.cleaned_data['lector'],
#                 libro = l,
#                 fecha_prestamo = date.today(),
#                 devuelto = False,
#             )
#             prestamos.append(prestamo)
        
#         Prestamo.objects.bulk_create(
#             prestamos
#         )
        
#         return super(AddMultiplePrestamo, self). form_valid(form)
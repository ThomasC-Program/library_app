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
        
        obj, created = Prestamo.objects.get_or_create(
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
        
        return super(AddMultiplePrestamo, self). form_valid(form)
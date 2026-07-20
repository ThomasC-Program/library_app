from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Prestamo

from .forms import PrestamoForm
# Create your views here.

class RegistrarPrestamo(FormView):
    template_name = 'prestamo/add.html'
    form_class = PrestamoForm
    success_url = '.'
    
    def form_valid(self, form):
        
        return super(RegistrarPrestamo, self).form_valid(form)
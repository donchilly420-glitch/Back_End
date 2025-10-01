from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LibroForm, AutorForm, LectorForm, PrestamoForm
from django.shortcuts import render
from .models import (Comuna, Nacionalidad, Direccion, Autor, Biblioteca, Libro, Lector, Prestamo)
from rest_framework import viewsets
from .models import (Comuna,Nacionalidad,Direccion,Autor,Biblioteca,Libro,Lector,Prestamo)
from .serializer import (Comuna_Serializer,nacionalidad_Serializer,direccion_Serializer,autor_Serializer,
Biblioteca_Serializer, Libro_Serializer,Lector_Serializer, Prestamo_Serializer)

def home(request):
    libros = Libro.objects.all()
    autores = Autor.objects.all()
    lectores = Lector.objects.all()
    prestamos = Prestamo.objects.all()

    context = {
        'libros': libros,
        'autores': autores,
        'lectores': lectores,
        'prestamos': prestamos,
    }
    return render(request, 'home/inicio.html', context)

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = Comuna_Serializer


class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = nacionalidad_Serializer


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = direccion_Serializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = autor_Serializer


class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = Biblioteca_Serializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = Libro_Serializer


class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = Lector_Serializer


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = Prestamo_Serializer

class LibroList(ListView):
    model = Libro
    template_name = 'libro/lista.html'
    context_object_name = 'libros'

class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/form.html'
    success_url = reverse_lazy('libro_list')

class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/form.html'
    success_url = reverse_lazy('libro_list')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'libro/confirm_delete.html'
    success_url = reverse_lazy('libro_list')

# ---- AUTORES ----
class AutorList(ListView):
    model = Autor
    template_name = 'autor/lista.html'
    context_object_name = 'autores'

class AutorCreate(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor/form.html'
    success_url = reverse_lazy('autor_list')

class AutorUpdate(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor/form.html'
    success_url = reverse_lazy('autor_list')

class AutorDelete(DeleteView):
    model = Autor
    template_name = 'autor/confirm_delete.html'
    success_url = reverse_lazy('autor_list')

# ---- LECTORES ----
class LectorList(ListView):
    model = Lector
    template_name = 'lector/lista.html'
    context_object_name = 'lectores'

class LectorCreate(CreateView):
    model = Lector
    form_class = LectorForm
    template_name = 'lector/form.html'
    success_url = reverse_lazy('lector_list')

class LectorUpdate(UpdateView):
    model = Lector
    form_class = LectorForm
    template_name = 'lector/form.html'
    success_url = reverse_lazy('lector_list')

class LectorDelete(DeleteView):
    model = Lector
    template_name = 'lector/confirm_delete.html'
    success_url = reverse_lazy('lector_list')

# ---- PRÉSTAMOS ----
class PrestamoList(ListView):
    model = Prestamo
    template_name = 'prestamo/lista.html'
    context_object_name = 'prestamos'

class PrestamoCreate(CreateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamo/form.html'
    success_url = reverse_lazy('prestamo_list')

class PrestamoUpdate(UpdateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamo/form.html'
    success_url = reverse_lazy('prestamo_list')

class PrestamoDelete(DeleteView):
    model = Prestamo
    template_name = 'prestamo/confirm_delete.html'
    success_url = reverse_lazy('prestamo_list')
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

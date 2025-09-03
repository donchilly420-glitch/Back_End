from rest_framework import viewsets
from .models import (comuna,nacionalidad,direccion,autor,Biblioteca,Libro,Lector,Prestamo)
from .serializer import (Comuna_Serializer,nacionalidad_Serializer,direccion_Serializer,autor_Serializer,
Biblioteca_Serializer, Libro_Serializer,Lector_Serializer, Prestamo_Serializer)


class ComunaViewSet(viewsets.ModelViewSet):
    queryset = comuna.objects.all()
    serializer_class = Comuna_Serializer


class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = nacionalidad.objects.all()
    serializer_class = nacionalidad_Serializer


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = direccion.objects.all()
    serializer_class = direccion_Serializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = autor.objects.all()
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

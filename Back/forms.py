from django import forms
from .models import Libro, Autor, Lector, Prestamo

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'genero', 'paginas', 'copias', 'id_autor', 'id_biblioteca']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'pseudonimo', 'id_nacionalidad', 'bio']

class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = ['nombre', 'rut', 'digito_verificador', 'correo', 'telefono', 'direccion', 'id_biblioteca']

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['id_libro', 'id_lector', 'fecha_prestamo', 'fecha_devolucion']

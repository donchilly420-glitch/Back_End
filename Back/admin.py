from django.contrib import admin
from .models import nacionalidad, autor, comuna, direccion, Biblioteca, Libro, Lector, Prestamo
# Register your models here.

admin.site.register(nacionalidad)
admin.site.register(autor)
admin.site.register(comuna)
admin.site.register(direccion)
admin.site.register(Biblioteca)
admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Prestamo)


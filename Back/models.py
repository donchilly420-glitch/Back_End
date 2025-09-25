from django.db import models

# Create your models here.
class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, null=False)
    nacionalidad = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nacionalidad


class Autor(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    pseudonimo = models.CharField(max_length=50, null=True)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    codigo = models.CharField(max_length=5, null=False)
    comuna = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.comuna


class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=10, null=True)
    departamento = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.id_comuna.comuna}"


class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    genero = models.CharField(max_length=100, null=True)
    paginas = models.IntegerField(null=False)
    copias = models.IntegerField(default=1)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Lector(models.Model):
    nombre = models.CharField(max_length=150, null=False)
    rut = models.CharField(max_length=12, null=False, unique=True)
    digito_verificador = models.CharField(max_length=1, null=False)
    correo = models.EmailField(max_length=150, null=False, unique=True)
    telefono = models.CharField(max_length=20, null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f"{self.id_libro.titulo} prestado a {self.id_lector.nombre}"

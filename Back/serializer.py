from rest_framework import serializers
from .models import comuna, nacionalidad, direccion, autor, Biblioteca, Libro, Lector, Prestamo


class Comuna_Serializer(serializers.ModelSerializer):
    class Meta:
        model = comuna
        fields = '__all__'


class nacionalidad_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = nacionalidad
        fields = '__all__'


class direccion_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = direccion
        fields = '__all__'


class autor_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = autor
        fields = '__all__'


class Biblioteca_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = '__all__'


class Libro_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'


class Lector_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lector
        fields = '__all__'


class Prestamo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'




        
       

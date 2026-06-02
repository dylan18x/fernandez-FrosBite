from rest_framework import serializers
from .models import Producto, Sabor  

class SaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sabor
        fields = ["id", "nombre"]

class ProductoSerializer(serializers.ModelSerializer):
    marca_nombre = serializers.CharField(source="marca.nombre", read_only=True)

    class Meta:
        model = Producto
        fields = ["id", "marca", "marca_nombre", "modelo", "anio", "placa", "color", "creado_en"]
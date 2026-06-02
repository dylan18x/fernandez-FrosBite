from rest_framework import serializers
from .models import Producto, Sabor  

class SaborSerializer(serializers.ModelSerializer):
    conteo = 0
    if(Producto.estado == True):
        conteo += 1
    total_productos = serializers.IntegerField(source="conteo", read_only=True)
    class Meta:
        model = Sabor
        fields = ["id", "nombre","total_productos"]

class ProductoSerializer(serializers.ModelSerializer):
    sabor_nombre = serializers.CharField(source="sabor.nombre", read_only=True)
    class Meta:
        model = Producto
        fields = ["id", "sabor", "sabor_nombre", "nombre", "codigo", "precio", "costoInsumos", "estado"]
from django.db import models

class Sabor(models.Model):
    nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    sabor = models.ForeignKey(Sabor,on_delete=models.PROTECT, related_name="productos")
    nombre = models.CharField(max_length=120, unique=True)
    codigo = models.CharField(max_length=120, unique=True)
    precio = models.CharField(max_length=120, unique=True)
    costoInsumos = models.CharField(max_length=120, unique=True)
    estado = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return f"{self.marca.nombre} {self.modelo} ({self.placa})"
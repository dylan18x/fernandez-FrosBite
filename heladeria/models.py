from django.db import models

class Sabor(models.Model):
    nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    sabor = models.ForeignKey(Sabor,on_delete=models.PROTECT, related_name="productos")
    nombre = models.CharField(max_length=120, unique=True)
    codigo = models.CharField(max_length=120, unique=True)
    precio = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    costoInsumos = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sabor.nombre} {self.nombre} ({self.precio})"
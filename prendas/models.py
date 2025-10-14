from django.db import models

class Ropa(models.Model):
    marca = models.CharField(max_length=100)
    talla = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_fabricacion = models.DateField()

    def __str__(self):
        return f"{self.marca} - Talla {self.talla} (${self.precio})"

from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(default="Sin contenido")
    fecha = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=50, null=False, blank=False, default="Desconocido")

    def __str__(self):
        return self.titulo

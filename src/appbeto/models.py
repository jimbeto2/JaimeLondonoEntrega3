from django.db import models

# Create your models here.

class MisBlog (models.Model):
    categoria = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    icono = models.ImageField(upload_to="iconos_blog", blank=True, null=True)
    fecha = models.DateField(max_length=255)
    nick = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.icono} {self.categoria} {self.titulo} Actualizado: {self.fecha}  Autor: {self.nick}"

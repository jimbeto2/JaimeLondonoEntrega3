from django.db import models

# Create your models here.

class Familiar (models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}: {self.edad} años"

class Regalo (models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255, blank=True)
    edad = models.IntegerField()
    regalo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años, Regalo: {self.regalo}"

class Menu (models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255, blank=True)
    plato = models.CharField(max_length=255)
    bebida = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Plato Fuerte: {self.plato}, Bebida: {self.bebida}"

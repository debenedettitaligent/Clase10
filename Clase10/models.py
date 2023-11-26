from django.db import models

class Perros(models.Model):
    raza = models.CharField(max_length=30)
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()

class Veterinario(models.Model):
    nombre = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=50)

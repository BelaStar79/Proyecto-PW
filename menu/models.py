from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    disponibilidad = models.IntegerField()
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=4, decimal_places=2)


class Menu(models.Model):
    id_menu = models.IntegerField(primary_key=True)
    nombre_menu = models.CharField(max_length=100)
    lista_productos = models.ManyToManyField(Producto)

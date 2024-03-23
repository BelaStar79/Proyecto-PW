from django.db import models


# Create your models here.
class Usuario(models.Model):
    ci = models.IntegerField()
    nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    user = models.CharField(primary_key=True, max_length=50)
    contrasena = models.TextField()


class Cliente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class PuestoTrabajo(models.Model):
    id_puesto = models.CharField(max_length=100, primary_key=True)
    nombre_puesto = models.CharField(max_length=100)


class Empleado(models.Model):
    segundo_apellido = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puesto = models.ForeignKey(PuestoTrabajo, on_delete=models.PROTECT)

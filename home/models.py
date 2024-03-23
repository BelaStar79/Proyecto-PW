from django.db import models


# Create your models here.
class Comentario(models.Model):
    id_comentario = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    correo_usuario = models.CharField(max_length=100)
    comentario_usuario = models.TextField()

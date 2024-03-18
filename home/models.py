from django.db import models


# Create your models here.
class Opinion(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    submission = models.TextField()

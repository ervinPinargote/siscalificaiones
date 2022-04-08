from django.db import models


# Create your models here.

class Configuracion(models.Model):
    entidad = models.CharField(max_length=200)
    autoridad = models.CharField(max_length=200, null=True)
    logo = models.ImageField(null=True)
    papel_tapiz = models.ImageField(null=True)
    administracion = models.CharField(max_length=200, blank=True, null=True)

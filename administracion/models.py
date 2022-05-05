from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Configuracion(models.Model):
    entidad = models.CharField(max_length=200)
    autoridad = models.CharField(max_length=200, null=True)
    logo = models.ImageField(null=True)
    papel_tapiz = models.ImageField(null=True)
    administracion = models.CharField(max_length=200, blank=True, null=True)


class certamen(models.Model):
    nombre_certamen = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_certamen


class parametros(models.Model):
    nombre_parametro = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_parametro

class candidatas(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField(null=True)
    representa = models.CharField(max_length=200, null=True)
    acerca = models.TextField(null=True, default="")
    foto = models.ImageField(upload_to="candidatas", null=True)
    id_certamen = models.ForeignKey('certamen', on_delete=models.CASCADE, verbose_name="Participa En: ")

    def __str__(self):
        return self.nombres + " " + self.apellidos

class calificacion_parametros(models.Model):
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)
    id_candidata = models.ForeignKey('candidatas', on_delete=models.CASCADE, verbose_name="Candidata")
    id_parametro = models.ForeignKey('parametros', on_delete=models.CASCADE, verbose_name="Parametro")
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario Califica ")
    id_metricas = models.ForeignKey('metricas_parametros', on_delete=models.CASCADE, verbose_name="METRICAS")


class usuario_calificador(models.Model):
    id_certamen = models.ForeignKey('certamen', on_delete=models.CASCADE, verbose_name="Certamen")
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

class parametros_certamen(models.Model):
    id_parametro = models.ForeignKey('parametros', on_delete=models.CASCADE, verbose_name="Parametro")
    id_certamen = models.ForeignKey('certamen', on_delete=models.CASCADE, verbose_name="Certamen")

class metricas_parametros(models.Model):
    nombremetrica = models.CharField(max_length=100)
    puntacionmax = models.DecimalField(max_digits=5, decimal_places=2)
    idparametrof = models.ForeignKey('parametros', on_delete=models.CASCADE, verbose_name="Parametro")
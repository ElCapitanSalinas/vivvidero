from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(models.Model):
    # id = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    customer = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Apartamentos(models.Model):
    userid = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    area = models.CharField(max_length=200, null=True)
    precio = models.CharField(max_length=200)
    precio_nuevo = models.CharField(max_length=200)
    precio_remo = models.CharField(max_length=200, null=True)
    estrato = models.CharField(max_length=200)
    comodidades = models.CharField(max_length=200)
    ktc = models.ImageField(upload_to='images/', null=True)
    ktc_new = models.ImageField(upload_to='images/', null=True)
    hall = models.ImageField(upload_to='images/', null=True)
    hall_new = models.ImageField(upload_to='images/', null=True)
    bath = models.ImageField(upload_to='images/', null=True)
    bath_new = models.ImageField(upload_to='images/', null=True)
    room = models.ImageField(upload_to='images/', null=True)
    room_new = models.ImageField(upload_to='images/', null=True)


    def __str__(self):
        return self.userid

class Estadisticas(models.Model):
    cpd = models.CharField("consultas por dia", max_length=200)
    cpm = models.CharField("consultas por mes", max_length=200)
    sav = models.CharField("similitude average", max_length=200)
    efc = models.CharField("efficiency", max_length=200)

class AdminUser(AbstractBaseUser, models.Model):
    # id = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=200)


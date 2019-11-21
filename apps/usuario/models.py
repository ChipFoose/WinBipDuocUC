from django.db import models

# Create your models here.

class Tarjeta(models.Model):
    id_tarjeta = models.IntegerField(primary_key=True)
    codigo = models.IntegerField()
    saldo = models.IntegerField()

class Persona(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length= 40)
    apellido = models.CharField(max_length = 40)
    correo = models.EmailField()
    direccion = models.CharField(max_length = 100)
    clave = models.CharField(max_length = 50)
    id_tarjeta = models.ForeignKey(Tarjeta, null = True, blank = True, on_delete = models.DO_NOTHING)


class Insignia(models.Model):
    id_insignia = models.IntegerField(primary_key=True)
    nombre_insignia = models.CharField(max_length = 30)
    imagen_insignia = models.ImageField


class Usuario_insignia(models.Model):
    id = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Persona, null = True , blank = True , on_delete = models.DO_NOTHING)
    id_insignia = models.ForeignKey(Insignia, null = True , blank = True , on_delete = models.DO_NOTHING)
    fecha = models.DateField
    
    

class Tipo_viaje(models.Model):
    id_tipo_viaje = models.IntegerField(primary_key=True)
    nombre_viaje = models.CharField(max_length = 15)
    valor_puntos = models.IntegerField


class Viaje(models.Model):
    id_viaje = models.IntegerField(primary_key=True)
    id_tipo_viaje = models.ForeignKey(Tipo_viaje, null = True, blank = True, on_delete = models.DO_NOTHING)
    id_usuario = models.ForeignKey(Persona, null = True , blank = True , on_delete = models.DO_NOTHING)






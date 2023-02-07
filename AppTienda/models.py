from django.db import models


class Tienda(models.Model):

       album = models.CharField(max_length=55)
       artista = models.CharField(max_length=55)
       fechaLanzamiento = models.IntegerField(blank=True)
       genero = models.CharField(max_length=55)
       subGenero = models.CharField(max_length=255)
       formato = models.CharField(max_length=55)
       paisOrigen = models.CharField(max_length=55)
       disponibilidad = models.BooleanField()
       #precio = models.IntegerField(blank=True)
       codigo = models.IntegerField(blank=True) #Este es el precio
       descripcion = models.CharField(max_length=255) 

class Cliente(models.Model):
       nombre = models.CharField(max_length=55)
       apellido = models.CharField(max_length=55)
       mail = models.EmailField(max_length=60)
       usuario = models.CharField(max_length=55)

class Contacto(models.Model):
       nombre = models.CharField(max_length=55)
       telefono = models.IntegerField(blank=True)
       mail = models.EmailField(max_length=60)
       usuario = models.CharField(max_length=55)

class Cotizar(models.Model):
       album = models.CharField(max_length=55)
       artista = models.CharField(max_length=55)
       formato = models.CharField(max_length=55)
       descripcion = models.CharField(max_length=255)
       
       nombre = models.CharField(max_length=100)
       telefono = models.IntegerField(blank=True)
       mail = models.EmailField(max_length=60)

class Suscribete(models.Model):
       
       mail = models.EmailField(max_length=60)
       nombre = models.CharField(max_length=55)

class Preventa(models.Model):
       album = models.CharField(max_length=55)
       artista = models.CharField(max_length=55)
       formato = models.CharField(max_length=55)
       descripcion = models.CharField(max_length=255)       
       nombre = models.CharField(max_length=100)
       telefono = models.IntegerField(blank=True)
       mail = models.EmailField(max_length=60)


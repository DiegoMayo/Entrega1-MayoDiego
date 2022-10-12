from django.db import models

# Create your models here.

class Tienda(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    contacto=models.EmailField()
    
class Juego(models.Model):
    nombre=models.CharField(max_length=30)
    codigo=models.CharField(max_length=30)
    precio=models.CharField(max_length=30)
    feha_de_entrega=models.DateField()
    
    
class Cliente (models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    dni=models.CharField(max_length=10)
    entregado=models.BooleanField()
    


    

    
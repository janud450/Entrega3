from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    nit = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Garantia(models.Model):
    banco = models.CharField(max_length=50)
    contrato = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"Vigencia {self.fecha_inicial}, {self.fecha_final}"

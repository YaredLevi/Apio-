from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    saldo = models.FloatField()

class Candado(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    latitud = models.FloatField()
    altitud = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
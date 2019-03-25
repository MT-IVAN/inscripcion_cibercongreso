from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    cupo = models.IntegerField()
    fecha = models.DateTimeField()    
    lugar = models.CharField(max_length=100)
    ponente = models.CharField(max_length=100)
    computador = models.BooleanField()
    
    def __str__(self):
            return '{}'.format(self.nombre)


class Persona(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=10)
    nombreCompleto = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha = models.DateField()
    numCupon = models.CharField(max_length=6)
    valor = models.CharField(max_length=9)
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
            return '{}'.format(self.nombreCompleto)




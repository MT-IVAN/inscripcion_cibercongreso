from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    cupo = models.IntegerField()
    fecha = models.DateField()
    hI = models.TimeField()
    hF = models.TimeField()
    lugar = models.CharField(max_length=100)
    ponente = models.CharField(max_length=100)
    
    #Devuelve el nombre
    def __str__(self):
            return '{}'.format(self.nombre)
    # unicode y Meta son para organizar las lista por nobre
    def __unicode__(self): 
        return self.nombre
    #organizar lista
    class Meta:
        ordering = ['nombre']



class Persona(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nombreCompleto = models.CharField(max_length=60)
    fecha = models.DateField()
    numCupon = models.CharField(max_length=6)
    valor = models.CharField(max_length=9)
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
            return '{}'.format(self.nombreCompleto)
    



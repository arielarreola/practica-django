from django.db import models

class Docente(models.Model):
    nombre=models.CharField(max_length=255)
    ocupacion=models.CharField(max_length=255)
    area=models.CharField(max_length=80)
    no_materias=models.IntegerField()
    
    
    def __str__(self):
        return f'{self.nombre}- {self.area}'
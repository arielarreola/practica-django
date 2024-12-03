from django.db import models

class Alumno(models.Model):
    OPCIONES=(
        ('CIB','Ingenieria Cibernetica'),
        ('PSI','Psicologia'),
        ('NUT', 'Nutricion'),
        ('DER','Derecho'),
        ('EDI','Educación')
        )
    nombre=models.CharField(max_length=255)
    fecha_nacimiento=models.DateField()
    carrera=models.CharField(choices=OPCIONES,max_length=255)
    semestre=models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre}, {self.carrera}'
from django.contrib import admin

# Register your models here.
from .models.alumno import Alumno
from .models.docente import Docente
admin.site.register(Alumno)
admin.site.register(Docente)
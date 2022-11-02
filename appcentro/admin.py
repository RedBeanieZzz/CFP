from django.contrib import admin

from .models import Alumnos, Cursos, Modulos, AlumnosPorModulos, Nacionalidad, Nomenclador

# Register your models here.
admin.site.register(Alumnos)
admin.site.register(Cursos)
admin.site.register(Modulos)
admin.site.register(AlumnosPorModulos)
admin.site.register(Nacionalidad)
admin.site.register(Nomenclador)
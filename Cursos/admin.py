from django.contrib import admin
from Cursos.models import Cursos, CursoAdmin, Estudiantes, EstudianteAdmin

admin.site.register(Cursos,CursoAdmin)
admin.site.register(Estudiantes,EstudianteAdmin)
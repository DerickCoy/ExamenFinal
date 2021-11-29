from django.db import models
from django.contrib import admin

class Estudiantes(models.Model):
    carne= models.CharField(max_length=9)
    nombres  =   models.CharField(max_length=50)
    aplledios= models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.carne

class Cursos(models.Model):
    nombrecurso   = models.CharField(max_length=100)
    estudiante    = models.ManyToManyField(Estudiantes, through='Cursando')

    def __str__(self):
        return self.nombrecurso

class Cursando (models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

class CursandoInLine(admin.TabularInline):
    model = Cursando
    extra = 1

class EstudianteAdmin(admin.ModelAdmin):
    inlines = (CursandoInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (CursandoInLine,)
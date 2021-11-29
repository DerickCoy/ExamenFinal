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
    estudinate    = models.ManyToManyField(Estudiantes, through='Actuacion')

    def __str__(self):
        return self.nombrecurso

class Cursnado (models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

class CursnadoInLine(admin.TabularInline):
    model = Cursnado
    extra = 1

class EstudaniteAdmin(admin.ModelAdmin):
    inlines = (CursnadoInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (CursnadoInLine,)
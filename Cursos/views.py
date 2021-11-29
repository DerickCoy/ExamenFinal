from django.shortcuts import render
from django.contrib import messages
from .forms import CursosForm
from Cursos.models import  Cursos, Cursando


def curso_nuevo(request):
    if request.method == "POST":
        formulario = CursosForm(request.POST)
        if formulario.is_valid():
            curso = Cursos.objects.create(nombrecurso=formulario.cleaned_data['nombrecurso'])
            for estudiante_id in request.POST.getlist('estudiante'):
             cursando = Cursando(estudiante_id=estudiante_id, curso_id = curso.id)
             cursando.save()
            messages.add_message(request, messages.SUCCESS, 'Curso Guardada Exitosamente')
    else:
          formulario = CursosForm()
    return render(request, 'curso/curso_editar.html', {'formulario': formulario})

from django import forms
from .models import Cursos, Estudiantes


class CursosForm(forms.ModelForm):
#todos los campos del curso
    class Meta:
        model = Cursos
        fields = ('nombrecurso', 'estudiante')

    def __init__ (self, *args, **kwargs):
        super(CursosForm, self).__init__(*args, **kwargs)
        self.fields["estudiante"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["estudiante"].help_text = "Ingrese los Estudiantes del Curso"
        self.fields["estudiante"].queryset = Estudiantes.objects.all()
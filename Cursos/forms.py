from django import forms
from .models import Cursos, Estudiantes


class CursosForm(forms.ModelForm):
#todos los campos del curso
    class Meta:
        model = Cursos
        fields = ('nombre', 'estudiantes')

    def __init__ (self, *args, **kwargs):
        super(CursosForm, self).__init__(*args, **kwargs)
        self.fields["estudiantes"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["estudiantes"].help_text = "Ingrese los Estudiantes del Curso"
        self.fields["estudiantes"].queryset = Estudiantes.objects.all()
from django import forms

from administracion.models import calificacion_parametros




class CalificarParametrosCandidatasForm(forms.ModelForm):
    class Meta:
        model = calificacion_parametros
        fields = [
            'calificacion',
            'id_candidata',
            'id_parametro',
            'id_usuario',
        ]
        labels = {
            'calificacion': 'Total Calificado',
            'id_candidata': 'Candidata',
            'id_parametro': 'Parametro',
            'id_usuario': 'Usuario Calificador',
        }
        widgets = {
            'calificacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_candidata': forms.TextInput(attrs={'class': 'form-control'}),
            'id_parametro': forms.Select(attrs={'class': 'form-control'}),
            'id_usuario': forms.TextInput(attrs={'class': 'form-control'}),
        }

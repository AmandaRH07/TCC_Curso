from django import forms
from django.forms import ModelForm
from .models import Vacinas


class VacinasForm(forms.ModelForm):
    class Meta:
        model = Vacinas
        fields = ['tipo_vacina', 'data_vacinacao', 'dose', 'lote', 'local', 'fk_usuario_vacinas']
from django import forms
from django.forms import ModelForm
from .models import AvaliacaoDiaria


class AvaliacaoDiariaForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoDiaria
        fields = ['sintomas', 'observacoes']
from django import forms
from django.forms import ModelForm
from .models import TipoSanguineo


class TipoSanguineoForm(forms.ModelForm):
    class Meta:
        model = TipoSanguineo
        fields = ['tipo_sanguineo', 'doador', 'historico_doacoes']

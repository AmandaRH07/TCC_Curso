from django import forms
from django.forms import ModelForm

from .models import TipoSanguineo


class TipoSanguineoForm(forms.ModelForm):
    tipo_sanguineo = forms.ChoiceField(choices=TipoSanguineo.TIPO_SANGUINEO_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = TipoSanguineo
        fields = ['tipo_sanguineo','doador', 'historico_doacoes']

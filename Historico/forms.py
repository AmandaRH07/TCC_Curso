from django import forms
from django.forms import ModelForm
from .models import HistoricoConsultas


class HistoricoConsultasForm(forms.ModelForm):
    class Meta:
        model = HistoricoConsultas
        fields = ['lugar', 'data', 'infos_extras', 'receita', 'atestado']
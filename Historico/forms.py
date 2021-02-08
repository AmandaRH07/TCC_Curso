from django import forms
from django.forms import ModelForm
from .models import HistoricoConsultas, HistoricoFamiliar


class HistoricoConsultasForm(forms.ModelForm):
    class Meta:
        model = HistoricoConsultas
        fields = ['lugar', 'data', 'receita', 'atestado', 'fk_usuario_historico_consulta']

class HistoricoFamiliarForm(forms.ModelForm):
    class Meta:
        model = HistoricoFamiliar
        fields = ['doenca_hereditarias', 'grau_parentesco', 'fk_usuario_historico_familiar']
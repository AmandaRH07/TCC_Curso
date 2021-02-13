from django import forms
from django.forms import ModelForm
from .models import HistoricoConsultas, HistoricoFamiliar, DoencaCronica


class HistoricoConsultasForm(forms.ModelForm):
    class Meta:
        model = HistoricoConsultas
        fields = ['lugar', 'data', 'receita', 'atestado', 'fk_usuario_historico_consulta']

class HistoricoFamiliarForm(forms.ModelForm):
    class Meta:
        model = HistoricoFamiliar
        fields = ['doenca_hereditarias', 'grau_parentesco', 'fk_usuario_historico_familiar']

class DoencaCronicaForm(forms.ModelForm):
    class Meta:
        model = DoencaCronica
        fields = '__all__'

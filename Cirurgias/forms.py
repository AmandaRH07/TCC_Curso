from django import forms
from django.forms import ModelForm
from .models import Cirurgias

class CirurgiasForm(forms.ModelForm):
    class Meta:
        model = Cirurgias
        fields = ['cirurgia', 'hospital', 'data_cirurgia', 'infos_extras', 'fk_usuario_cirurgias']
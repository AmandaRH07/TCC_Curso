from django import forms
from .models import Medicamentos

class MedicacaoForm(forms.ModelForm):

    class Meta:
        model = Medicamentos
        fields = '__all__'
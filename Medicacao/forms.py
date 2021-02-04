from django import forms
from .models import Medicamentos

class EntryCreationForm(forms.ModelForm):

    class Meta:
        model = Medicamentos
        fields = '__all__'
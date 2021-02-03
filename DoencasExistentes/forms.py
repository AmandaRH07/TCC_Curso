from django import forms
from django.forms import ModelForm
from .models import DoencasExistentes


class DoencasExistentesForm(forms.ModelForm):
    class Meta:
        model = DoencasExistentes
        fields = '__all__'

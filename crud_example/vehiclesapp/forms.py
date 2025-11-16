from django import forms
from .models import vehiculo

class vehiculoForm(forms.ModelForm):
    class Meta:
        model = vehiculo
        fields = ['placa', 'marca', 'color', 'modelo']

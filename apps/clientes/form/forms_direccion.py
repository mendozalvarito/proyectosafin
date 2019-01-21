from django import forms
from apps.clientes.models import Direccion

"""
Constantes
"""

class DireccionForm(forms.ModelForm):

    class Meta:
        model = Direccion
        fields = ('Distrito', 'nombrebarrio', 'siglabarrio', 'detallebarrio')
        widgets = {}

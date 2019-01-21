from django import forms
from apps.clientes.models import Distrito

"""
Constantes
"""

class DistritoForm(forms.ModelForm):

    class Meta:
        model = Distrito
        fields = ('Distrito', 'nombrebarrio', 'siglabarrio', 'detallebarrio')
        widgets = {}

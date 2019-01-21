from django import forms
from apps.clientes.models import Barrio

"""
Constantes
"""

class BarrioForm(forms.ModelForm):

    class Meta:
        model = Barrio
        fields = ('Distrito','nombrebarrio','siglabarrio','detallebarrio')
        widgets = {}

from django import forms
from apps.clientes.models import Cliente,Persona,Instituciones
from apps.clientes.models import Direccion,Ubicacion,Barrio
from apps.clientes.models import Planservicios

"""
Constantes
"""
ERROR_MESSAGE_CI = {'required':'El numero de cedula de identidad es requerido','unique':'El numero de cedula de identidad ya se encuentra registrado','invalid': 'Ingrese el numero de cedula de identidad valido'}
SEXOS = (('F', 'Femenino'),('M', 'Masculino'))
FORMATO_FECHA = ['%Y-%m-%d']


class ClienteForm(forms.ModelForm):
    """
    Personas_Clientes
    Instituciones
    celularcliente
    emailcliente
    observacioncliente
    """

    class Meta:
        model = Cliente
        fields = ('Personas_Clientes','Instituciones','celularcliente','emailcliente','observacioncliente')
        widgets = {'Personas_Clientes': forms.TextInput(attrs={'class': 'form-control'}),
                   'Instituciones': forms.TextInput(attrs={'class': 'form-control'}),
                   'celularcliente': forms.TextInput(attrs={'class': 'form-control'}),
                   'emailcliente': forms.EmailInput(attrs={'class': 'form-control'}),
                   'observacioncliente': forms.TextInput(attrs={'class': 'form-control'})
                   }
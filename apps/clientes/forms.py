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


class PersonaForm(forms.ModelForm):
    """
    nombrepersona = form.CharField(max_length=20,label='Nombre',widget=form.TextInput(attrs={'class': 'form-control',}))
    paternopersona = form.CharField(max_length=20,label='Apellido Materno',widget=form.TextInput(attrs={'class': 'form-control',}))
    maternopersona = form.CharField(max_length=20,label='Apellido Paterno',widget=form.TextInput(attrs={'class': 'form-control',}))
    cipersona = form.CharField(max_length=20,label='Cedula Identidad',widget=form.TextInput(attrs={'class': 'form-control'}))
    generopersona1 = form.CharField(label='Sexo',widget=form.Select(choices=SEXOS,attrs={'class':'form-control'}))

    nacimientopersona = form.DateField(label='Fecha de Nacimiento',widget=form.DateInput(attrs={
        'class':'form-control',
        'maxlength':'10'
    }),input_formats=FORMATO_FECHA)"""

    class Meta:
        model = Persona
        fields = ('nombrepersona','paternopersona','maternopersona','cipersona','generopersona','nacimientopersona')
        widgets = {'nombrepersona': forms.TextInput(attrs={'class': 'form-control'}),
                   'paternopersona': forms.TextInput(attrs={'class': 'form-control'}),
                   'maternopersona': forms.TextInput(attrs={'class': 'form-control'}),
                   'cipersona': forms.TextInput(attrs={'class': 'form-control'}),
                   'generopersona': forms.Select(attrs={'class': 'form-control'}),
                   'nacimientopersona': forms.DateInput(attrs={'class': 'form-control'})}

    def clean_nombrepersona(self):
        nombrepersona = self.cleaned_data['nombrepersona']
        if not nombrepersona.isalpha():
            raise forms.ValidationError('No puede contener números')
        return nombrepersona
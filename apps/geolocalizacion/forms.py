from django import forms
from .models import Ubicacion


#formulario de ubicacion

class UbicacionForm(forms.ModelForm):

    class Meta:
        model = Ubicacion
        fields =[
            'latitudubicacion',
            'longitudubicacion',
            'descripcionubicacion',
        ]

        labels={
            'latitudubicacion':'Latitud',
            'longitudubicacion':'Longitud',
            'descripcionubicacion':'Descripcion',
        }


        widgets={
            'latitudubicacion': forms.TextInput(attrs={'class':'form-control'}),
            'longitudubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcionubicacion': forms.TextInput(attrs={'class': 'form-control'}),
        }


    """
    latitudubicacion = form.CharField(max_length= 30,label='Latitud',widget = form.TextInput(attrs={
        'class': 'form-group',
        'class': 'col-xs-12',
        'class': 'form-control input-lg',
        'type': 'text',
        'placeholder': 'Ingresa la Latitud'}))
    longitudubicacion = form.CharField( max_length= 30,label='Longitud', widget= form.TextInput(attrs={
        'class': 'form-group',
        'class': 'col-xs-12',
        'class': 'form-control input-lg',
        'type':'text',
        'placeholder': 'Ingresa la Longitud'}))
    descripcionubicacion = form.CharField(max_length=60,label='Descripcion Ubicacion',widget = form.TextInput(attrs={
        'class': 'form-group',
        'class': 'col-xs-12',
        'class': 'form-control input-lg',
        'type': 'text',
        'placeholder': 'Ingresa la Descripcion Ubicacion'}))
    class Meta:
        model = Ubicacion
        fields = '__all__'
        
        
"""
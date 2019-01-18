from django import forms
from django.contrib.auth.models import User


"""
Constantes
"""
ERROR_MESSAGE_USER = {'required':'El usuario es requerido','unique':'El usuario ya se encuentra registrado','invalid': 'Ingrese el usuario valido'}
ERROR_MESSAGE_PASSWORD = {'required':'El password es requerido'}
ERROR_MESSAGE_EMAIL = {'required':'el email es requerido','invalid':'Ingrese un correo valido'}


"""
Funcion
"""

def must_be_gt(value_password):
    if len(value_password) < 2:
        raise forms.ValidationError('El Password debe tener mas de 5 Caracter')


"""
Clases 
"""
#Login
class LoginUserForm(forms.Form):
    username = forms.CharField(max_length= 20,label='Usuario',widget = forms.TextInput(attrs={
        'class': 'form-group',
        'class': 'col-xs-12',
        'class': 'form-control input-lg',
        'type': 'text',
        'placeholder': 'Ingresa el Usuario',
        'autocomplete': 'off'}))
    password = forms.CharField( max_length= 20,label='Contraseña', widget= forms.PasswordInput(attrs={
        'class': 'form-group',
        'class': 'col-xs-12',
        'class': 'form-control input-lg',
        'type':'password',
        'placeholder': 'Ingresa la Contraseña',
        'autocomplete':'off'}))

#Usuario
class EditUserForm(forms.ModelForm):
    username = forms.CharField(max_length=20,label='Usuario',widget=forms.TextInput(
        attrs={'class': 'form-control',}),error_messages=ERROR_MESSAGE_USER)

    email = forms.EmailField(label='Correo Electronico',
                            help_text='Ingresa Email',widget=forms.TextInput(attrs={
                'class': 'form-control',}),error_messages=ERROR_MESSAGE_EMAIL)

    first_name = forms.CharField(label='Nombre',max_length=50,
                                 help_text='Ingresa Nombre',widget=forms.TextInput(attrs={'class': 'form-control',}))

    last_name = forms.CharField(label='Apellidos', max_length=100,widget=forms.TextInput(attrs={
            'class': 'form-control',}),help_text='Ingresa Apellido',)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

#Usuario Password
class EditPasswordForm(forms.Form):
    password = forms.CharField( max_length= 20,label='Contraseña Actual', widget= forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Ingresa la Contraseña'
        }) )
    new_password = forms.CharField(max_length=20,label='Nueva Contraseña', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Ingresa la Contraseña'
        }),validators = [must_be_gt] )
    repeat_password = forms.CharField( max_length= 20,label='Confirmar Nueva Contraseña', widget= forms.PasswordInput(attrs={
        'class': 'form-control',
        'type':'password',
        'placeholder': 'Ingresa la Contraseña'
        }),validators = [must_be_gt]  )

    def clean(self):
        clean_data = super(EditPasswordForm,self).clean()
        password1 = clean_data['new_password']
        password2 = clean_data['repeat_password']
        if password1 != password2:
            raise forms.ValidationError('Los Password son distintos')
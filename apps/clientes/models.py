from django.db import models
from apps.cooperativa.models import Cooperativa
from apps.cooperativa.models import Instituciones
from apps.cooperativa.models import Planservicios
from apps.geolocalizacion.models import Ubicacion
from django.core.validators import RegexValidator

"""
#Informacion
Persona()
Cliente(Persona,Instituciones)
Distrito()
Barrio(Distrito)
Direccion(Ubicacion,Barrio)
///////Contrato(Cliente,Planservicios,Direccion)
"""

"""
Constantes
"""
SEXOS = (('M', 'Masculino'),('F', 'Femenino'))

class TimeStampModel(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    class Meta:
        abstract = True
#TimeStampModel    title=True, |titlecase

class Persona(TimeStampModel):
    nombrepersona = models.CharField(max_length=100, blank=False, null=True,
                                     verbose_name='Nombre',
                                     help_text='Ingrese su Nombre')
    paternopersona = models.CharField(max_length=100, blank=True, null=True,
                                      verbose_name='Apellido Paterno',
                                      help_text = 'Ingrese su Apellido Paterno')
    maternopersona = models.CharField(max_length=100, blank=True, null=True,
                                      verbose_name='Apellido Materno',
                                      help_text='Ingrese su Apellido Materno')
    cipersona = models.CharField(max_length=20, blank=False, null=True,unique=True,#cambiar esta obligatorio numero carnet cliente
                                 verbose_name='Cedula de Identidad',
                                 help_text = 'Ingrese su Numero de Cedula de Identidad')
    generopersona=models.CharField(max_length=1,choices=SEXOS,default='M',
                                 verbose_name='Genero',
                                 help_text = 'Ingrese Genero')
    nacimientopersona = models.DateField(blank=True,null=True,
                                         verbose_name = 'Fecha de nacimiento',
                                         help_text = 'Seleccione su fecha de nacimiento')
    #usuariopersona = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s' % (self.cipersona,self.nombrepersona,self.paternopersona,self.maternopersona)

class Cliente(TimeStampModel):
    Personas_Clientes = models.ManyToManyField(Persona)
    Instituciones = models.ForeignKey(Instituciones,null=True,blank=True,on_delete=models.CASCADE)


    celularcliente = models.CharField(max_length=15, blank=True, null=True,
                                              verbose_name = 'Numero de Celular',
                                              help_text = 'Ingrese el Numero de Celular')
    emailcliente = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Email',
                                              help_text = 'Ingrese el Email')
    observacioncliente = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Observaciones',
                                              help_text = 'Ingrese Observaciones')
    #estadocliente = models.BooleanField(default=True)
    #usuariocliente = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.emailcliente,self.Instituciones)

class Distrito(TimeStampModel):
    numerodistrito = models.IntegerField(blank=True, null=True,
                                              verbose_name = 'Numero del Distrito',
                                              help_text = 'Ingrese el Numero del Distrito')
    nombredistrito = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Nombre Distrito',
                                              help_text = 'Ingrese del Nombre Distrito')
    sigladistrito = models.CharField(max_length=10, blank=True, null=True,default='Sin/Sigla',
                                              verbose_name = 'Sigla del Distrito',
                                              help_text = 'Ingrese la Sigla del Distrito')
    detalledistrito = models.CharField(max_length=255, blank=True, null=True,
                                              verbose_name = 'Detalle del Distrito',
                                              help_text = 'Ingrese Detalle del Distrito')

    def __str__(self):
        return '%s %s %s' % (self.numerodistrito,self.nombredistrito,self.sigladistrito)

class Barrio(TimeStampModel):
    Distrito = models.ForeignKey(Distrito,null=True,blank=True,on_delete=models.CASCADE)
    nombrebarrio = models.CharField(max_length=50, blank=True, null=True,unique=True,
                                              verbose_name = 'Nombre del Barrio',
                                              help_text = 'Ingrese Nombre del Barrio')
    siglabarrio = models.CharField(max_length=20, blank=True, null=True,
                                              verbose_name = 'Sigla del Barrio',
                                              help_text = 'Ingrese Sigla del Barrio')
    detallebarrio = models.CharField(max_length=255, blank=True, null=True,
                                              verbose_name = 'Detalle del Barrio',
                                              help_text = 'Ingrese Detalle del Barrio')

    def __str__(self):
        return '%s %s' % (self.Distrito,self.nombrebarrio)

class Direccion(TimeStampModel):
    Ubicacion = models.ForeignKey(Ubicacion,null=True,blank=True,on_delete=models.CASCADE)
    Barrio = models.ForeignKey(Barrio,null=False,blank=False,on_delete=models.CASCADE)
    zonadireccion = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Zona',
                                              help_text = 'Ingrese Nombre de la Zona')
    referenciadireccion = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Referencia',
                                              help_text = 'Ingrese Referencia')
    viadireccion = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Nombre de la Via',
                                              help_text = 'Ingrese Nombre de la Via')
    calledireccion = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Nombre de la Calle',
                                              help_text = 'Ingrese Nombre de la Calle')
    numerocasadireccion = models.CharField(max_length=20, blank=True, null=True,
                                              verbose_name = 'Numero de Casa',
                                              help_text = 'Ingrese Numero de Casa')
    avenidadireccion = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Nombre de la Avenida',
                                              help_text = 'Ingrese Nombre de la Avenida')

    def __str__(self):
        return '%s %s %s' % (self.Barrio,self.avenidadireccion,self.numerocasadireccion)

from django.db import models
from django.core.validators import RegexValidator

"""
#Informacion
Departamentos()
Provincias(Departamentos)
Municipios(Provincias)
Instituciones()
Cooperativa(Instituciones,Municipios)
Servicios(Cooperativa)
Precioservicios()
Planservicios(Precioservicios,Servicios)
Direcciones()
Unidades(Direcciones)
Subunidades(Unidades)/Muchos A Muchos
"""


class TimeStampModel(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    class Meta:
        abstract = True
#TimeStampModel

class Departamentos(TimeStampModel):
    nombredepartamentos = models.CharField(max_length=50, blank=True, null=True,unique=True,
                                     verbose_name='Departamento',
                                     help_text='Ingrese su Nombre de Departamento')
    sigladepartamentos = models.CharField(max_length=15, blank=True, null=True,
                                     verbose_name='Sigla del Departamento',
                                     help_text='Ingrese la Sigla de Departamento')
    def __str__(self):
        return '%s %s' % (self.nombredepartamentos, self.sigladepartamentos)

class Provincias(TimeStampModel):
    Departamentos = models.ForeignKey(Departamentos, null=True, blank=True, on_delete=models.CASCADE)
    nombreprovincias = models.CharField(max_length=50, blank=True, null=True,unique=True,
                                     verbose_name='Provinvia',
                                     help_text='Ingrese su Nombre Provinvia')
    siglaprovincias = models.CharField(max_length=15, blank=True, null=True,
                                     verbose_name='Sigla Provinvia',
                                     help_text='Ingrese la Sigla Provinvia')
    def __str__(self):
        return '%s %s' % (self.Departamentos.nombredepartamentos,self.nombreprovincias)

class Municipios(TimeStampModel):
    Provincias = models.ForeignKey(Provincias, null=True, blank=True, on_delete=models.CASCADE)
    nombremunicipios = models.CharField(max_length=50, blank=True, null=True,
                                     verbose_name='Ciudad',
                                     help_text='Ingrese su Nombre Ciudad')
    siglamunicipios  = models.CharField(max_length=15, blank=True, null=True,
                                     verbose_name='Sigla Ciudad',
                                     help_text='Ingrese la Sigla Ciudad')
    def __str__(self):
        return '%s %s' % (self.Provincias, self.nombremunicipios)

class Instituciones(TimeStampModel):
    nombreinstituciones = models.CharField(max_length=50, blank=False, null=True,
                                     verbose_name='Nombre Institucion',
                                     help_text='Ingrese su Nombre Institucion')
    siglainstituciones = models.CharField(max_length=15, blank=True, null=True,
                                     verbose_name='Sigla Institucion',
                                     help_text='Ingrese la Sigla Institucion')
    nitinstituciones = models.CharField(max_length=20, blank=False, null=False, unique=True,
                                 verbose_name='Nit de Institucion',
                                 help_text='Ingrese el Nit o Número de Identifican Tributaria')
    def __str__(self):
        return '%s %s' % (self.nombreinstituciones,self.nitinstituciones)

class Cooperativa(TimeStampModel):
    Instituciones = models.ForeignKey(Instituciones, null=True, blank=True, on_delete=models.CASCADE)
    Municipios = models.ForeignKey(Municipios,null=True,blank=True,on_delete=models.CASCADE)
    misioncooperativa = models.CharField(max_length=255, blank=True, null=False,
                                 verbose_name='Mision de la Cooperativa',
                                 help_text='Ingrese la Mision de la Cooperativa')
    visioncooperativa = models.CharField(max_length=255, blank=True, null=False,
                                 verbose_name='Vision de la Cooperativa',
                                 help_text='Ingrese la Vision de la Cooperativa')
    logocooperativa = models.ImageField(upload_to='static/photos/', null=True, blank=True)#faltacorregir

    def __str__(self):
        return (self.Instituciones.nombreinstituciones)
"""
        return '%s %s %s' % (self.Instituciones,self.misioncooperativa,self.visioncooperativa)
"""

class Servicios(TimeStampModel):
    Cooperativa = models.ForeignKey(Cooperativa, null=False, blank=False, on_delete=models.CASCADE)
    nombreservicios = models.CharField(max_length=50, blank=False, null=False,validators=[
        RegexValidator(regex='^[[0-9a-zA-Z]||[ñÑ]]*$',message='Este campo solo debe contener caracteres alfanúmericos')],
                                            verbose_name='Nombre del Servicio',
                                            help_text='Ingrese Nombre del Servicio Servicio')
    siglaservicios = models.CharField(max_length=20, blank=False, null=False,
                                            verbose_name='Sigla del Servicio',
                                            help_text='Ingrese la Sigla del Servicio')
    descripcionservicios = models.CharField(max_length=50, blank=True, null=True,
                                            verbose_name='Descripcion del Servicio',
                                            help_text='Ingrese Descripcion del Servicio')
    #estadoservicios = models.BooleanField(default=True)

    def __str__(self):
        return self.nombreservicios

class Precioservicios(TimeStampModel):
    costoprecioservicios = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True,default=0.00,
                                              verbose_name = 'Valor',
                                              help_text = 'Ingrese su Valor')
    MONEDA = (('BS', 'Bolivianos')), \
             (('R$', 'Reales')), \
             (('USD', 'Dolares'))
    monedaprecioservicios = models.CharField(max_length=5,
                                            verbose_name='Moneda',
                                            help_text='Ingrese Tipo Moneda',
                                            choices = MONEDA, default = 'BS')
    estadoprecioservicios = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.costoprecioservicios,self.monedaprecioservicios)

class Planservicios(TimeStampModel):
    Precioservicios = models.ForeignKey(Precioservicios,null=False,blank=False,on_delete=models.CASCADE)
    Servicios = models.ForeignKey(Servicios,null=False,blank=False,on_delete=models.CASCADE)
    nombreplanservicios = models.CharField(max_length=50,
                                            verbose_name='Nombre del Servicio',
                                            help_text='Ingrese Nombre del Servicio')
    detalleplanservicios = models.CharField(max_length=255,blank=True, null=True,
                                            verbose_name='Detalle del Plan Servicio',
                                            help_text='Ingrese Detalle del Plan Servicio')
    #estadoplanservicios = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s %s' % (self.nombreplanservicios, self.Servicios, self.Precioservicios)

class Direcciones(TimeStampModel):
    nombredirecciones = models.CharField(max_length=50, blank=False, null=False,
                                     verbose_name='Nombre de la Direcciones',
                                     help_text='Ingrese Nombre de la Direcciones')
    sigladirecciones = models.CharField(max_length=15, blank=True, null=True,
                                     verbose_name='Sigla de la Direcciones',
                                     help_text='Ingrese la Sigla de la Direcciones')
    descripciondirecciones = models.CharField(max_length=255, blank=True, null=True,
                                 verbose_name='Descripcion de la Direcciones',
                                 help_text='Ingrese la Descripcion de la Direcciones')
    #estadodirecciones = models.BooleanField(default=True)

    def __str__(self):
        return (self.nombredirecciones)

class Subunidades(TimeStampModel):

    nombresubunidades = models.CharField(max_length=50, blank=True, null=True,
                                             verbose_name='Nombre de la Subunidad',
                                             help_text='Ingrese Nombre de la Subunidad')
    siglasubunidades = models.CharField(max_length=15, blank=True, null=True,
                                            verbose_name='Sigla de la Subunidad',
                                            help_text='Ingrese la Subunidad')
    descripcionsubunidades = models.CharField(max_length=255, blank=True, null=True,
                                           verbose_name='Descripcion de la Subunidad',
                                           help_text='Ingrese la Descripcion de la Subunidad')
    #estadosubunidades = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.nombresubunidades, self.siglasubunidades)

class Unidades(TimeStampModel):
    Direcciones = models.ForeignKey(Direcciones, null=False, blank=False, on_delete=models.CASCADE)
    Unidades_Subunidades = models.ManyToManyField(Subunidades)
    nombreunidades = models.CharField(max_length=50, blank=True, null=True,
                                      verbose_name='Nombre de la Unidad',
                                      help_text='Ingrese Nombre de la Unidad')
    siglaunidades = models.CharField(max_length=15, blank=True, null=True,
                                     verbose_name='Sigla de la Unidades',
                                     help_text='Ingrese la Unidad')
    descripcionunidades = models.CharField(max_length=255, blank=True, null=True,
                                           verbose_name='Descripcion de la Unidad',
                                           help_text='Ingrese la Descripcion de la Unidad')


    #estadounidades = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.nombreunidades, self.siglaunidades)

from django.db import models
from django.forms import ModelForm
"""
#Informacion
Ubicacion()
"""

class TimeStampModel(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    class Meta:
        abstract = True
#TimeStampModel

class Ubicacion(TimeStampModel):
    latitudubicacion = models.CharField(max_length=30, blank=True, null=True,
                                              verbose_name = 'Latitud',
                                              help_text = 'Ingrese la Latitud')
    longitudubicacion = models.CharField(max_length=30, blank=True, null=True,
                                              verbose_name = 'Longitud',
                                              help_text = 'Ingrese la Longitud')
    descripcionubicacion = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Descripcion de la Ubicacion',
                                              help_text = 'Ingrese Descripcion de la Ubicacion')
    def __str__(self):
        return '%s %s' % (self.latitudubicacion,self.longitudubicacion)


"""
class UbicacionForm(ModelForm):
    class Meta:
        model = Ubicacion
        fields = '__all__'
"""
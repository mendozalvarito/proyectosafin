from django.db import models
from apps.clientes.models import Cliente
from apps.clientes.models import Planservicios
from apps.clientes.models import Direccion

"""
#Informacion
Contrato(Cliente,Planservicios,Direccion)
"""

class TimeStampModel(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    class Meta:
        abstract = True
#TimeStampModel

class Contrato(TimeStampModel):
    Cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    Planservicios = models.ForeignKey(Planservicios, null=True, blank=True, on_delete=models.CASCADE)
    Direccion = models.ForeignKey(Direccion, null=True, blank=True, on_delete=models.CASCADE)
    referenciacontrato = models.CharField(max_length=50,null=True,blank=True,
                                              verbose_name = 'Referencia Contrato',
                                              help_text = 'Ingrese Referencia del Contrato')
    def __str__(self):
        return '%s %s %s' % (self.Cliente.celularcliente,self.Planservicios.nombreplanservicios,self.Direccion.referenciadireccion)
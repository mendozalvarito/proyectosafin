from __future__ import unicode_literals
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.utils.timesince import timesince
from django.views.generic import ListView, TemplateView

from .forms import *
import json


# Create your view here.
API_KEY_GOOGLE_MAPS = getattr(settings, "API_KEY_GOOGLE_MAPS", None)



def index(request):
    form = UbicacionForm()
    ubicaciones = Ubicacion.objects.all()
    context = {
        'form': form,'ubicaciones': ubicaciones}
    return render_to_response('geolocalizacion/index.html',context,RequestContext(request))

def ubicacion_guardar(request):
    if request.is_ajax():
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            data = getHTML()
            return HttpResponse(json.dumps({'ok': True, 'msg': data}))
        else:
            return HttpResponse(json.dumps({'ok': False, 'msg': 'Debes llenar todos los campos'}))


#metodo para obtener el html que lista los objetos
def getHTML():
    ubicaciones = Ubicacion.objects.all().order_by('created')

    data = '<select id="cars" name="cars" size="10">'
    for ubicacion in ubicaciones:
        data += '<option value="%s">%s %s - hace %s</option>' % (
        ubicacion.id, ubicacion.latitudubicacion, ubicacion.longitudubicacion, timesince(ubicacion.created))
    data += '</select>' \
            '<button type="button" id="deleteUbicacion">Eliminar</button>'
    return data


def ubicacion_obtener(request):
    pass
def ubicacion_eliminar(request):
    pass
def ubicacion_buscar(request):
    pass








class ListaUbicacion(ListView):
    context_object_name = 'ubicaciones'
    model = Ubicacion
    template_name = 'geolocalizacion/listar_ubicacion.html'











"""
    if request.is_ajax():
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            data = getHTML()
            return HttpResponse(json.dumps({'ok': True, 'msg': data}))
        else:
            return HttpResponse(json.dumps({'ok': False, 'msg': 'Debes llenar todos los campos'}))
"""


#form_ubicacion
"""
class UbicacionView(View):
    model = Ubicacion
    form = UbicacionForm()
    #template = 'geolocalizacion/index1.html'
    #template_name = 'geolocalizacion/index1.html'
    #form_class = UbicacionForm
    success_message = "Tu Ubicacion ha sido guardado"
    #success_url = reverse_lazy('usuarios:editar_usuario')


def index(request):
    form = UbicacionForm()
    ubicaciones = Ubicacion.objects.all().order_by('fecha')
    return render_to_response('index1.html', {'form':form,'ubicaciones':ubicaciones}, RequestContext(request))

def coords_obtener(request):
    ubicacion = Ubicacion.objects.get(id=request.POST['value'])
    return HttpResponse(json.dumps({'lat': ubicacion.lat, 'lng':ubicacion.lng}))
"""

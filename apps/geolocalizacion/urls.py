from django.urls import include,path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.http import HttpResponse

app_name = 'geolocalizacion'

urlpatterns = [
    path('ubicacion/',views.index,name='index'),

    path('guardar/', views.ubicacion_guardar, name='ubicacionguardar'),

    path('ubicacionobtener/', views.ubicacion_obtener, name='ubicacionobtener'),
    path('ubicacioneliminar/', views.ubicacion_eliminar, name='ubicacioneliminar'),
    path('ubicacionbuscar/', views.ubicacion_buscar, name='ubicacionbuscar'),

    path('listarubicacion/', views.ListaUbicacion.as_view(), name='listarubicacion'),

    #   url(r'^mapa/$', view.index, name='index'),
#    url(r'^coords/save$', view.coords_save, name='coords_save'),
#    url(r'^coords/obtener$', view.coords_obtener, name='coords_obtener'),
#    url(r'^coords/eliminar$', view.coords_eliminar, name='coords_eliminar'),
#    url(r'^coords/buscar/$', view.coords_buscar, name='coords_buscar'),

]

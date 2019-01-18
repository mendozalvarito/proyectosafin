from django.urls import path,re_path
from . import views
from .views import CreatePersonaView,ListarPersonaView,ActualizarPersonaView,DetallePersonaView,EliminarPersonaView

from apps.clientes.view.views_cliente import ListaClienteView

app_name = 'clientes'

urlpatterns = [
    path('listarpersona/', views.ListarPersonaView, name='listarpersona'),

    path('createpersona/', CreatePersonaView, name='createpersona'),

    re_path(r'^detallepersona/(?P<cipersona_url>\w+)/$', views.DetallePersonaView.as_view(), name='detallepersona'),
    path('persona/<int:id>/actualizar',views.ActualizarPersonaView, name='actualizarpersona'),
    path('persona/<int:id>/eliminar',EliminarPersonaView, name='eliminarpersona'),










    path('listarcliente/', ListaClienteView, name='listarcliente'),

]





#path('createpersona/',view.PersonaView.as_view(), name='CreatePersona'),
"""
    path('detallepersona/<cipersona_url>/',view.DetallePersonaView.as_view(), name='DetallePersona'),
    re_path(r'^info/(?P<username_url>\w+)/$', view.InfoView.as_view(), name='info'),
    path('editar/', name='editar_usuario'),
    path('editar_password/', name='editar_password'),
    path('', list_products, name='list_products'),
    path('new', create_product, name='create_products'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
"""

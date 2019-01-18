from django.urls import path
from django.urls import include, re_path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'usuarios'
urlpatterns = [

    #  path('index/', view.LoginView.as_view(), name='index'),
    path('', views.LoginView.as_view(), name='index'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    path('editar/', views.EditarUsuarioView.as_view(), name='editar_usuario'),
    path('editar_password/', views.EditarPassword, name='editar_password'),

    re_path(r'^informacion/(?P<username_url>\w+)/$', views.InfoView.as_view(), name='informacion'),



#info ayuda
    path('menu/', views.manual, name='menu'),
]

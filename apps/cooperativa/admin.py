from django.contrib import admin
from .models import Cooperativa
from .models import Direcciones
from .models import Unidades
from .models import Subunidades
from .models import Instituciones
from .models import Precioservicios
from .models import Servicios
from .models import Planservicios
from .models import Departamentos
from .models import Provincias
from .models import Municipios
# Register your models here.

class SubunidadesUnidadesInlines(admin.TabularInline):
    model = Unidades.Unidades_Subunidades.through

class SubunidadesAdmin(admin.ModelAdmin):
    inlines = [
        SubunidadesUnidadesInlines,
    ]
class UnidadesAdmin(admin.ModelAdmin):
    inlines = [
        SubunidadesUnidadesInlines,
    ]
    exclude = ('Unidades_Subunidades',)

admin.site.register(Instituciones)
admin.site.register(Precioservicios)
admin.site.register(Servicios)
admin.site.register(Planservicios)
admin.site.register(Cooperativa)
admin.site.register(Departamentos)
admin.site.register(Provincias)
admin.site.register(Municipios)
admin.site.register(Direcciones)
#admin.site.register(Subunidades, SubunidadesAdmin)
admin.site.register(Subunidades)
admin.site.register(Unidades, UnidadesAdmin)

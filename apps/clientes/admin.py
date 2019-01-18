from django.contrib import admin
from .models import Persona
from .models import Cliente
from .models import Distrito
from .models import Barrio
from .models import Direccion


# Register your models here.
class PersonaClienteInlines(admin.TabularInline):
    model = Cliente.Personas_Clientes.through

class PersonaAdmin(admin.ModelAdmin):
    inlines = [
        PersonaClienteInlines,
    ]
class ClienteAdmin(admin.ModelAdmin):
    inlines = [
        PersonaClienteInlines,
    ]
    exclude = ('Personas_Clientes',)

#admin.site.register(Persona,PersonaAdmin)
admin.site.register(Persona)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Distrito)
admin.site.register(Barrio)
admin.site.register(Direccion)


class PersonaAdmin(admin.ModelAdmin):
	list_display = ('nombrepersona', 'paternopersona','maternopersona', 'cipersona', 'generopersona'  )
	search_fields = ('cipersona', 'paternopersona')
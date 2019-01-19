from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
from .forms import PersonaForm
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, ListView, DetailView
from django.views.generic.edit import FormView



class DetallePersonaView(DetailView):
	model = Persona
	template_name = 'clientes/persona/detalle_persona.html'



def ListarPersonaView(request):
    personas = Persona.objects.all()
    return render(request,'clientes/persona/listar_persona.html',{'personas':personas})

def book_create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
    else:
        form = PersonaForm()
    return save_book_form(request, form, 'books/includes/partial_book_create.html')

def CreatePersonaView(request):
    form = PersonaForm(request.POST or None)
    #print(Persona.nacimientopersona)
    if form.is_valid():
        form.save()
        return redirect('clientes:listarpersona')
    return render(request, 'clientes/persona/agregar_persona.html', {'form': form})


def add_blog(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
    else:
        form = PersonaForm()
    return render(request, 'blog/blog_form.html', {'form': form})


def ActualizarPersonaView(request, id):
    personas = Persona.objects.get(id=id)
    form = PersonaForm(request.POST or None, instance=personas)
    if form.is_valid():
        form.save()
        return redirect('clientes:ListaPersona')
    return render(request, 'clientes/persona/actualizar_persona.html',{'form':form,'personas':personas})

def ActualizarPersonaView1(request, id):
    personas = get_object_or_404(Persona, id=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=personas)
    else:
        form = PersonaForm(instance=personas)
    return save_book_form(request, form, 'clientes/persona/includes/persona_actualizar.html')

    #return render(request, 'clientes/persona/includes/persona_actualizar.html', {'form': form, 'personas': personas})
    #return save_book_form(request, form, 'books/includes/partial_book_update.html')







def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            personas = Persona.objects.all()
            data['html_persona_lista'] = render_to_string('clientes/persona/includes/persona_listar.html', {
                'personas': personas
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


#html_persona_lista
#html_form










def EliminarPersonaView1(request, id):
    personas = Persona.objects.get(id=id)
    if request.method =='POST':
        personas.delete()
        return redirect('clientes:ListaPersona')
    return render(request,'clientes/persona/eliminar_persona.html',{'personas':personas})

def EliminarPersonaView(request, id):
    persona = get_object_or_404(Persona, id=id)
    data = dict()
    if request.method == 'POST':
        persona.delete()
        data['form_is_valid'] = True
        personas = Persona.objects.all()
        data['html_persona_lista'] = render_to_string('clientes/persona/includes/persona_listar.html', {
            'personas': personas
        })
    else:
        context = {'persona': persona}
        data['html_form'] = render_to_string('clientes/persona/includes/persona_eliminar.html', context, request=request)
    return JsonResponse(data)






"""
class DetallePersonaView(DetailView):
    model = Persona
    template_name = 'clientes/persona/persona_detalle.html'
    slug_field = 'cipersona'#que campo de la base de datos
    slug_url_kwarg = 'cipersona_url'#que campo de la url
    """
"""
class CreatePersonaView(CreateView):
	form_class = PersonaForm
	template_name = 'clientes/persona/persona_agregar.html'
	model = Persona
	success_url = '/listar_persona/'

class ListaPersonaView(ListView):
	context_object_name = 'personas'
	model = Persona
	template_name = 'clientes/persona/persona_listar.html'

class DetallePersonaView(DetailView):
	model = Persona
	template_name = 'clientes/persona/persona_detalle.html'

class EliminarPersonaView(DeleteView):
	model = Persona
	template_name = 'clientes/persona/persona_eliminar.html'
	success_url = '/listar_persona/'

class ActualizarPersonaView(UpdateView):
	form_class = PersonaForm
	template_name = 'clientes/persona/persona_agregar.html'
	model = Persona
	success_url = '/listar_persona/'

class PersonaView(FormView):
	template_name = 'clientes/persona/persona_agregar.html'
	form_class = PersonaForm
	success_url = '/listar_persona/'
"""
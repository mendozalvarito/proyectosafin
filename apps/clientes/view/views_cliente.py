from django.shortcuts import render, redirect, get_object_or_404
from apps.clientes.models import Cliente
from apps.clientes.form.forms_cliente import ClienteForm
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, ListView, DetailView
from django.views.generic.edit import FormView

def ListaClienteView(request):
    clientes = Cliente.objects.all()
    return render(request,'clientes/cliente/listar_cliente.html',{'clientes':clientes})




def CreatePersonaView(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes:listapersona')
    return render(request, 'clientes/cliente/', {'form': form})
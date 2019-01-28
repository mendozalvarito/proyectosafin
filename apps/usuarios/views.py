from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from .forms import LoginUserForm, EditUserForm, EditPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.detail import DetailView
from django.views.generic import View
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth import update_session_auth_hash
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
"""
Clases 
"""
#Login
#ip ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')

def manual(request):
    return render(request, template_name='')


class LoginView(View):
    form = LoginUserForm()
    message = None
    template = 'usuarios/index.html'#url

    def get(self, request, *args,  **kwargs):
        if request.user.is_authenticated:  # tomar en cuenta
            return redirect('usuarios:dashboard')
        return render(request, self.template, self.get_context())

    def post(self, request, *args, **kwargs):
        username_post = request.POST['username']
        password_post = request.POST['password']
        user = authenticate(username=username_post, password=password_post)
        #print(user)
        if user is not None:
            login_django(request, user)
            return redirect('usuarios:dashboard')
        else:
            self.message = "Usuario o la Contraseña son Incorrectos"
            return render(request, self.template, self.get_context())

    def get_context(self):
        return {'form': self.form, 'message' : self.message}



#Dashboard
class DashboardView(LoginRequiredMixin, View):
    login_url = 'usuarios:index'
    def get(self, request, *args, **kwargs):
        return render(request, 'usuarios/includes/dashboard.html', {})#url

#Informacion

class InfoView(LoginRequiredMixin, DetailView):
    login_url = 'usuarios:index'
    model = User
    template_name = 'usuarios/includes/informacion_usuario.html'#url
    slug_field = 'username'#que campo de la base de datos
    slug_url_kwarg = 'username_url'#que campo de la url


#Editar Usuario
class EditarUsuarioView(LoginRequiredMixin,UpdateView,SuccessMessageMixin):
    login_url = 'usuarios:index'
    model = User
    template_name = 'usuarios/includes/editarusuario_usuario.html'#url
    success_url = reverse_lazy('usuarios:editar_usuario')
#    success_url = reverse_lazy('usuarios:info')
    form_class = EditUserForm
    success_message = "Tu usuario ha sido actualizado"

    def form_valid(self, request,*args,**kwargs):
        messages.success(self.request,self.success_message)
        return super(EditarUsuarioView,self).form_valid(request,*args,**kwargs)

    def get_object(self, queryset = None):
        return self.request.user


"""
Funciones
"""

#Editar Password
@login_required(login_url='usuarios:index')
def EditarPassword(request):
    #message = None

    form = EditPasswordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            current_password = form.cleaned_data['password']
            new_password = form.cleaned_data['new_password']

            if authenticate(username = request.user.username,password = current_password):
                request.user.set_password(new_password)
                request.user.save()

                update_session_auth_hash(request, request.user)
                #message = 'Password Actualizado'
                messages.success(request, 'Password actualizado, messages')
            else:
                messages.error(request, 'No es posible actualizar el Password, messages')
    context = {'form': form}
    return render(request, 'usuarios/includes/editarpassword_usuario.html', context)#url


#Logout
@login_required(login_url='usuarios:index')
def logout(request):
    logout_django(request)
    return redirect('usuarios:index')

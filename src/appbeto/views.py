from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_not_required 
from django.views.generic import CreateView, UpdateView
from . import forms, models

# Create your views here.

@login_not_required
def inicio(solicitud):
	return render(solicitud, 'appbeto/index.html')

@login_not_required
def about(solicitud):
	return render(solicitud, 'appbeto/about.html')

class LoginVista(LoginView):
	authentication_form = forms.LoginForm
	template_name = 'appbeto/login.html'
	next_page = reverse_lazy('appbeto:inicio')
	
	def form_valid(self, form: forms.LoginForm):
		usuario = form.get_user()
		messages.success(
			self.request, f'Inicio de Sesión Exitoso, Bienvenido {usuario.username}'
		)
		return super().form_valid(form)

@method_decorator(login_not_required, name= 'dispatch')
class Registrarme(CreateView):
	form_class = forms.CrearUsuarioForm
	template_name = 'appbeto/registro.html'
	success_url = reverse_lazy('appbeto:login')
	
	def form_valid(self, form: forms.LoginForm):
		messages.success(
			self.request, f'Registro de Usuario Exitoso, Puedes Iniciar Sesión'
		)
		return super().form_valid(form)

class Actualizar(UpdateView):
	model = User
	form_class = forms.ActualizaUserForm
	template_name = 'appbeto/actualizar.html'
	success_url = reverse_lazy('appbeto:inicio')

	def get_object(self):
		#regresa el usuario actual
		return self.request.user

	def form_valid(self, form: forms.LoginForm):
		messages.success(
			self.request, f'Actualización de Datos Exitosa'
		)
		return super().form_valid(form)


def familiar_list(request):
	indice = models.Familiar.objects.all()
	return render(request, 'appbeto/familiar_list.html', {'id_familiar':indice})

# creacion de registros nuevos

def familiar_form(solicitud):
	if solicitud.method == 'GET':
		form = forms.FamiliarForm()
	if solicitud.method == 'POST':
		form = forms.FamiliarForm(solicitud.POST)
		if form.is_valid():
			form.save()
			return redirect ("appbeto:familiar_listado")
	return render(solicitud, 'appbeto/familiar_form.html', {'id_form':form})

# Edicion de registros existentes

def familiar_editar(request, indice:int):
	edicion = models.Familiar.objects.get(id=indice)
	if request.method == 'GET':
		form = forms.FamiliarForm(instance=edicion)
	if request.method == 'POST':
		form = forms.FamiliarForm(request.POST, instance=edicion)
		if form.is_valid():
			form.save()
			return redirect ("appbeto:familiar_listado")
	return render(request, 'appbeto/familiar_form.html', {'id_form':form})


def familiar_borrar(request, indice:int):
	borrado = models.Familiar.objects.get(id=indice)
	borrado.delete()
	return redirect ("appbeto:familiar_listado")

def regalo_list(request):
	indice = models.Regalo.objects.all()
	return render(request, 'appbeto/regalo_list.html', {'id_regalo':indice})

def regalo_form(request):
	if request.method == 'GET':
		form = forms.RegaloForm()
	if request.method == 'POST':
		form = forms.RegaloForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect ("appbeto:regalo_listado")
	return render(request, 'appbeto/Regalo_form.html', {'id_form':form})


def menu_list(request):
	indice = models.Menu.objects.all()
	return render(request, 'appbeto/menu_list.html', {'id_menu':indice})

def menu_form(request):
	if request.method == 'GET':
		form = forms.MenuForm()
	if request.method == 'POST':
		form = forms.MenuForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect ("appbeto:menu_listado")
	return render(request, 'appbeto/menu_form.html', {'id_form':form})
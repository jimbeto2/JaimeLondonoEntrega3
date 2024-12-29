from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_not_required 
from django.views.generic import CreateView, UpdateView, ListView
from . import forms, models

# Create your views here.

# VISTA INICIAL
@login_not_required
def inicio(solicitud):
	indice = models.MisBlog.objects.all()
	return render(solicitud, 'appbeto/index.html', {'id_blog':indice})

@login_not_required
def about(solicitud):
	return render(solicitud, 'appbeto/about.html')

# GESTION DE USUARIOS
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


# GESTION DE BLOGS

# Edicion Datos y Borrado de Blog

def MisBlog_edit(solicitud, indice:int):
	edicion = models.MisBlog.objects.get(id=indice)
	if solicitud.method == 'GET':
		form = forms.MisBlog_Form(instance=edicion)
	if solicitud.method == 'POST':
		form = forms.MisBlog_Form(solicitud.POST, instance=edicion)
		if form.is_valid():
			form.save()
			return redirect ("appbeto:inicio")
	return render(solicitud, 'appbeto/misblog_edit.html', {'id_form':form})		

def MisBlog_borrar(request, indice:int):
	borrado = models.MisBlog.objects.get(id=indice)
	borrado.delete()
	return redirect ("appbeto:inicio")

# Creación de nuevos Blog
def MisBlog_crear(solicitud):
	if solicitud.method == 'GET':
		form = forms.MisBlog_Form()
	if solicitud.method == 'POST':
		form = forms.MisBlog_Form(solicitud.POST)
		if form.is_valid():
			form.save()
			return redirect ("appbeto:inicio")
	return render(solicitud, 'appbeto/misblog_form.html', {'id_form':form})



#ELIMINAR DESDE AQUI

#CREAR NUEVas entradas
def familiar_form(solicitud):
	if solicitud.method == 'GET':
		form = forms.FamiliarForm()
	if solicitud.method == 'POST':
		form = forms.FamiliarForm(solicitud.POST)
		if form.is_valid():
			form.save()
			return redirect ("appbeto:familiar_listado")
	return render(solicitud, 'appbeto/familiar_form.html', {'id_form':form})



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



def familiar_list(request):
	indice = models.Familiar.objects.all()
	return render(request, 'appbeto/familiar_list.html', {'id_familiar':indice})


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


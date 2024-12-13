from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import forms, models

# Create your views here.

def inicio(request):
	return render(request, 'appbeto/index.html')

#def positronix(request):
#	return render(request, 'appbeto/positronix.html')

def familiar_list(request):
	indice = models.Familiar.objects.all()
	return render(request, 'appbeto/familiar_list.html', {'id_familiar':indice})

def familiar_form(request):
	if request.method == 'GET':
		form = forms.FamiliarForm()
	if request.method == 'POST':
		form = forms.FamiliarForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect ("appbeto:familiar_list")
	return render(request, 'appbeto/familiar_form.html', {'id_form':form})

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
			return redirect ("appbeto:regalo_list")
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
			return redirect ("appbeto:menu_list")
	return render(request, 'appbeto/menu_form.html', {'id_form':form})
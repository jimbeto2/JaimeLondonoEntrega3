from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from . import models

class LoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']
      #todavia no estoy seguro de que estos campos se requieran

class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ActualizaUserForm(forms.ModelForm):
   class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class MisBlog_Form(forms.ModelForm):
    class Meta:
        model = models.MisBlog
        fields = "__all__"



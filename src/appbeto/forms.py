from django import forms
from django.contrib.auth.forms import AuthenticationForm
from . import models

class LoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
      #  fields = ['username', 'password']
      #todavia no estoy seguro de que estos campos se requieran

class FamiliarForm(forms.ModelForm):
    class Meta:
        model = models.Familiar
        fields = "__all__"
        #fields = ['nombre'] esta es otra opcion pero toca campo por campo

class RegaloForm(forms.ModelForm):
    class Meta:
        model = models.Regalo
        fields = "__all__"


class MenuForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = "__all__"
       



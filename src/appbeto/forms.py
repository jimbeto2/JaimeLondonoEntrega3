from django import forms
from . import models

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
       
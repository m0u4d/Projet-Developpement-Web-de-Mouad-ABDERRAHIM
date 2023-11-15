from django import forms
from .models import Equipe, Stade

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['id_equipe', 'logo', 'situation', 'adversaire', 'lieu']

    widgets = {
        'situation': forms.Select(choices=[('interieur', 'Intérieur'), ('exterieur', 'Extérieur')]),
        'adversaire': forms.TextInput(attrs={'placeholder': 'Nom de l\'équipe adversaire'}),
    }

class StadeForm(forms.ModelForm):
    class Meta:
        model = Stade
        fields = ['id_stade', 'capacite', 'occupe', 'image']  
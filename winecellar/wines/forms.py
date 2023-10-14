from django import forms
from wines.models import Vin, RegionViticole, CaveVirtuelle, Cepage


class VinForm(forms.ModelForm):
    class Meta:
        model = Vin
        exclude = ['id_cave']


class VinSearchForm(forms.Form):
    nom = forms.CharField(required=False, label='Nom du vin')
    millesime = forms.IntegerField(required=False, label='Millésime')
    couleur = forms.ChoiceField(choices=Vin.Couleur.choices, required=False, label='Couleur')


class RegionForm(forms.ModelForm):
    class Meta:
        model = RegionViticole
        fields = '__all__'


class CaveForm(forms.ModelForm):
    class Meta:
        model = CaveVirtuelle
        exclude = ['id_user']


class CepageForm(forms.ModelForm):
    class Meta:
        model = Cepage
        fields = '__all__'

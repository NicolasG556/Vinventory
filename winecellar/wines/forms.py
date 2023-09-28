from django import forms
from wines.models import Vin, RegionViticole, CaveVirtuelle, Cepage


class VinForm(forms.ModelForm):
    class Meta:
        model = Vin
        fields = '__all__'


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
        fields = '__all__'


class CepageForm(forms.ModelForm):
    class Meta:
        model = Cepage
        fields = '__all__'

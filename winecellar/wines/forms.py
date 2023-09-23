from django import forms
from wines.models import Vin, RegionViticole, CaveVirtuelle


class VinForm(forms.ModelForm):
    class Meta:
        model = Vin
        fields = '__all__'


class RegionForm(forms.ModelForm):
    class Meta:
        model = RegionViticole
        fields = '__all__'


class CaveForm(forms.ModelForm):
    class Meta:
        model = CaveVirtuelle
        fields = '__all__'

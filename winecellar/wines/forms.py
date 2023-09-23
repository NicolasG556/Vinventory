from django import forms
from wines.models import Vin


class VinForm(forms.ModelForm):
    class Meta:
        model = Vin
        fields = '__all__'

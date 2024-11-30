from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from cars.models import Car

class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'O valor minimo do carro é R$20.000,00')
        else:
            return value
        
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1985:
            self.add_error('factory_year', 'Não é possivel cadastrar carros abaixo de 1985')
        else:
            return factory_year
        
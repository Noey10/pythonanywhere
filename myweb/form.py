from django.forms import ModelForm
from django import forms

from .models import Cactus

class order(ModelForm):
    class Meta:
        model = Cactus
        fields = ['cactusName','cactusPrice', 'amout']

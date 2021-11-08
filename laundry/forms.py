from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import BLaundry, GLaundry


class BOrderForm(forms.ModelForm):
    class Meta:
        model = BLaundry
        fields = '__all__'
        exclude = ['student']


class GOrderForm(forms.ModelForm):
    class Meta:
        model = GLaundry
        fields = '__all__'
        exclude = ['student']

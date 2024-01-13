# in forms.py
from django import forms
from .models import Appoi

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appoi
        fields = ['NomClient', 'EmailC', 'TypeMar', 'dateApp', 'Comment']

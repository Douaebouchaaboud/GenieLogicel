from django import forms
from .models import Rating, RatingDjs

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        
class RatingDjsForm(forms.ModelForm):
    class Meta:
        model = RatingDjs
        fields = ['rating']

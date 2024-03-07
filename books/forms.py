from django import forms
from .models import Review

class reviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name',  'comment']
        


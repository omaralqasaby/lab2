from django import forms
from .models import category,movie

class movieForm(forms.ModelForm):
    class meta:
        model = movie
        fields = "__all__"
        
class categoryForm(forms.ModelForm):
    class meta:
        model = category
        fields = "__all__"

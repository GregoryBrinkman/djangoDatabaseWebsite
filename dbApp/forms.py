from django import forms
from .models import *

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musicians
        fields = '__all__'

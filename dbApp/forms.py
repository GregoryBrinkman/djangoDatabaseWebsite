from django import forms
from .models import *

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musicians
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = '__all__'

class SongForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = '__all__'

class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instruments
        fields = '__all__'

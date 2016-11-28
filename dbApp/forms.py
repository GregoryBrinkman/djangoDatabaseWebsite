from django import forms
from .models import *

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

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

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class PerformsForm(forms.ModelForm):
    class Meta:
        model = Performs
        fields = '__all__'

class PlaysForm(forms.ModelForm):
    class Meta:
        model = Plays
        fields = '__all__'

class AppearsOnForm(forms.ModelForm):
    class Meta:
        model = AppearsOn
        fields = '__all__'

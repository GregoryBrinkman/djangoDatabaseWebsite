from django.forms import ModelForm
from django.db import models
from .models import *

# Create your models here.
class MusiciansForm(ModelForm):
    class Meta:
        model = Musicians
        fields = '__all__'


class InstrumentsForm(ModelForm):
    class Meta:
        model = Instruments
        fields = '__all__'

class PlaysForm(ModelForm):
    class Meta:
        model = Plays
        fields = '__all__'


class AlbumsForm(ModelForm):
    class Meta:
        model = Albums
        fields = '__all__'


class SongsForm(ModelForm):
    class Meta:
        model = Songs
        fields = '__all__'
        # exclude = ['songID']

    # def __init__(self, *args, **kwargs):
    #     super(SongsForm, self).__init__(*args, **kwargs)
    #     self.fields['author'].label = 'Musician'
    #     self.fields['title'].label = 'Song Title'
    #     self.fields['albumident'].label = 'Song Album'
    #     self.fields['performs'].label = 'Performances'

class PerformsForm(ModelForm):
    class Meta:
        model = Performs
        fields = '__all__'


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

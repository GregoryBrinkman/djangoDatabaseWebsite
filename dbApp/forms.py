from django.db import models

# Create your models here.
class AddressForm(models.Model):

    #table declarations

    address       = models.CharField(max_length=100, unique=True, primary_key=True)
    phone         = models.CharField(max_length=12, unique=True)


    #function declarions

    def Meta:
        model = AddressForm
       fields = "__all__"

class MusiciansForm(models.Model):

    #table declarations

    #Ints are big enough to hold entire social security numbers. Let's do that.
    ssn           = models.IntegerField(primary_key=True, unique=True)
    name          = models.CharField(max_length=30)
    phone         = models.CharField(max_length=15)
    address       = models.ForeignKey(Address)

    #function declarions

    def Meta:
        model = Musicians
       fields = "__all__"


class InstrumentsForm(models.Model):

    #table declarations

    id            = models.IntegerField(primary_key=True, unique=True)
    name          = models.CharField(max_length=50)
    key           = models.CharField(max_length=2)


    #function declarions

    def Meta:
        model = Instruments
       fields = "__all__"




class PlaysForm(models.Model):

    #table declarations

    musician      = models.ForeignKey(Musicians)
    instrument    = models.ForeignKey(Instruments)


    #function declarions

    def Meta:
       model = Plays
       fields = "__all__"



class AlbumsForm(models.Model):

    #table declarations

    id            = models.IntegerField(primary_key=True, unique=True)
    title         = models.CharField(max_length=50)
    copyrightdate = models.DateField()
    speed         = models.IntegerField()
    producer      = models.ForeignKey(Musicians)

    #function declarions

    def Meta:
        model = Albums
       fields = "__all__"



class SongsForm(models.Model):

    #table declarations

    title         = models.CharField(primary_key=True, max_length=50)
    author        = models.CharField(max_length=50)
    album     = models.ForeignKey(Albums)

    #function declarions

    def Meta:
        model = Songs
       fields = "__all__"




class PerformsForm(models.Model):

    #table declarations

    musician      = models.ForeignKey(Musicians)
    song          = models.ForeignKey(Songs)


    #function declarions

    def Meta:
       model = Performs
       fields = "__all__"

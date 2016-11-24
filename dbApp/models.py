from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Address(models.Model):

    #table declarations

    address        = models.CharField(max_length=100, unique=True, primary_key=True)
    addressPhone   = models.CharField(max_length=12, unique=True)


    #function declarions

    def __str__(self):
        return (str(self.address) + " " + str(self.addressPhone))


class Musicians(models.Model):

    #table declarations

    #Ints are big enough to hold entire social security numbers. Let's do that.
    ssn            = models.IntegerField(primary_key=True, unique=True)
    name           = models.CharField(max_length=30)
    phone          = models.CharField(max_length=15)
    address        = models.ForeignKey(Address)

    #function declarions

    def __str__(self):
        return (str(self.name) + " " +  str(self.ssn) + " "
                + str(self.phone) + " " +  str(self.address))

    def get_absolute_url(self):
        return reverse("selected_musician", kwargs={"name":self.name})
        # return "/musicians/%s/" %(self.name)

class Instruments(models.Model):

    #table declarations

    instrumentId   = models.IntegerField(primary_key=True, unique=True)
    instrumentName = models.CharField(max_length=50)
    key            = models.CharField(max_length=2)


    #function declarions

    def __str__(self):
        return (str(self.instrumentId) + " " 
                +  str(self.instrumentName) + " " +  str(self.key))




class Plays(models.Model):

    #table declarations

    musician       = models.ForeignKey(Musicians)
    instrument     = models.ForeignKey(Instruments)


    #function declarions

    def __str__(self):
        return (str(self.musician) + " " +  str(self.instrument))




class Albums(models.Model):

    #table declarations

    albumId        = models.IntegerField(primary_key=True, unique=True)
    albumTitle     = models.CharField(max_length=50)
    copyrightdate  = models.DateField()
    speed          = models.IntegerField()
    producer       = models.ForeignKey(Musicians)

    #function declarions

    def __str__(self):
        return (str(self.albumId) + " " +  str(self.albumTitle) + " "
                +  str(self.copyrightdate) + " " +  str(self.speed)
                + " " + str(self.producer))



class Songs(models.Model):

    #table declarations

    songTitle      = models.CharField(primary_key=True, max_length=50)
    songWriter     = models.CharField(max_length=50)
    appearsOn      = models.ForeignKey(Albums)

    #function declarions

    def __str__(self):
        return (str(self.songTitle) + " " +  str(self.songWriter)
                + " " + str(self.appearsOn))




class Performs(models.Model):

    #table declarations

    musician       = models.ForeignKey(Musicians)
    song           = models.ForeignKey(Songs)


    #function declarions

    def __str__(self):
        return (str(self.musician) + " " +  str(self.song))




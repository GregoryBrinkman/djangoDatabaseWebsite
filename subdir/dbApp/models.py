from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Users(models.Model):

    #table declarations

    username = models.CharField(max_length=100, unique=True, primary_key=True, default=None)
    password = models.CharField(max_length=100, default=None)


    #function declarions

    def __str__(self):
        return (str(self.username) + " " + str(self.password))


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
    phone          = models.CharField(max_length=11)
    address        = models.ForeignKey(Address)

    #function declarions

    def __str__(self):
        return (str(self.name) + " " +  str(self.ssn) + " "
                + str(self.phone) + " " +  str(self.address))

    def get_absolute_url(self):
        return reverse("selected_musician", kwargs={"name":self.name, "id":self.ssn})

class Instruments(models.Model):

    KEYS = (
        ('Ab', 'A Flat'), ('A', 'A'), ('A#', 'A Sharp'),
        ('Bb', 'B Flat'), ('B', 'B'),
                          ('C', 'C'), ('C#', 'C Sharp'),
        ('Db', 'D Flat'), ('D', 'D'), ('D#', 'D Sharp'),
        ('Eb', 'E Flat'), ('E', 'E'),
                          ('F', 'F'), ('F#', 'F Sharp'),
        ('Gb', 'G Flat'), ('G', 'G'), ('G#', 'G Sharp'),
    )
    #table declarations

    instrumentId   = models.IntegerField(primary_key=True, unique=True)
    instrumentName = models.CharField(max_length=50)
    key            = models.CharField(max_length=2, choices=KEYS, default='Bb')


    #function declarions

    def __str__(self):
        return (str(self.instrumentId) + " " 
                +  str(self.instrumentName) + " " +  str(self.key))

    def get_absolute_url(self):
        return reverse("instrument_update", kwargs={"id":self.instrumentId})



class Plays(models.Model):

    #table declarations

    musician       = models.ForeignKey(Musicians)
    instrument     = models.ForeignKey(Instruments)


    #function declarions

    def __str__(self):
        return (str(self.musician) + " " +  str(self.instrument))




class Albums(models.Model):

    VINYL_SPEEDS = ((33, 33), (45, 45), (78, 78))
    #table declarations

    albumId        = models.IntegerField(default=0, primary_key=True, unique=True)
    albumTitle     = models.CharField(max_length=50)
    copyrightdate  = models.DateField(default=timezone.now())
    speed          = models.IntegerField(choices=VINYL_SPEEDS, default=45)
    producer       = models.ForeignKey(Musicians)

    #function declarions

    def __str__(self):
        return (str(self.albumId) + " " +  str(self.albumTitle) + " "
                +  str(self.copyrightdate) + " " +  str(self.speed)
                + " " + str(self.producer))

    def get_absolute_url(self):
        return reverse("selected_album", kwargs={"name":self.albumTitle, "id":self.albumId})


class Songs(models.Model):

    #table declarations

    songId        = models.IntegerField(default=0, primary_key=True, unique=True)
    songTitle      = models.CharField(max_length=150)
    songWriter     = models.ForeignKey(Musicians)

    #function declarions

    def __str__(self):
        return (str(self.songTitle) + " " +  str(self.songWriter))

    def get_absolute_url(self):
        return reverse("selected_song", kwargs={"name":self.songTitle, "id":self.songId})



class Performs(models.Model):

    #table declarations

    musician       = models.ForeignKey(Musicians)
    song           = models.ForeignKey(Songs)


    #function declarions

    def __str__(self):
        return (str(self.musician) + " " +  str(self.song))



class AppearsOn(models.Model):

    #table declarations

    album          = models.ForeignKey(Albums)
    song           = models.ForeignKey(Songs)

    #function declarions

    def __str__(self):
        return (str(self.album) + " " + str(self.song))

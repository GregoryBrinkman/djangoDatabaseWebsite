from django.db import models

# Create your models here.
class Address(models.Model):

    #table declarations

    address       = models.CharField(max_length=100, unique=True, primary_key=True)
    addressPhone  = models.CharField(max_length=12, unique=True)


    #function declarions

    def __str__(self):
        return (str(self.address) + " " + str(self.addressPhone))


class Musicians(models.Model):

    #table declarations

    #Ints are big enough to hold entire social security numbers. Let's do that.
    ssn           = models.IntegerField(primary_key=True, unique=True)
    name          = models.CharField(max_length=30)
    personalPhone = models.CharField(max_length=15)
    address       = models.ForeignKey(Address)

    #function declarions

    def __str__(self):
        return (str(self.name) + " " +  str(self.ssn) + " "
                + str(self.personalPhone) + " " +  str(self.address))


class Instruments(models.Model):

    #table declarations

    id            = models.IntegerField(primary_key=True, unique=True)
    name          = models.CharField(max_length=50)
    key           = models.CharField(max_length=2)


    #function declarions

    def __str__(self):
        return (str(self.id) + " " +  str(self.name)
                + " " +  str(self.key))




class Plays(models.Model):

    #table declarations

    ssn           = models.ForeignKey(Musicians)
    instrumentId  = models.ForeignKey(Instruments)


    #function declarions

    def __str__(self):
        return (str(self.ssn) + " " +  str(self.instrumentId))




class Albums(models.Model):

    #table declarations

    id            = models.IntegerField(primary_key=True, unique=True)
    title         = models.CharField(max_length=50)
    copyrightdate = models.DateField()
    speed         = models.IntegerField()
    producer      = models.ForeignKey(Musicians)

    #function declarions

    def __str__(self):
        return (str(self.id) + " " +  str(self.title) + " "
                +  str(self.copyrightdate) + " " +  str(self.speed)
                + " " + str(self.producer))



class Songs(models.Model):

    #table declarations

    title         = models.CharField(primary_key=True, max_length=50)
    author        = models.CharField(max_length=50)
    appearsOn     = models.ForeignKey(Albums)

    #function declarions

    def __str__(self):
        return (str(self.title) + " " +  str(self.author)
                + " " + str(self.appearsOn))




class Performs(models.Model):

    #table declarations

    musician      = models.ForeignKey(Musicians)
    song          = models.ForeignKey(Songs)


    #function declarions

    def __str__(self):
        return (str(self.ssn) + " " +  str(self.song))




import logging
#use logging.warning for console output

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# from django.core.urlresolvers import reverse_lazy
from django.forms import forms
from .forms import * 

#instance = model.objects.get(x=y)
#instance = get_object_or_404(model, x=y)

def UserMusicianLookup(request):
    template_name = 'user_musician_list.html'
    queryset = Musicians.objects.all()
    contextual = {
        'musician_list': queryset,
    }
    return render(request, template_name, contextual)

def UserAlbumLookup(request):
    template_name = 'user_album_list.html'
    queryset = Albums.objects.all()
    contextual = {
        'album_list': queryset,
    }
    return render(request, template_name, contextual)

def UserSongLookup(request):
    template_name = 'user_song_list.html'
    queryset = Songs.objects.all().order_by('appearson')
    contextual = {
        'song_list': queryset,
    }
    return render(request, template_name, contextual)

def UserSelectedMusician(request, name, id):
    selected_musician = Musicians.objects.get(name=name, ssn=id)
    song_list = Performs.objects.filter(musician=selected_musician)
    instrument_list = Plays.objects.filter(musician=selected_musician)
    template_name = 'user_musician.html'
    contextual = {
        'musician': selected_musician,
        'performs_list': song_list,
        'plays_list': instrument_list,
    }
    return render(request, template_name, contextual)

def UserSelectedAlbum(request, name, id):
    selected_album = Albums.objects.get(albumTitle=name, albumId=id)
    template_name = 'user_album.html'
    song_list = AppearsOn.objects.filter(album=selected_album)
    contextual = {
            'album': selected_album,
            'songs': song_list,
            }
    return render(request, template_name, contextual)

def UserSelectedSong(request, id):
    selected_song = Songs.objects.get(songId=id)
    template_name = 'user_song.html'
    song_list = AppearsOn.objects.filter(song=selected_song)
    contextual = {
        'song': selected_song,
        'appears_on': song_list,
    }
    return render(request, template_name, contextual)




#General User Search Query Views
def Search(request):
    queryset = None
    if request.POST:
        # logging.warning()
        musician = Musicians.objects.get(name__contains=request.POST['search'])
        queryset = musician
    template_name = 'index.html'
    contextual = {
        'object_list': queryset,
    }
    return render(request, template_name, contextual)


def MusicianLookup(request):
    template_name = 'musician_list.html'
    queryset = Musicians.objects.all()
    contextual = {
        'musician_list': queryset,
    }
    return render(request, template_name, contextual)

def AlbumLookup(request):
    template_name = 'album_list.html'
    queryset = Albums.objects.all()
    contextual = {
        'album_list': queryset,
    }
    return render(request, template_name, contextual)

def SongLookup(request):
    template_name = 'song_list.html'
    queryset = Songs.objects.all().order_by('appearson')
    contextual = {
        'song_list': queryset,
    }
    return render(request, template_name, contextual)

def InstrumentLookup(request):
    template_name = 'instrument_list.html'
    queryset = Instruments.objects.all()
    contextual = {
        'instrument_list': queryset,
    }
    return render(request, template_name, contextual)

def AddressLookup(request):
    template_name = 'address_list.html'
    queryset = Address.objects.all()
    contextual = {
        'address_list': queryset,
    }
    return render(request, template_name, contextual)

def PerformsLookup(request):
    template_name = 'performs_list.html'
    queryset = Performs.objects.all().order_by('musician')
    contextual = {
        'performs_list': queryset,
    }
    return render(request, template_name, contextual)

def PlaysLookup(request):
    template_name = 'plays_list.html'
    queryset = Plays.objects.all().order_by('musician')
    contextual = {
        'plays_list': queryset,
    }
    return render(request, template_name, contextual)

def AppearsOnLookup(request):
    template_name = 'appears_on_list.html'
    queryset = AppearsOn.objects.all().order_by('album')
    contextual = {
        'list': queryset,
    }
    return render(request, template_name, contextual)



#Individual item views

def SelectedMusician(request, name, id):
    selected_musician = Musicians.objects.get(name=name, ssn=id)
    song_list = Performs.objects.filter(musician=selected_musician)
    instrument_list = Plays.objects.filter(musician=selected_musician)
    template_name = 'musician.html'
    contextual = {
        'musician': selected_musician,
        'performs_list': song_list,
        'plays_list': instrument_list,
    }
    return render(request, template_name, contextual)

def SelectedAlbum(request, name, id):
    selected_album = Albums.objects.get(albumTitle=name, albumId=id)
    template_name = 'album.html'
    song_list = AppearsOn.objects.filter(album=selected_album)
    contextual = {
            'album': selected_album,
            'songs': song_list,
            }
    return render(request, template_name, contextual)

def SelectedSong(request, name, id):
    selected_song = Songs.objects.get(songTitle=name, songId=id)
    template_name = 'song.html'
    song_list = AppearsOn.objects.filter(song=selected_song)
    contextual = {
        'song': selected_song,
        'appears_on': song_list,
    }
    return render(request, template_name, contextual)



#forms
def Login(request, page=None):
    if request.method == "POST":
        password = request.POST['password']
        user = authenticate(username='user', password=password)
        if user is not None:
            return HttpResponseRedirect('/admin_panel')
        else:
            message = "Incorrect Password"
            messages.error(request, message)
            return HttpResponseRedirect('/')
    else:
        template_name = 'login.html'
        contextual = {}
        return render(request, template_name, contextual)


def AdminHome(request):
    template_name = 'admin.html'
    contextual = {}
    return render(request, template_name, contextual)

def MusiciansInsert(request):
    form = MusicianForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        message = "Musician successfully saved"
        messages.success(request, message)
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "action": "Add",
        "tableName": "Musician",
        "form": form,
    }
    return render(request, "insert.html", context)

def MusiciansUpdate(request, id=None):
    instance = get_object_or_404(Musicians, ssn=id)
    form = MusicianForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Musician successfully saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "action": "Edit",
        "tableName": "Musician",
        "form": form,
    }
    return render(request, "insert.html", context)


def MusiciansDelete(request, id=None):
    instance = get_object_or_404(Musicians, ssn=id)
    instance.delete()
    messages.success(request, "Musician successfully deleted")
    return HttpResponseRedirect("/admin_panel/musicians")





def AlbumsInsert(request):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Album successfully saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "action": "Add",
        "tableName": "Album",
        "form": form,
    }
    return render(request, "insert.html", context)

def AlbumsUpdate(request, id=None):
    instance = get_object_or_404(Albums, albumId=id)
    form = AlbumForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Album successfully saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "action": "Edit",
        "tableName": "Album",
        "form": form,
    }
    return render(request, "insert.html", context)


def AlbumsDelete(request, id=None):
    instance = get_object_or_404(Albums, albumId=id)
    instance.delete()
    messages.success(request, "Album successfully deleted")
    return HttpResponseRedirect("/admin_panel/albums")




def SongsInsert(request):
    form = SongForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Song successfully saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "action": "Add",
        "tableName": "Song",
        "form": form,
    }
    return render(request, "insert.html", context)

def SongsUpdate(request, id=None):
    instance = get_object_or_404(Songs, songId=id)
    form = SongForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Song successfully saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "action": "Edit",
        "tableName": "Song",
        "form": form,
    }
    return render(request, "insert.html", context)


def SongsDelete(request, id=None):
    instance = get_object_or_404(Songs, songId=id)
    instance.delete()
    messages.success(request, "Song successfully deleted")
    return HttpResponseRedirect("/admin_panel/songs")




def InstrumentsInsert(request):
    form = InstrumentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        message = "Instrument successfully saved"
        messages.success(request, message)
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "action": "Add",
        "tableName": "Instrument",
        "form": form,
    }
    return render(request, "insert.html", context)

def InstrumentsUpdate(request, id=None):
    instance = get_object_or_404(Instruments, instrumentId=id)
    form = InstrumentForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Instrument successfully saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "action": "Edit",
        "tableName": "Instrument",
        "form": form,
    }
    return render(request, "insert.html", context)


def InstrumentsDelete(request, id=None):
    instance = get_object_or_404(Instruments, instrumentId=id)
    instance.delete()
    messages.success(request, "Instrument successfully deleted")
    return HttpResponseRedirect("/admin_panel/instruments")






def AddressInsert(request):
    form = AddressForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        message = "Address successfully saved"
        messages.success(request, message)
        return HttpResponseRedirect("/admin_panel/addresses")

    context = {
        "action": "Add",
        "tableName": "Address",
        "form": form,
    }
    return render(request, "insert.html", context)

def AddressUpdate(request, id=None):
    instance = get_object_or_404(Address, addressPhone=id)
    form = AddressForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Address successfully saved")
        return HttpResponseRedirect("/admin_panel/addresses")

    context = {
        "action": "Edit",
        "tableName": "Address",
        "form": form,
    }
    return render(request, "insert.html", context)


def AddressDelete(request, id=None):
    instance = get_object_or_404(Address, addressPhone=id)
    instance.delete()
    messages.success(request, "Address successfully deleted")
    return HttpResponseRedirect("/admin_panel/addresses")



def PlaysInsert(request):
    form = PlaysForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        message = "Instrument successfully linked to Musician"
        messages.success(request, message)
        return HttpResponseRedirect("/admin_panel/musicians")

    context = {
        "action": "Add",
        "tableName": "Plays",
        "form": form,
    }
    return render(request, "insert.html", context)


def PlaysUpdate(request, ssn=None, id=None):
    instance = get_object_or_404(Plays, instrument_id=id, musician_id=ssn)
    form = PlaysForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Instrument successfully linked to Musician")
        musician = Musicians.objects.get(ssn=ssn)
        return HttpResponseRedirect(musician.get_absolute_url())

    context = {
        "action": "Edit",
        "tableName": "Plays",
        "form": form,
    }
    return render(request, "insert.html", context)


def PlaysDelete(request, ssn=None, id=None):
    instance = get_object_or_404(Plays, instrument_id=id, musician_id=ssn)
    instance.delete()
    messages.success(request, "Instrument successfully removed from Musician")
    musician = Musicians.objects.get(ssn=ssn)
    return HttpResponseRedirect(musician.get_absolute_url())





def AppearsOnInsert(request):
    form = AppearsOnForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        message = "Song successfully added to Album"
        messages.success(request, message)
        return HttpResponseRedirect("/admin_panel/albums")

    context = {
        "action": "Add",
        "tableName": "AppearsOn",
        "form": form,
    }
    return render(request, "insert.html", context)


def AppearsOnUpdate(request, ssn=None, id=None):
    instance = get_object_or_404(AppearsOn, album_id=ssn, song_id=id)
    form = AppearsOnForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Song successfuly added to Album")
        album = Albums.objects.get(albumId=ssn)
        return HttpResponseRedirect(album.get_absolute_url())

    context = {
        "action": "Edit",
        "tableName": "AppearsOn",
        "form": form,
    }
    return render(request, "insert.html", context)


def AppearsOnDelete(request, ssn=None, id=None):
    instance = get_object_or_404(AppearsOn, album_id=ssn, song_id=id)
    instance.delete()
    messages.success(request, "Song successfully removed from Album")
    album = Albums.objects.get(albumId=ssn)
    return HttpResponseRedirect(album.get_absolute_url())






def PerformsInsert(request):
    form = PerformsForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        message = "Musician successfully linked to song"
        messages.success(request, message)
        return HttpResponseRedirect("/admin_panel/musicians")

    context = {
        "action": "Add",
        "tableName": "Performs",
        "form": form,
    }
    return render(request, "insert.html", context)


def PerformsUpdate(request, ssn=None, id=None):
    instance = get_object_or_404(Performs, musician_id=ssn, song_id=id)
    form = PerformsForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Musician successfully linked to song")
        musician = Musicians.objects.get(ssn=ssn)
        return HttpResponseRedirect(musician.get_absolute_url())

    context = {
        "action": "Edit",
        "tableName": "Performs",
        "form": form,
    }
    return render(request, "insert.html", context)


def PerformsDelete(request, ssn=None, id=None):
    instance = get_object_or_404(Performs, musician_id=ssn, song_id=id)
    instance.delete()
    messages.success(request, "Musician successfully removed from song")
    musician = Musicians.objects.get(ssn=ssn)
    return HttpResponseRedirect(musician.get_absolute_url())


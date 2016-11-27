import logging
#use logging.warning for console output

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
# from django.core.urlresolvers import reverse_lazy
from django.forms import forms
from .forms import *
# from django.contrib.auth.mixins import LoginRequiredMixin

#instance = model.objects.get(x=y)
#instance = get_object_or_404(model, x=y)

#General User Search Query Views
def Search(request):
    template_name = 'index.html'
    queryset = Musicians.objects.all()
    contextual = {
        'object_list': queryset,
    }
    return render(request, template_name, contextual)

template_name = 'index.html'

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



#Individual item views

def SelectedMusician(request, name, id):
    selected_musician = Musicians.objects.get(name=name, ssn=id)
    template_name = 'musician.html'
    contextual = {
        'musician': selected_musician,
    }
    return render(request, template_name, contextual)

def SelectedAlbum(request, name, id):
    selected_album = Albums.objects.get(albumTitle=name, albumId=id)
    template_name = 'album.html'
    #make this work
#    if query_set = AppearsOn.objects.get(album=selected_album):
#
#        contextual = {
#                'album': selected_album,
#                'songs': query_set
#                }
#
#    else:
#        contextual = {
#                'album': selected_album,
#                }
    contextual = {
            'album': selected_album,
#             'songs': query_set
            }
    return render(request, template_name, contextual)

def SelectedSong(request, name, id):
    selected_song = Songs.objects.get(songTitle=name, songId=id)
    template_name = 'song.html'
    contextual = {
        'song': selected_song,
    }
    return render(request, template_name, contextual)



#forms
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
    return HttpResponseRedirect("/musicians")





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
    return HttpResponseRedirect("/albums")




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
    return HttpResponseRedirect("/songs")




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
    return HttpResponseRedirect("/instruments")






def AddressInsert(request):
    form = AddressForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        message = "Address successfully saved"
        messages.success(request, message)
        return HttpResponseRedirect("/addresses")

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
        return HttpResponseRedirect("/addresses")

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
    return HttpResponseRedirect("/addresses")







# class SongsInsert(LoginRequiredMixin,CreateView):
#     model = Songs
#     success_url = reverse_lazy("songs_insert")
# class AddressInsert(LoginRequiredMixin,CreateView):
#     model = Address
#     success_url = reverse_lazy("address_insert")
# class InstrumentsInsert(LoginRequiredMixin,CreateView):
#     model = Instruments
#     success_url = reverse_lazy("instruments_insert")
# class PerformsInsert(LoginRequiredMixin,CreateView):
#     model = Performs
#     success_url = reverse_lazy("performs_insert")
# class PlaysInsert(LoginRequiredMixin,CreateView):
#     model = Plays
#     success_url = reverse_lazy("plays_insert")

# class SongEdit(LoginRequiredMixin,UpdateView):
#     model = Songs
#     success_url = reverse_lazy("songs_edit")
# class SongsEdit(LoginRequiredMixin,UpdateView):
#     model = Songs
#     success_url = reverse_lazy("songs_edit")
# class AddressEdit(LoginRequiredMixin,UpdateView):
#     model = Address
#     success_url = reverse_lazy("address_edit")
# class InstrumentsEdit(LoginRequiredMixin,UpdateView):
#     model = Instruments
#     success_url = reverse_lazy("instruments_edit")
# class PerformsEdit(LoginRequiredMixin,UpdateView):
#     model = Performs
#     success_url = reverse_lazy("performs_edit")
# class PlaysEdit(LoginRequiredMixin,UpdateView):
#     model = Plays
#     success_url = reverse_lazy("plays_edit")

# class AlbumDelete(LoginRequiredMixin,DeleteView):
#     model = Albums
#     success_url = reverse_lazy("albums_delete")
# class SongsDelete(LoginRequiredMixin,DeleteView):
#     model = Songs
#     success_url = reverse_lazy("songs_delete")
# class AddressDelete(LoginRequiredMixin,DeleteView):
#     model = Address
#     success_url = reverse_lazy("address_delete")
# class InstrumentsDelete(LoginRequiredMixin,DeleteView):
#     model = Instruments
#     success_url = reverse_lazy("instruments_delete")
# class PerformsDelete(LoginRequiredMixin,DeleteView):
#     model = Performs
#     success_url = reverse_lazy("performs_delete")
# class PlaysDelete(LoginRequiredMixin,DeleteView):
#     model = Plays
#     success_url = reverse_lazy("plays_delete")







# class MusiciansLookup(ListView):

#     model               = Musicians
#     context_object_name = 'musicians'
#     template_name       = "musicians.html"

#     # def get_queryset(self):
#     #     # SSN     = self.request.GET.get("ssn")
#     #     NAME    = self.request.GET.get("name")
#     #     # PHONE   = self.request.GET.get("phone")
#     #     # ADDRESS = self.request.GET.get("address")
#     #     # print(SSN, NAME, PHONE, ADDRESS)
#     #     print(NAME)

#     def get(self, request, *args, **kwargs):
#         self.object_list = self.get_queryset().order_by("name")
#         context = self.get_context_data()
#         return self.render_to_response(context)

# class AlbumLookup(ListView):

#     model               = Albums
#     context_object_name = 'albums'
#     template_name       = "albums.html"

#     def get(self, request, *args, **kwargs):
#         self.object_list = self.get_queryset().order_by("title")
#         context = self.get_context_data()
#         return self.render_to_response(context)

# class SongLookup(ListView):

#     model               = Songs
#     context_object_name = 'songs'
#     template_name       = "songs.html"

#     def get(self, request, *args, **kwargs):
#         self.object_list = self.get_queryset().order_by("title")
#         context = self.get_context_data()
#         return self.render_to_response(context)





# # #Admin Del/Add/Edit Views

# class AlbumInsert(LoginRequiredMixin,CreateView):
#     model = Albums
#     form = AlbumsForm()
#     success_url = reverse_lazy("albums")
#     fields = "__all__"
#     # login_url = '/accounts/login'

#     def form_valid(self,form):
#         # if((form.cleaned_data['id']) <= 0):
#         return super(AlbumInsert, self).form_valid(form)

#     def post(self, request, *args, **kwargs):
#         if request.POST['password'] != "cs430":
#             return HttpResponseRedirect("/albums")
#         return super(AlbumInsert, self).post(request, *args, **kwargs)





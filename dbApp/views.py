import logging
#use logging.warning for console output

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from django.core.urlresolvers import reverse_lazy
#from django.forms import forms
#from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

#instance = model.objects.get(x=y)
#instance = get_object_or_404(model, x=y)

#General User Search Query Views
def MusicianLookup(request):
    template_name = 'musician_list.html'
    queryset = Musicians.objects.all()
    contextual = {
        'musician_list': queryset,
    }
    return render(request, template_name, contextual)

def SelectedMusician(request, name):
    selected_musician = Musicians.objects.get(name=name)
    template_name = 'musician.html'
    contextual = {
        'musician': selected_musician,
    }
    return render(request, template_name, contextual)

def AlbumLookup(request):
    template_name = 'album_list.html'
    queryset = Albums.objects.all()
    contextual = {
        'album_list': queryset,
    }
    return render(request, template_name, contextual)

def SelectedAlbum(request, title):
    selected_album = Albums.objects.get(albumTitle=title)
    logging.warning(selected_album)
    query_set = AppearsOn.objects.get(album=selected_album)
    logging.warning(query_set)
    template_name = 'album.html'
    contextual = {
        'album': selected_album,
        'songs': query_set
    }
    return render(request, template_name, contextual)

def SongLookup(request):
    template_name = 'song_list.html'
    queryset = Songs.objects.all().order_by('appearson')
    contextual = {
        'song_list': queryset,
    }
    return render(request, template_name, contextual)

def SelectedSong(request, title):
    selected_song = Songs.objects.get(songTitle=title)
    template_name = 'song.html'
    contextual = {
        'song': selected_song,
    }
    return render(request, template_name, contextual)


















# class MusiciansInsert(LoginRequiredMixin,CreateView):
#     model = Musicians
#     success_url = reverse_lazy("musicians_insert")
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

# class AlbumEdit(LoginRequiredMixin,UpdateView):
#     model = Albums
#     success_url = reverse_lazy("albums_edit")
# class MusiciansEdit(LoginRequiredMixin,UpdateView):
#     model = Musicians
#     success_url = reverse_lazy("musicians_edit")
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
# class MusiciansDelete(LoginRequiredMixin,DeleteView):
#     model = Musicians
#     success_url = reverse_lazy("musicians_delete")
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





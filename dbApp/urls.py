from django.conf.urls import include, url
from . import views

urlpatterns = (
    url(r'^$', views.MusicianLookup),
    url(r'^songs/$', views.SongLookup),
    url(r'^albums/$', views.AlbumLookup),
    url(r'^musicians/(?P<name>\w+)', views.SelectedMusician, name='selected_musician'),
    url(r'^albums/(?P<name>\w+)', views.SelectedAlbum, name='selected_album'),
    url(r'^songs/(?P<name>\w+)', views.SelectedSong, name='selected_song'),
        )

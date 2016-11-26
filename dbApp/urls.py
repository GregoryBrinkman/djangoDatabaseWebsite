from django.conf.urls import include, url
from . import views

urlpatterns = (
    url(r'^$', views.Search),
    url(r'^musicians/insert/$', views.MusiciansInsert),
    url(r'^musicians/$', views.MusicianLookup),
    url(r'^musicians/(?P<name>[a-zA-z_. ]+)/$', views.SelectedMusician, name='selected_musician'),
    url(r'^musicians/(?P<name>[a-zA-z_. ]+)/edit/$', views.MusiciansUpdate, name='musician_update'),
    url(r'^musicians/(?P<name>[a-zA-z_. ]+)/delete/$', views.MusiciansDelete, name='musician_delete'),
    url(r'^songs/$', views.SongLookup),
    url(r'^albums/$', views.AlbumLookup),
    url(r'^albums/(?P<title>[a-zA-z_. ]+)/$', views.SelectedAlbum, name='selected_album'),
    url(r'^songs/(?P<title>[a-zA-z_. ]+)/$', views.SelectedSong, name='selected_song'),
        )

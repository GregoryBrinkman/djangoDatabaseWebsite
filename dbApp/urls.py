from django.conf.urls import include, url
from . import views

urlpatterns = (
    url(r'^$', views.Search),

    url(r'^musicians/$', views.UserMusicianLookup),
    url(r'^musicians/(?P<id>[\d]+)/(?P<name>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};\\|,.<>\/? ]+)/$', views.UserSelectedMusician),
    url(r'^songs/$', views.UserSongLookup),
    url(r'^songs/(?P<id>[\d]+)/$', views.UserSelectedSong),
    url(r'^albums/$', views.UserAlbumLookup),
    url(r'^albums/(?P<id>[\d]+)/(?P<name>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};\\|,.<>\/? ]+)$', views.UserSelectedAlbum),

    url(r'^login/$', views.Login),
    url(r'^admin_panel/$', views.AdminHome),

    url(r'^admin_panel/musicians/$', views.MusicianLookup),
    url(r'^admin_panel/musicians/insert/$', views.MusiciansInsert),
    url(r'^admin_panel/musicians/(?P<id>[\d]+)/(?P<name>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};\\|,.<>\/? ]+)/$', views.SelectedMusician, name='selected_musician'),
    url(r'^admin_panel/musician/(?P<id>[\d]+)/edit/$', views.MusiciansUpdate, name='musician_update'),
    url(r'^admin_panel/musician/(?P<id>[\d]+)/delete/$', views.MusiciansDelete, name='musician_delete'),


    url(r'^admin_panel/songs/$', views.SongLookup),
    url(r'^admin_panel/songs/insert/$', views.SongsInsert),
    url(r'^admin_panel/songs/(?P<id>[\d]+)/(?P<name>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};\\|,.<>\/? ]+)$', views.SelectedSong, name='selected_song'),
    url(r'^admin_panel/song/(?P<id>[\d]+)/edit/$', views.SongsUpdate, name='song_update'),
    url(r'^admin_panel/song/(?P<id>[\d]+)/delete/$', views.SongsDelete, name='song_delete'),


    url(r'^admin_panel/albums/$', views.AlbumLookup),
    url(r'^admin_panel/albums/insert/$', views.AlbumsInsert),
    url(r'^admin_panel/albums/(?P<id>[\d]+)/(?P<name>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};\\|,.<>\/? ]+)$', views.SelectedAlbum, name='selected_album'),
    url(r'^admin_panel/album/(?P<id>[\d]+)/edit/$', views.AlbumsUpdate, name='album_update'),
    url(r'^admin_panel/album/(?P<id>[\d]+)/delete/$', views.AlbumsDelete, name='album_delete'),

    url(r'^admin_panel/instruments/$', views.InstrumentLookup),
    url(r'^admin_panel/instruments/insert/$', views.InstrumentsInsert),
    url(r'^admin_panel/instruments/(?P<id>[\d]+)/edit/$', views.InstrumentsUpdate, name='instrument_update'),
    url(r'^admin_panel/instruments/(?P<id>[\d]+)/delete/$', views.InstrumentsDelete, name='instrument_delete'),

    url(r'^admin_panel/performs/$', views.PerformsLookup),
    url(r'^admin_panel/performs/insert/$', views.PerformsInsert),
    url(r'^admin_panel/performs/(?P<ssn>[\d]+)/(?P<id>[\d]+)/edit/$', views.PerformsUpdate),
    url(r'^admin_panel/performs/(?P<ssn>[\d]+)/(?P<id>[\d]+)/delete/$', views.PerformsDelete),

    url(r'^admin_panel/appears_on/$', views.AppearsOnLookup),
    url(r'^admin_panel/appears_on/insert/$', views.AppearsOnInsert),
    url(r'^admin_panel/appears_on/(?P<ssn>[\d]+)/(?P<id>[\d]+)/edit/$', views.AppearsOnUpdate),
    url(r'^admin_panel/appears_on/(?P<ssn>[\d]+)/(?P<id>[\d]+)/delete/$', views.AppearsOnDelete),

    url(r'^admin_panel/plays/$', views.PlaysLookup),
    url(r'^admin_panel/plays/insert/$', views.PlaysInsert),
    url(r'^admin_panel/plays/(?P<ssn>[\d]+)/(?P<id>[\d]+)/edit/$', views.PlaysUpdate),
    url(r'^admin_panel/plays/(?P<ssn>[\d]+)/(?P<id>[\d]+)/delete/$', views.PlaysDelete),

    url(r'^admin_panel/addresses/$', views.AddressLookup),
    url(r'^admin_panel/addresses/insert/$', views.AddressInsert),
    url(r'^admin_panel/addresses/(?P<id>[\d]+)/edit/$', views.AddressUpdate, name='address_update'),
    url(r'^admin_panel/addresses/(?P<id>[\d]+)/delete/$', views.AddressDelete, name='address_delete'),
        )

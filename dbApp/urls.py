from django.conf.urls import include, url
from . import views

urlpatterns = (
    url(r'^$', views.Search),
    url(r'^admin_panel/$', views.AdminHome),

    url(r'^musicians/$', views.MusicianLookup),
    url(r'^musicians/insert/$', views.MusiciansInsert),
    url(r'^musicians/(?P<id>[\d]+)/(?P<name>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};\\|,.<>\/? ]+)/$', views.SelectedMusician, name='selected_musician'),
    url(r'^musician/(?P<id>[\d]+)/edit/$', views.MusiciansUpdate, name='musician_update'),
    url(r'^musician/(?P<id>[\d]+)/delete/$', views.MusiciansDelete, name='musician_delete'),


    url(r'^songs/$', views.SongLookup),
    url(r'^songs/insert/$', views.SongsInsert),
    url(r'^songs/(?P<id>[\d]+)/(?P<name>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};\\|,.<>\/? ]+)$', views.SelectedSong, name='selected_song'),
    url(r'^song/(?P<id>[\d]+)/edit/$', views.SongsUpdate, name='song_update'),
    url(r'^song/(?P<id>[\d]+)/delete/$', views.SongsDelete, name='song_delete'),


    url(r'^albums/$', views.AlbumLookup),
    url(r'^albums/insert/$', views.AlbumsInsert),
    url(r'^albums/(?P<id>[\d]+)/(?P<name>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};\\|,.<>\/? ]+)$', views.SelectedAlbum, name='selected_album'),
    url(r'^album/(?P<id>[\d]+)/edit/$', views.AlbumsUpdate, name='album_update'),
    url(r'^album/(?P<id>[\d]+)/delete/$', views.AlbumsDelete, name='album_delete'),

    url(r'^instruments/$', views.InstrumentLookup),
    url(r'^instruments/insert/$', views.InstrumentsInsert),
    url(r'^instruments/(?P<id>[\d]+)/edit/$', views.InstrumentsUpdate, name='instrument_update'),
    url(r'^instruments/(?P<id>[\d]+)/delete/$', views.InstrumentsDelete, name='instrument_delete'),

    # url(r'^connect/performs/$', views.PerformsInsert),
    # url(r'^connect/appears_on/$', views.AppearsOnInsert),
    # url(r'^connect/plays/$', views.PlaysInsert),

    url(r'^addresses/$', views.AddressLookup),
    url(r'^addresses/insert/$', views.AddressInsert),
    url(r'^addresses/(?P<id>[\d]+)/edit/$', views.AddressUpdate, name='address_update'),
    url(r'^addresses/(?P<id>[\d]+)/delete/$', views.AddressDelete, name='address_delete'),
        )

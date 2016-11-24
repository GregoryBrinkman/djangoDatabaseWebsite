from django.conf.urls import include, url
from . import views

urlpatterns = (
    # url(r'^musicians/(?P<name>\w+)/$', views.MusicianLookup),
    url(r'^$', views.MusicianLookup),
    url(r'^musicians/(?P<name>\w+)', views.SelectedMusician, name='selected_musician'),
    url(r'^albums/$', views.AlbumLookup),
    url(r'^songs/$', views.SongLookup),
        )

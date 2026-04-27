from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets, views

router = DefaultRouter()
router.register(r'artists', viewsets.ArtistViewSet)
router.register(r'bands', viewsets.BandViewSet)
router.register(r'albums', viewsets.AlbumViewSet)
router.register(r'generos', viewsets.GeneroMusicalViewSet)
router.register(r'songs', viewsets.SongsViewSet)
router.register(r'playlists', viewsets.PlaylistViewSet)
router.register(r'users', viewsets.UsersViewSet)
router.register(r'albumartist', viewsets.AlbumartistViewSet)
router.register(r'albumband', viewsets.AlbumbandViewSet)
router.register(r'artistsband', viewsets.ArtistsbandViewSet)
router.register(r'songsplaylist', viewsets.SongsplaylistViewSet)
router.register(r'usersplaylists', viewsets.UsersplaylistsViewSet)

urlpatterns = [
    path('login/', views.login, name='login'),
    path('upload/image/', views.upload_image, name='upload_image'),
    path('', include(router.urls)),
]
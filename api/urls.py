from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'artists', viewsets.ArtistViewSet)
router.register(r'bands', viewsets.BandViewSet)
router.register(r'albums', viewsets.AlbumViewSet)
router.register(r'generos', viewsets.GeneroMusicalViewSet)
router.register(r'songs', viewsets.SongsViewSet)
router.register(r'playlists', viewsets.PlaylistViewSet)
router.register(r'users', viewsets.UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
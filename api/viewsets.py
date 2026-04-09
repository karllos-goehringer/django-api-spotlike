from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from api import models


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class BandViewSet(viewsets.ModelViewSet):
    queryset = models.Band.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class GeneroMusicalViewSet(viewsets.ModelViewSet):
    queryset = models.GeneroMusical.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class SongsViewSet(viewsets.ModelViewSet):
    queryset = models.Songs.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = models.Playlist.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
class UsersViewSet(viewsets.ModelViewSet):
    queryset = models.Users.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

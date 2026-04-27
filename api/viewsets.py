from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from api import models, serializers


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class BandViewSet(viewsets.ModelViewSet):
    queryset = models.Band.objects.all()
    serializer_class = serializers.BandSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    @action(detail=True, methods=['get'])
    def songs(self, request, pk=None):
        """
        Retorna todas as músicas de um álbum específico.
        
        Exemplo: GET /api/albums/1/songs/
        """
        album = self.get_object()
        songs = models.Songs.objects.filter(album_pk_albumid1=album)
        serializer = serializers.SongsSerializer(songs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_owner(self, request, pk=None):
        """
        Busca o artista ou a banda vinculada a este álbum através das tabelas de relação.
        
        Exemplo: GET /api/albums/1/get_owner/
        """
        album = self.get_object()
        
        # Verifica se há artistas associados (tabela Albumartist)
        album_artists = models.Albumartist.objects.filter(album_PK_albumID=album)
        if album_artists.exists():
            artists = [rel.artist_PK_artistID for rel in album_artists]
            serializer = serializers.ArtistSerializer(artists, many=True)
            return Response({
                'owner_type': 'artist',
                'data': serializer.data
            })
            
        # Se não houver artistas, verifica se há bandas associadas (tabela Albumband)
        album_bands = models.Albumband.objects.filter(album_PK_albumID=album)
        if album_bands.exists():
            bands = [rel.band_PK_bandID for rel in album_bands]
            serializer = serializers.BandSerializer(bands, many=True)
            return Response({
                'owner_type': 'band',
                'data': serializer.data
            })
            
        return Response(
            {'detail': 'Nenhum artista ou banda associado a este álbum.'}, 
            status=status.HTTP_404_NOT_FOUND
        )

class GeneroMusicalViewSet(viewsets.ModelViewSet):
    queryset = models.GeneroMusical.objects.all()
    serializer_class = serializers.GeneroMusicalSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    @action(detail=True, methods=['get'])
    def albums(self, request, pk=None):
        """
        Retorna todos os albums de um gênero específico.
        
        Exemplo: GET /api/generos/1/albums/
        """
        genero = self.get_object()
        albums = models.Album.objects.filter(
            songs__generomusical_idgeneroMusical=genero
        ).distinct()
        serializer = serializers.AlbumSerializer(albums, many=True)
        return Response(serializer.data)

class SongsViewSet(viewsets.ModelViewSet):
    queryset = models.Songs.objects.all()
    serializer_class = serializers.SongsSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializers.PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
    @action(detail=True, methods=['get'])
    def songs(self, request, pk=None):
        """
        Retorna todas as músicas de uma playlist específica.
        
        Exemplo: GET /api/playlists/1/songs/
        """
        playlist = self.get_object()
        songs = models.Songs.objects.filter(
            songsplaylist__playlist_PK_playlistID=playlist
        ).order_by('songsplaylist__ordem')
        serializer = serializers.SongsSerializer(songs, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'], serializer_class=serializers.CreatePlaylistSerializer)
    def create_playlist_for_user(self, request):
        """
        Cria uma nova playlist e associa au usuário logado.
        
        Exemplo de requisição:
        POST /api/playlists/create_playlist_for_user/
        {
            "plName": "Minha Nova Playlist"
        }
        
        Retorna os dados da associação criada (Usersplaylists).
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usersplaylist = serializer.save()
        
        response_serializer = serializers.UsersplaylistsSerializer(usersplaylist)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], serializer_class=serializers.AddSongPlaylistSerializer)
    def add_song(self, request):
        """Adiciona uma música a uma playlist existente."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        songsplaylist = serializer.save()
        response_serializer = serializers.SongsplaylistSerializer(songsplaylist)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], serializer_class=serializers.RemoveSongPlaylistSerializer)
    def remove_song(self, request):
        """Remove uma música de uma playlist existente."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.delete(serializer.validated_data)
        return Response({'detail': 'Música removida da playlist'}, status=status.HTTP_200_OK)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = models.Users.objects.all()
    serializer_class = serializers.UsersSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    @action(detail=True, methods=['get'])
    def playlists(self, request, pk=None):
        """
        Retorna todas as playlists de um usuário específico.
        
        Exemplo: GET /api/users/1/playlists/
        """
        user = self.get_object()
        user_playlists = models.Usersplaylists.objects.filter(users_PK_userID=user)
        playlists = [up.playlist_PK_playlistID for up in user_playlists]
        serializer = serializers.PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

class AlbumartistViewSet(viewsets.ModelViewSet):
    queryset = models.Albumartist.objects.all()
    serializer_class = serializers.AlbumartistSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class AlbumbandViewSet(viewsets.ModelViewSet):
    queryset = models.Albumband.objects.all()
    serializer_class = serializers.AlbumbandSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class ArtistsbandViewSet(viewsets.ModelViewSet):
    queryset = models.Artistsband.objects.all()
    serializer_class = serializers.ArtistsbandSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class SongsplaylistViewSet(viewsets.ModelViewSet):
    queryset = models.Songsplaylist.objects.all()
    serializer_class = serializers.SongsplaylistSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

class UsersplaylistsViewSet(viewsets.ModelViewSet):
    queryset = models.Usersplaylists.objects.all()
    serializer_class = serializers.UsersplaylistsSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

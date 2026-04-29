import hashlib

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.db.models import Q
from api import models, serializers


def verify_password(raw_password: str, hashed_password: str) -> bool:
    if not raw_password or not hashed_password:
        return False
    return hashlib.sha1(raw_password.encode('utf-8')).hexdigest() == hashed_password


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    @action(detail=True, methods=['get'])
    def albums(self, request, pk=None):
        """Retorna todos os álbuns de um artista específico."""
        artist = self.get_object()
        album_artists = models.Albumartist.objects.filter(artist_PK_artistID=artist)
        albums = [rel.album_PK_albumID for rel in album_artists]
        serializer = serializers.AlbumSerializer(albums, many=True)
        return Response(serializer.data)

class BandViewSet(viewsets.ModelViewSet):
    queryset = models.Band.objects.all()
    serializer_class = serializers.BandSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    @action(detail=True, methods=['get'])
    def albums(self, request, pk=None):
        """Retorna todos os álbuns de uma banda específica."""
        band = self.get_object()
        album_bands = models.Albumband.objects.filter(band_PK_bandID=band)
        albums = [rel.album_PK_albumID for rel in album_bands]
        serializer = serializers.AlbumSerializer(albums, many=True)
        return Response(serializer.data)

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
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    
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
        Cria uma nova playlist e associa ao usuário especificado ou logado.
        
        Exemplo de requisição (form-data ou JSON):
        POST /api/playlists/create_playlist_for_user/
        {
            "plName": "Minha Nova Playlist",
            "description": "Descrição opcional da playlist",
            "plImage": [arquivo de imagem],
            "user_id": 123 (opcional, usa usuário logado se não informado)
        }
        
        O campo de nome pode ser enviado como:
        - plName (padrão)
        - playlist_name
        - name
        - title
        
        Retorna os dados da associação criada (Usersplaylists) com informações da playlist.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usersplaylist = serializer.save()
        
        # Retorna dados da associação com dados completos da playlist
        response_data = {
            'id': usersplaylist.users_PK_userID.PK_userID,
            'users_PK_userID': usersplaylist.users_PK_userID.PK_userID,
            'playlist_PK_playlistID': usersplaylist.playlist_PK_playlistID.PK_playlistID,
            'playlist': {
                'PK_playlistID': usersplaylist.playlist_PK_playlistID.PK_playlistID,
                'plName': usersplaylist.playlist_PK_playlistID.plName,
                'description': usersplaylist.playlist_PK_playlistID.description,
                'plImage': usersplaylist.playlist_PK_playlistID.plImage.url if usersplaylist.playlist_PK_playlistID.plImage else None,
                'plImage_path': str(usersplaylist.playlist_PK_playlistID.plImage) if usersplaylist.playlist_PK_playlistID.plImage else None,
            }
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], serializer_class=serializers.AddSongPlaylistSerializer)
    def add_song(self, request):
        """Adiciona uma música a uma playlist existente."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if models.Songsplaylist.objects.filter(
            playlist_PK_playlistID=serializer.validated_data.get('playlist_id'),
            songs_PK_songID=serializer.validated_data.get('song_id')
        ).exists():
            return Response({'detail': 'Música já adicionada a esta playlist.'}, status=status.HTTP_400_BAD_REQUEST)

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

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny], url_path='register')
    def register(self, request):
        """Registra um novo usuário na tabela Users com senha criptografada."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if models.Users.objects.filter(name=serializer.validated_data.get('name')).exists():
            return Response({'detail': 'Nome de usuário já cadastrado.'}, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get('email')
        if email and models.Users.objects.filter(email=email).exists():
            return Response({'detail': 'E-mail já cadastrado.'}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        return Response({
            'id': user.PK_userID,
            'name': user.name,
            'email': user.email,
        }, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny], url_path='login')
    def login(self, request):
        """Autentica usuário por e-mail ou nome e retorna o ID do usuário."""
        identifier = (
            request.data.get('username')
            or request.data.get('email')
            or request.data.get('name')
            or request.data.get('identifier')
        )
        password = request.data.get('password') or request.data.get('senha')

        if not identifier or not password:
            return Response(
                {'detail': 'Nome de usuário ou e-mail e senha são obrigatórios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = models.Users.objects.filter(Q(name=identifier) | Q(email=identifier)).first()
        if user is None or not verify_password(password, user.senha):
            return Response(
                {'detail': 'Usuário ou senha incorretos.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response({'id': user.PK_userID}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        self.perform_destroy(user)
        return Response({'detail': 'Usuário excluído com sucesso.'}, status=status.HTTP_200_OK)

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

class SearchViewSet(viewsets.ViewSet):
    """
    ViewSet para busca global em múltiplos modelos (Artista, Banda, Álbum e Música).
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    def list(self, request):
        """
        Realiza uma busca baseada no parâmetro 'q'.
        Exemplo: GET /api/search/?q=nome_do_item
        """
        query = request.query_params.get('q', '')
        if not query:
            return Response(
                {'detail': 'O parâmetro de busca "q" é obrigatório.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        artists = models.Artist.objects.filter(name__icontains=query)
        bands = models.Band.objects.filter(name__icontains=query)
        albums = models.Album.objects.filter(albumName__icontains=query)
        songs = models.Songs.objects.filter(songtitle__icontains=query)

        return Response({
            'artists': serializers.ArtistSerializer(artists, many=True).data,
            'bands': serializers.BandSerializer(bands, many=True).data,
            'albums': serializers.AlbumSerializer(albums, many=True).data,
            'songs': serializers.SongsSerializer(songs, many=True).data,
        })

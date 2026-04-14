from api import models
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artist
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Band
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = '__all__'

class GeneroMusicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GeneroMusical
        fields = '__all__'

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Songs
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Playlist
        fields = '__all__'

class AlbumartistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Albumartist
        fields = '__all__'

class AlbumbandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Albumband
        fields = '__all__'

class ArtistsbandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artistsband
        fields = '__all__'

class SongsplaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Songsplaylist
        fields = '__all__'

class UsersplaylistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usersplaylists
        fields = '__all__'

# Serializer personalizado para criar playlist
class CreatePlaylistSerializer(serializers.Serializer):
    plName = serializers.CharField(max_length=45, required=True)
    
    def create(self, validated_data):
        """
        Cria uma nova playlist e associa ao usuário logado.
        Retorna a instância da Usersplaylists criada.
        """
        user = self.context['request'].user
        
        # Converte o usuário Django para modelo Users (se necessário)
        try:
            spotlike_user = models.Users.objects.get(pk_userid=user.id)
        except models.Users.DoesNotExist:
            raise serializers.ValidationError("Usuário não encontrado no banco de dados da aplicação.")
        
        # Cria a playlist
        playlist = models.Playlist.objects.create(plName=validated_data['plName'])
        
        # Cria a associação entre usuário e playlist
        usersplaylist = models.Usersplaylists.objects.create(
            users_PK_userID=spotlike_user,
            playlist_PK_playlistID=playlist
        )
        
        return usersplaylist
    
class AddSongPlaylistSerializer(serializers.Serializer):
    playlist_id = serializers.IntegerField(required=True)
    song_id = serializers.IntegerField(required=True)
    ordem = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """
        Adiciona uma música a uma playlist existente.
        Retorna a instância da Songsplaylist criada.
        """
        try:
            playlist = models.Playlist.objects.get(pk=validated_data['playlist_id'])
        except models.Playlist.DoesNotExist:
            raise serializers.ValidationError("Playlist não encontrada.")
        
        try:
            song = models.Songs.objects.get(pk=validated_data['song_id'])
        except models.Songs.DoesNotExist:
            raise serializers.ValidationError("Música não encontrada.")
        
        songsplaylist = models.Songsplaylist.objects.create(
            playlist_PK_playlistID=playlist,
            songs_PK_songID=song,
            ordem=validated_data.get('ordem', 0)  
        )
        
        return songsplaylist
    
class RemoveSongPlaylistSerializer(serializers.Serializer):
    playlist_id = serializers.IntegerField(required=True)
    song_id = serializers.IntegerField(required=True)

    def validate_playlist_id(self, value):
        """Valida se a playlist existe"""
        if not models.Playlist.objects.filter(PK_playlistID=value).exists():
            raise serializers.ValidationError("Playlist não encontrada.")
        return value

    def validate_song_id(self, value):
        """Valida se a música existe"""
        if not models.Songs.objects.filter(PK_songID=value).exists():
            raise serializers.ValidationError("Música não encontrada.")
        return value

    def delete(self, validated_data):
        """
        Remove uma música de uma playlist existente.
        Retorna um booleano indicando se a remoção foi bem-sucedida.
        """
        try:
            songsplaylist = models.Songsplaylist.objects.get(
                playlist_PK_playlistID=validated_data['playlist_id'],
                songs_PK_songID=validated_data['song_id']
            )
            songsplaylist.delete()
            return True
        except models.Songsplaylist.DoesNotExist:
            raise serializers.ValidationError("Associação entre música e playlist não encontrada.")

class SongRequestsSerializer(serializers.Serializer):
    """
    Serializer para requisitar/buscar músicas com filtros.
    Suporta filtros por gênero, álbum e título.
    """
    song_id = serializers.IntegerField(required=False, allow_null=True)
    title = serializers.CharField(max_length=150, required=False, allow_blank=True)
    genre_id = serializers.IntegerField(required=False, allow_null=True)
    album_id = serializers.IntegerField(required=False, allow_null=True)
    limit = serializers.IntegerField(required=False, default=10, min_value=1, max_value=100)
    offset = serializers.IntegerField(required=False, default=0, min_value=0)

    def validate_genre_id(self, value):
        """Valida se o gênero existe"""
        if value and not models.GeneroMusical.objects.filter(idgeneroMusical=value).exists():
            raise serializers.ValidationError("Gênero musical não encontrado.")
        return value

    def validate_album_id(self, value):
        """Valida se o álbum existe"""
        if value and not models.Album.objects.filter(PK_albumID=value).exists():
            raise serializers.ValidationError("Álbum não encontrado.")
        return value

    def validate_song_id(self, value):
        """Valida se a música existe"""
        if value and not models.Songs.objects.filter(PK_songID=value).exists():
            raise serializers.ValidationError("Música não encontrada.")
        return value

    def filter_songs(self, validated_data):
        """
        Filtra músicas de acordo com os critérios fornecidos.
        Retorna uma lista de músicas com serialização completa.
        """
        queryset = models.Songs.objects.all()

        # Filtro por ID da música
        if validated_data.get('song_id'):
            queryset = queryset.filter(PK_songID=validated_data['song_id'])

        # Filtro por título (contém)
        if validated_data.get('title'):
            queryset = queryset.filter(songtitle__icontains=validated_data['title'])

        # Filtro por gênero
        if validated_data.get('genre_id'):
            queryset = queryset.filter(generomusical_idgeneroMusical=validated_data['genre_id'])

        # Filtro por álbum
        if validated_data.get('album_id'):
            queryset = queryset.filter(album_pk_albumid1=validated_data['album_id'])

        # Aplicar limite e offset para paginação
        offset = validated_data.get('offset', 0)
        limit = validated_data.get('limit', 10)
        queryset = queryset[offset:offset + limit]

        # Serializar resultados
        return SongsSerializer(queryset, many=True).data
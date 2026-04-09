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

class AlbummusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Albummusica
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
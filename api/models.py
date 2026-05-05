from django.db import models

class Artist(models.Model):
    PK_artistID = models.AutoField(db_column='PK_artistID', primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    imageArtist = models.ImageField(upload_to='images/', blank=True, null=True, db_column='imageArtist')
    backgroundImage = models.ImageField(upload_to='images/', blank=True, null=True, db_column='backgroundImage')

    class Meta:
        managed = False
        db_table = 'artist'

class Band(models.Model):
    PK_bandID = models.AutoField(db_column='PK_bandID', primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True, null=True)
    imageBand = models.ImageField(upload_to='images/', blank=True, null=True, db_column='imageBand')
    backgroundImage = models.ImageField(upload_to='images/', blank=True, null=True, db_column='backgroundImage')

    class Meta:
        managed = False
        db_table = 'band'

class Album(models.Model):
    PK_albumID = models.AutoField(db_column='PK_albumID', primary_key=True)
    albumName = models.CharField(db_column='albumName', max_length=100)
    releaseDate = models.DateField(db_column='releaseDate', blank=True, null=True)
    albumimage = models.ImageField(upload_to='images/', blank=True, null=True, db_column='albumimage')

    class Meta:
        managed = False
        db_table = 'album'

class GeneroMusical(models.Model):
    idgeneroMusical = models.AutoField(primary_key=True, db_column='idgeneroMusical')
    nomeGenero = models.CharField(max_length=150, db_column='nomeGenero')

    class Meta:
        managed = False
        db_table = 'generomusical'

class Songs(models.Model):
    PK_songID = models.AutoField(db_column='PK_songID', primary_key=True)
    songtitle = models.CharField(max_length=150, db_column='songTitle')
    timeMusic = models.TimeField(blank=True, null=True, db_column='timeMusic')
    lyrics = models.TextField(blank=True, null=True)
    songpath = models.FileField(upload_to='songs/', blank=True, null=True, db_column='songpath')
    generomusical_idgeneroMusical = models.ForeignKey(
        GeneroMusical,
        on_delete=models.CASCADE,
        db_column='generomusical_idgeneroMusical'
    )
    album_pk_albumid1 = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        db_column='album_PK_albumID1'
    )

    class Meta:
        managed = False
        db_table = 'songs'

class Playlist(models.Model):
    PK_playlistID = models.AutoField(db_column='PK_playlistID', primary_key=True)
    plName = models.CharField(db_column='plName', max_length=45, blank=True, null=True)
    description = models.CharField(db_column='description', max_length=2048, blank=True, null=True)
    plImage = models.ImageField(upload_to='images/', blank=True, null=True, db_column='plImage')

    class Meta:
        managed = False
        db_table = 'playlist'

class Users(models.Model):
    PK_userID = models.AutoField(db_column='PK_userID', primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=250, blank=True, null=True)
    senha = models.CharField(max_length=45)
    profilepicture = models.ImageField(upload_to='images/', blank=True, null=True, db_column='profilePicture')

    class Meta:
        managed = False
        db_table = 'users'

# TABELAS INTERMEDIÁRIAS

class Albumartist(models.Model):
    artist_PK_artistID = models.ForeignKey(Artist, on_delete=models.CASCADE, db_column='artist_PK_artistID')
    album_PK_albumID = models.ForeignKey(Album, on_delete=models.CASCADE, db_column='album_PK_albumID')

    class Meta:
        managed = False  # Atenção a isso (leia abaixo)
        db_table = 'albumartist'
        # Isso garante que o par Artista + Álbum seja único
        unique_together = (('artist_PK_artistID', 'album_PK_albumID'),)

class Albumband(models.Model):
    # Removido o primary_key=True
    band_PK_bandID = models.ForeignKey(Band, on_delete=models.CASCADE, db_column='band_PK_bandID')
    album_PK_albumID = models.ForeignKey(Album, on_delete=models.CASCADE, db_column='album_PK_albumID')

    class Meta:
        managed = False
        db_table = 'albumband'
        unique_together = (('band_PK_bandID', 'album_PK_albumID'),)

class Artistsband(models.Model):
    artist_PK_artistID = models.ForeignKey(Artist, on_delete=models.CASCADE, db_column='artist_PK_artistID', primary_key=True)
    band_PK_bandID = models.ForeignKey(Band, on_delete=models.CASCADE, db_column='band_PK_bandID')

    class Meta:
        managed = False
        db_table = 'artistsband'
        unique_together = (('artist_PK_artistID', 'band_PK_bandID'),)

class Songsplaylist(models.Model):
    PK_songsplaylistID = models.AutoField(primary_key=True, db_column='PK_songsplaylistID')
    playlist_PK_playlistID = models.ForeignKey(Playlist, on_delete=models.CASCADE, db_column='playlist_PK_playlistID')
    songs_PK_songID = models.ForeignKey(Songs, on_delete=models.CASCADE, db_column='songs_PK_songID')
    ordem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'songsplaylist'

class Usersplaylists(models.Model):
    users_PK_userID = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='users_PK_userID', primary_key=True)
    playlist_PK_playlistID = models.ForeignKey(Playlist, on_delete=models.CASCADE, db_column='playlist_PK_playlistID')

    class Meta:
        managed = False
        db_table = 'usersplaylists'
        unique_together = (('users_PK_userID', 'playlist_PK_playlistID'),)
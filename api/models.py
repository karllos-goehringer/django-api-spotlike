from django.db import models

class Artist(models.Model):
    pk_artistid = models.AutoField(db_column='PK_artistID', primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    imageartist = models.FileField(upload_to='images/')

    class Meta:
        managed = False
        db_table = 'artist'

class Band(models.Model):
    pk_bandid = models.AutoField(db_column='PK_bandID', primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True, null=True)
    imageband = models.FileField(upload_to='images/')

    class Meta:
        managed = False
        db_table = 'band'

class Album(models.Model):
    pk_albumid = models.AutoField(db_column='PK_albumID', primary_key=True)
    albumname = models.CharField(db_column='albumName', max_length=100)
    releasedate = models.DateField(db_column='releaseDate', blank=True, null=True)
    albumimage =  models.FileField(upload_to='images/')
    class Meta:
        managed = False
        db_table = 'album'

from django.db import models

class GeneroMusical(models.Model):
    idgeneroMusical = models.AutoField(primary_key=True)
    nomeGenero = models.CharField(max_length=45)

    class Meta:
        db_table = 'generomusical'

class Songs(models.Model):
    PK_songID = models.AutoField(primary_key=True)
    songTitle = models.CharField(max_length=150)
    songPath = models.FileField(upload_to='songs/')
    timeMusic = models.TimeField(null=True, blank=True)
    lyrics = models.TextField(null=True, blank=True)
    genero = models.ForeignKey(
        GeneroMusical, 
        on_delete=models.CASCADE, 
        db_column='generomusical_idgeneroMusical'
    )

    class Meta:
        db_table = 'songs'
class Playlist(models.Model):
    pk_playlistid = models.AutoField(db_column='PK_playlistID', primary_key=True)
    plname = models.CharField(db_column='plName', max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playlist'

class Users(models.Model):
    pk_userid = models.AutoField(db_column='PK_userID', primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=250, blank=True, null=True)
    senha = models.CharField(max_length=45)
    profilepicture = models.CharField(db_column='profilePicture', max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

# TABELAS INTERMEDIÁRIAS 

class Albumartist(models.Model):
    artist = models.ForeignKey(Artist, models.DO_NOTHING, db_column='artist_PK_artistID', primary_key=True)
    album = models.ForeignKey(Album, models.DO_NOTHING, db_column='album_PK_albumID')

    class Meta:
        managed = False
        db_table = 'albumartist'
        unique_together = (('artist', 'album'),)

class Albumband(models.Model):
    band = models.ForeignKey(Band, models.DO_NOTHING, db_column='band_PK_bandID', primary_key=True)
    album = models.ForeignKey(Album, models.DO_NOTHING, db_column='album_PK_albumID')

    class Meta:
        managed = False
        db_table = 'albumband'
        unique_together = (('band', 'album'),)

class Albummusica(models.Model):
    album = models.ForeignKey(Album, models.DO_NOTHING, db_column='album_PK_albumID', primary_key=True)
    songs = models.ForeignKey(Songs, models.DO_NOTHING, db_column='songs_PK_songID')

    class Meta:
        managed = False
        db_table = 'albummusica'
        unique_together = (('album', 'songs'),)

class Artistsband(models.Model):
    artist = models.ForeignKey(Artist, models.DO_NOTHING, db_column='artist_PK_artistID', primary_key=True)
    band = models.ForeignKey(Band, models.DO_NOTHING, db_column='band_PK_bandID')

    class Meta:
        managed = False
        db_table = 'artistsband'
        unique_together = (('artist', 'band'),)

class Songsplaylist(models.Model):
    playlist = models.ForeignKey(Playlist, models.DO_NOTHING, db_column='playlist_PK_playlistID', primary_key=True)
    songs = models.ForeignKey(Songs, models.DO_NOTHING, db_column='songs_PK_songID')

    class Meta:
        managed = False
        db_table = 'songsplaylist'
        unique_together = (('playlist', 'songs'),)

class Usersplaylists(models.Model):
    users = models.ForeignKey(Users, models.DO_NOTHING, db_column='users_PK_userID', primary_key=True)
    playlist = models.ForeignKey(Playlist, models.DO_NOTHING, db_column='playlist_PK_playlistID')

    class Meta:
        managed = False
        db_table = 'usersplaylists'
        unique_together = (('users', 'playlist'),)
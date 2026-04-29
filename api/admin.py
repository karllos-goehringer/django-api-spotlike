from django.contrib import admin
from .models import Artist, Band, Album, GeneroMusical, Songs, Playlist, Users, Albumartist, Albumband, Artistsband, Songsplaylist, Usersplaylists

class UsersAdmin(admin.ModelAdmin):
    list_display = ('PK_userID', 'email', 'profilepicture')
    pass
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('PK_artistID', 'name', 'description', 'imageArtist', 'backgroundImage')
    pass
class BandAdmin(admin.ModelAdmin):
    list_display = ('PK_bandID', 'name', 'description', 'imageBand', 'backgroundImage')
    pass
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('PK_albumID', 'albumName', 'releaseDate', 'albumimage')
    pass
class GeneroMusicalAdmin(admin.ModelAdmin):
    list_display = ('idgeneroMusical', 'nomeGenero')
    pass
class SongsAdmin(admin.ModelAdmin):
    list_display = ('PK_songID', 'songtitle', 'songpath', 'timeMusic', 'lyrics', 'generomusical_idgeneroMusical')
    pass
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('PK_playlistID', 'plName')
    pass
class AlbumartistAdmin(admin.ModelAdmin):
    list_display = ('album_PK_albumID', 'artist_PK_artistID')
    pass
class AlbumbandAdmin(admin.ModelAdmin):
    list_display = ('album_PK_albumID', 'band_PK_bandID')
    pass
class ArtistsbandAdmin(admin.ModelAdmin):
    list_display = ('artist_PK_artistID', 'band_PK_bandID')
    pass
class SongsplaylistAdmin(admin.ModelAdmin):
    list_display = ('playlist_PK_playlistID', 'songs_PK_songID', 'ordem')
    pass
class UsersplaylistsAdmin(admin.ModelAdmin):
    list_display = ('users_PK_userID', 'playlist_PK_playlistID')
    pass

admin.site.register(Users, UsersAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(GeneroMusical, GeneroMusicalAdmin)
admin.site.register(Songs, SongsAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Albumartist, AlbumartistAdmin)
admin.site.register(Albumband, AlbumbandAdmin)
admin.site.register(Artistsband, ArtistsbandAdmin)
admin.site.register(Songsplaylist, SongsplaylistAdmin)
admin.site.register(Usersplaylists, UsersplaylistsAdmin)
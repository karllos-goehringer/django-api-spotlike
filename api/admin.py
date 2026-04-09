from django.contrib import admin
from .models import Artist, Band, Album, GeneroMusical, Songs, Playlist, Users, Albumartist, Albumband, Albummusica, Artistsband, Songsplaylist, Usersplaylists

class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk_userid', 'email', 'profilepicture')
    pass
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('pk_artistid', 'name', 'description', 'imageartist')
    pass
class BandAdmin(admin.ModelAdmin):
    list_display = ('pk_bandid', 'name', 'description', 'imageband')
    pass
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('pk_albumid', 'albumname', 'releasedate', 'albumimage')
    pass
class GeneroMusicalAdmin(admin.ModelAdmin):
    list_display = ('idgeneroMusical', 'nomeGenero')
    pass
class SongsAdmin(admin.ModelAdmin):
    list_display = ('PK_songID', 'songTitle', 'songPath', 'timeMusic', 'lyrics','genero')
    pass
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('pk_playlistid', 'plname')
    pass
class AlbumartistAdmin(admin.ModelAdmin):
    list_display = ('album', 'artist')
    pass
class AlbumbandAdmin(admin.ModelAdmin):
    list_display = ('album', 'band')
    pass
class AlbummusicaAdmin(admin.ModelAdmin):
    list_display = ('album', 'songs')
    pass
class ArtistsbandAdmin(admin.ModelAdmin):
    list_display = ('artist', 'band')
    pass
class SongsplaylistAdmin(admin.ModelAdmin):
    list_display = ('songs', 'playlist')
    pass
class UsersplaylistAdmin(admin.ModelAdmin):
    list_display = ('users', 'playlist')
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
admin.site.register(Albummusica, AlbummusicaAdmin)
admin.site.register(Artistsband, ArtistsbandAdmin)
admin.site.register(Songsplaylist, SongsplaylistAdmin)
admin.site.register(Usersplaylists, UsersplaylistAdmin)
from django.contrib import admin
from .models import Artist, Band, Album, GeneroMusical, Songs, Playlist, Users

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

admin.site.register(Users, UsersAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(GeneroMusical, GeneroMusicalAdmin)
admin.site.register(Songs, SongsAdmin)
admin.site.register(Playlist, PlaylistAdmin)
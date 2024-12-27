from django.contrib import admin
from .models import Group, Album, Song, GroupMember


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_date')
    search_fields = ('name', 'description')
    list_filter = ('creation_date',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'release_date')
    search_fields = ('name', 'description')
    list_filter = ('release_date', 'group')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'group', 'duration')
    search_fields = ('name', 'lyrics')
    list_filter = ('album', 'group')


@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'group')
    search_fields = ('name', 'role')
    list_filter = ('group',)

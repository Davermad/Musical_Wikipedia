from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Group, Album, Song, GroupMember


def index(request):
    latest_groups = Group.objects.order_by('-id')[:5]
    latest_albums = Album.objects.order_by('-id')[:5]
    latest_songs = Song.objects.order_by('-id')[:5]

    return render(request, 'index.html', {
        'latest_groups': latest_groups,
        'latest_albums': latest_albums,
        'latest_songs': latest_songs,
    })


def search(request):
    query = request.GET.get('q', '')
    groups = Group.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    albums = Album.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    songs = Song.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    members = GroupMember.objects.filter(Q(name__icontains=query) | Q(biography__icontains=query))

    return render(request, 'search.html', {
        'query': query,
        'groups': groups,
        'albums': albums,
        'songs': songs,
        'members': members,
    })


def get_groups(request):
    groups = Group.objects.all().order_by('name')
    paginator = Paginator(object_list=groups, per_page=10)

    page = request.GET.get('page', 1)
    groups = paginator.get_page(number=page)

    context = {
        'groups': groups
    }
    return render(request=request, template_name='groups.html', context=context)


def get_group_detail(request, pk):
    group = get_object_or_404(Group, id=pk)
    albums = group.albums.all()
    songs = group.songs.all()
    members = group.members.all()

    context = {
        'group': group,
        'albums': albums,
        'songs': songs,
        'members': members
    }
    return render(request, template_name='group_detail.html', context=context)


def get_albums(request):
    albums = Album.objects.all().order_by('name')
    paginator = Paginator(object_list=albums, per_page=10)
    page = request.GET.get('page', 1)
    albums = paginator.get_page(number=page)

    context = {
        'albums': albums
    }
    return render(request, template_name='albums.html', context=context)


def get_album_detail(request, pk):
    album = get_object_or_404(Album, id=pk)
    songs = album.songs.all()

    context = {
        'album': album,
        'songs': songs
    }
    return render(request, template_name='album_detail.html', context=context)


def get_songs(request):
    songs = Song.objects.all().order_by('name')
    paginator = Paginator(object_list=songs, per_page=10)
    page = request.GET.get('page', 1)
    songs = paginator.get_page(number=page)

    context = {
        'songs': songs
    }
    return render(request, template_name='songs.html', context=context)


def get_song_detail(request, pk):
    song = get_object_or_404(Song, id=pk)

    context = {
        'song': song
    }
    return render(request, template_name='song_detail.html', context=context)


def get_member_detail(request, pk):
    member = get_object_or_404(GroupMember, id=pk)

    context = {
        'member': member
    }
    return render(request, template_name='member_detail.html', context=context)

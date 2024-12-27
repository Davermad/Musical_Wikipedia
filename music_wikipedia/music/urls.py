from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('groups/', views.get_groups, name='get_groups'),
    path('group/<int:pk>/', views.get_group_detail, name='get_group_detail'),
    path('album/<int:pk>/', views.get_album_detail, name='get_album_detail'),
    path('song/<int:pk>/', views.get_song_detail, name='get_song_detail'),
    path('member/<int:pk>/', views.get_member_detail, name='get_member_detail'),
    path('songs/', views.get_songs, name='get_songs'),
    path('albums/', views.get_albums, name='get_albums'),
]

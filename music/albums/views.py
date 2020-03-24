from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Songs


def songs_response(request, album_id):
    my_list = []
    album_view = Album.objects.get(pk=album_id)
    songs_view = Songs.objects.filter(alb=album_id)
    for i in songs_view:
        my_list.append('<br>' + i.songs_name + "- "+ "Duration - " + str(i.song_minute)+ " min")

    return HttpResponse('<b>' + album_view.album_name+ '</b>' + ''.join(my_list))

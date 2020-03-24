from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=50)

class Songs(models.Model):
    alb = models.ForeignKey(Album, on_delete=models.CASCADE)
    songs_name = models.CharField(max_length=50)
    song_minute = models.FloatField(default=0)

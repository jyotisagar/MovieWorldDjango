from django.db import models
from django.urls import reverse

class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music/detail.html', kwargs={'pk': self.pk})

    def __str__(self):
        return self.artist + '-' + self.album_title + '-' + self.genre + '-' + self.album_logo


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    file_type = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title + ' - ' + self.file_type


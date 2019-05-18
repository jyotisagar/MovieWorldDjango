from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Album, Song
# from django.template import loader
from django.shortcuts import render, get_object_or_404
# from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    context = {"all_albums": all_albums}
    return render(request, 'music/index.html', context)


def details(request, id):
    album = get_object_or_404(Album, pk=id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, id):
    album = get_object_or_404(Album, pk=id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',
                      {
                         'album': album,
                         'error_msg': 'Select a valid song!'
                      })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})


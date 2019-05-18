from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Album
# from django.template import loader
from django.shortcuts import render
from django.http import Http404

def index(request):
    all_albums = Album.objects.all()
    context = {"all_albums": all_albums}
    return render(request, 'music/index.html', context)




def details(request, id):
    try:
        album = Album.objects.get(pk=id)
    except Album.DoesNotExist:
        raise Http404('Album does not exist!')
    return render(request, 'music/detail.html', {'album': album})


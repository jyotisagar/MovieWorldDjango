from django.views import generic
from .models import Album, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import TemplateView
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class  UserFormView(TemplateView):
    form_class = UserForm
    template_name = 'music/register_form.html'

    # display blank form
    def get(self, request):
      form = self.form_class(None)
      return render(request, self.template_name, {'form': form})


    # process form data
    def post(self, request):
      form = self.form_class(request.POST)
      if form.is_valid():
          user = form.save(commit=False)
          # clean normalized data
          username = form.cleaned_data['username']
          password = form.cleaned_data['password']
          user.set_password(password)
          user.save()
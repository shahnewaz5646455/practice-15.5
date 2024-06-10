from django.shortcuts import render, redirect
from . import froms
from . import models
# Create your views here.

def add_album(request):
    if request.method=='POST':
        album_form = froms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            album_form = froms.AlbumForm()
    else:
        album_form = froms.AlbumForm()
    return render(request, 'add_album.html', {'form' : album_form})


def edit(request, id):
    album=models.Album.objects.get(pk=id)
    album_form = froms.AlbumForm(instance=album)

    if request.method=='POST':
        album_form = froms.AlbumForm(request.POST,instance=album)

        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    

    return render(request, 'add_album.html', {'form' : album_form})
def delete(request, id):
    album=models.Album.objects.get(pk=id)
    album.delete()
    return redirect('home')

    
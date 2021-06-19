from django.shortcuts import render, get_object_or_404
from .models import Album
from .forms import AlbumForm

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_detail(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'albums': albums})

def album_new(request):
    form = AlbumForm()
    return render(request, 'albums/album_edit.html', {'form': form})
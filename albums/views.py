from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm
from django.utils import timezone

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_detail(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'albums': albums})

def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.created_date = timezone.now()
            album.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'albums/album_edit.html', {'form': form})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.created_date = timezone.now()
            album.save()
            return redirect('post_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album_edit.html', {'form': form})

# below version gives me a form but does redirect to album list
# def album_new(request):
    if request.method == "POST":
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='album_list')
    
    return render(request, 'albums/album_edit.html', {'form': form})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_album, name='list_album'),
    path('/albums/new', views.new_album, name='new_album'),
    path('/albums/<int:pk>/edit', views.edit_album, name='edit_album'),
    path('/albums/<int:pk>/delete', views.delete_album, name='delete_album'),
]
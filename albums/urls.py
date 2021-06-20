from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/new/', views.album_new, name='album_new'),
    path('albums/<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('albums/<int:pk>/delete', views.album_delete, name='album_delete'),
]
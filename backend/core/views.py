from django.shortcuts import render
from rest_framework import viewsets
from .models import Song, ArtistProfile, Download
from .serializers import SongSerializer, ArtistSerializer, DownloadSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistSerializer


class DownloadViewSet(viewsets.ModelViewSet):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer

# Create your views here.

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')

        songs = Song.objects.filter(
            Q(title__icontains=query) |
            Q(genre__icontains=query) |
            Q(artist__stage_name__icontains=query)
        )

        serializer = self.get_serializer(songs, many=True)
        return Response(serializer.data)
        
        
@action(detail=False, methods=['get'])
def trending(self, request):
    songs = Song.objects.all().order_by('-plays', '-downloads')[:20]
    serializer = self.get_serializer(songs, many=True)
    return Response(serializer.data)
    
@action(detail=True, methods=['post'])
def play(self, request, pk=None):
    song = self.get_object()
    song.plays += 1
    song.save()
    return Response({"message": "play recorded"})

from django.shortcuts import render

def home(request):
    return render(request, "index.html")

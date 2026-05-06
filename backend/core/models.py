from django.db import models
from django.contrib.auth.models import User


class ArtistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.stage_name


class Song(models.Model):
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/')
    audio_file = models.FileField(upload_to='songs/')
    is_royalty_free = models.BooleanField(default=True)
    downloads = models.IntegerField(default=0)
    plays = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Download(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    downloaded_at = models.DateTimeField(auto_now_add=True)

# Create your models here.

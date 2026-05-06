from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, ArtistViewSet, DownloadViewSet

router = DefaultRouter()
router.register('songs', SongViewSet)
router.register('artists', ArtistViewSet)
router.register('downloads', DownloadViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

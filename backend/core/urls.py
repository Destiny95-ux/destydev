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

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),

]

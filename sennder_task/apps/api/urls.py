"""Api urls file."""
from django.urls import path
from apps.api.views import MovieListTemplateView, MovieListAPIView

urlpatterns = [
    path("movies/", MovieListTemplateView.as_view(), name="movies"),
    path("movies-api/", MovieListAPIView.as_view(), name="movies-api"),
]

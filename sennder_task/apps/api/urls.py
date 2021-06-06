"""Api urls file."""
from django.urls import path
from apps.api.views import MovieListTemplateView, MovieListAPIView

urlpatterns = [
    # show movie list in the give template file
    path("movies/", MovieListTemplateView.as_view(), name="movies"),
    # show movie list in the json format
    path("movies-api/", MovieListAPIView.as_view(), name="movies-api"),
]

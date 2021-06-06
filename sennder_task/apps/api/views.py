"""Api views file."""
from rest_framework.generics import ListAPIView
from apps.api.serializers import MovieSerializer
from apps.api.models import Movie
from rest_framework import permissions
from apps.pagination import StandardResultsSetPagination
from django.views.generic.list import ListView
from sennder_task.settings import PAGE_SIZE


class MovieListAPIView(ListAPIView):
    """Movie list api view class.

    A HTTP api endpoint which shows the paginated movie list along with people in it.

    Parameters
    ----------
    ListAPIView : rest_framework.generics
    """

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.AllowAny]


class MovieListTemplateView(ListView):
    """Movie list template view class.

    View for viewing the paginated movie data along with people in it.

    Parameters
    ----------
    ListView : django.views.generic.list
    """

    model = Movie
    template_name = 'movies_list.html'
    context_object_name = 'movies'
    paginate_by = PAGE_SIZE
    queryset = Movie.objects.all()

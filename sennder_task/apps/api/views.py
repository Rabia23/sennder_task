"""Api views file."""
from django.views.generic.list import ListView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.models import Movie
from apps.api.serializers import MovieSerializer
from apps.api.tasks import update_db
from apps.pagination import StandardResultsSetPagination
from sennder_task.settings import PAGE_SIZE


@swagger_auto_schema(
    request_body=MovieSerializer, responses={"200": MovieSerializer}
)
class MovieListAPIView(ListAPIView):
    """Movie list api view class.

    A HTTP api endpoint which shows the paginated movie list
    along with people in it.

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
    template_name = "movies_list.html"
    context_object_name = "movies"
    paginate_by = PAGE_SIZE
    queryset = Movie.objects.all()


class RunCeleryTaskView(APIView):
    def get(self, request, format=None):
        print(update_db.name)
        update_db.delay()
        return Response("Task will run shortly", status=status.HTTP_204_NO_CONTENT)

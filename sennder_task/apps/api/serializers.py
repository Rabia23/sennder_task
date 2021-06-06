"""Api serializers file."""
from rest_framework import serializers

from apps.api.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Movie serializer class.

    Parameters
    ----------
    serializers : rest_framework
    """

    # use the `name` field of the people model using relationship
    people = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:  # noqa: D106
        model = Movie
        fields = (
            "key",
            "title",
            "director",
            "producer",
            "release_date",
            "people",
        )

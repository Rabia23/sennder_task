"""Api admin file."""
from django.contrib import admin

from apps.api.models import Movie, People


class MovieAdmin(admin.ModelAdmin):
    """Movie model admin.
/Users/rabia/Downloads/sennder_hometask/sennder_task/apps/api/admin.py
    Parameters
    ----------
    admin : django.contrib
    """

    list_display = ("id", "key", "title")


admin.site.register(Movie, MovieAdmin)


class PeopleAdmin(admin.ModelAdmin):
    """People model admin.

    Parameters
    ----------
    admin : django.contrib
    """

    list_display = ("id", "key", "name")


admin.site.register(People, PeopleAdmin)

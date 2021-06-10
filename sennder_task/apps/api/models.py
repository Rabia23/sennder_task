"""Api models file."""
from django.db import models
from django.utils.translation import ugettext as _


class Movie(models.Model):
    """Movie model class.

    Parameters
    ----------
    models : django.db
    """

    key = models.CharField(
        _("key"), max_length=100, db_index=True, unique=True
    )
    title = models.CharField(_("title"), max_length=150, blank=True)
    director = models.CharField(_("director"), max_length=150, blank=True)
    producer = models.CharField(_("producer"), max_length=150, blank=True)
    release_date = models.PositiveIntegerField(
        _("release_date"), null=True, blank=True
    )
    created_at = models.DateField(
        _("created_at"),
        auto_now_add=True,
        help_text=_("the date when movie was created"),
    )

    class Meta:  # noqa: D106
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self):
        """Str representation of movie model.

        Returns
        -------
        str
            containing key and title of the given object
        """
        return f"{self.key}-{self.title}"


class People(models.Model):
    """People model class.

    Parameters
    ----------
    models : django.db
    """

    key = models.CharField(
        _("key"), max_length=100, db_index=True, unique=True
    )
    name = models.CharField(_("name"), max_length=150, blank=True)
    gender = models.CharField(_("gender"), max_length=10, blank=True)
    age = models.CharField(_("age"), max_length=50, blank=True)
    movies = models.ManyToManyField(Movie, related_name="people")
    created_at = models.DateField(
        _("created_at"),
        auto_now_add=True,
        help_text=_("the date when people was created"),
    )

    class Meta:  # noqa: D106
        verbose_name = "people"
        verbose_name_plural = "people"

    def __str__(self):
        """Str representation of people model.

        Returns
        -------
        str
            containing key and name of the given object
        """
        return f"{self.key}-{self.name}"

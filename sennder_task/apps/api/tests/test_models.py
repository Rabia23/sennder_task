"""Models test cases."""
from django.db.utils import DataError, IntegrityError
from django.test import TransactionTestCase

from apps.api.models import Movie


class MovieTestCase(TransactionTestCase):
    """Movie model test cases.

    Parameters
    ----------
    TransactionTestCase : django.test
    """

    def test_creates_row_with_valid_data(self):
        """Test that row with the valid data successfully
        added in the database.
        """
        movie_obj = {
            "key": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
            "title": "Castle in the Sky",
            "director": "Hayao Miyazaki",
            "producer": "Isao Takahata",
            "release_date": "1986",
        }
        movie = Movie.objects.create(**movie_obj)
        # assert that one record is added in the db
        self.assertEqual(Movie.objects.count(), 1)
        # assert that movie's title inserted in the db is same as
        # movie_obj title
        self.assertEqual(movie.title, "Castle in the Sky")

    def test_no_row_created_with_invalid_data(self):
        """Test that row with the invalid data doesn't added
        in the database.
        """
        movie_obj = {
            "key": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
            "title": "Castle in the Sky",
            "director": "Hayao Miyazaki",
            "producer": "Isao Takahata",
            "release_date": "-1980",
        }
        expected_error_message = (
            "Out of range value for column 'release_date' at row 1"
        )
        with self.assertRaisesRegexp(DataError, expected_error_message):
            Movie.objects.create(**movie_obj)
        # assert that no record is added in the db
        self.assertFalse(Movie.objects.exists())

    def test_no_row_created_with_duplicate_key(self):
        """Test that row with the duplicate key doesn't added
        in the database.
        """
        movie_obj = {
            "key": "12cfb892-aac0-4c5b-94af-521852e46d6a",
            "title": "Grave of the Fireflies",
            "director": "Hayao Miyazaki",
            "producer": "Isao Takahata",
            "release_date": "1988",
        }
        Movie.objects.create(**movie_obj)
        # assert that one record is added in the db
        self.assertEqual(Movie.objects.count(), 1)

        # create record with the same key raises duplicate entry error
        expected_error_message = (
            "Duplicate entry '12cfb892-aac0-4c5b-94af-521852e46d6a' for key 'api_movie.key'"
        )
        with self.assertRaisesRegexp(IntegrityError, expected_error_message):
            Movie.objects.create(**movie_obj)
        # assert that no new record is added in the db
        self.assertEqual(Movie.objects.count(), 1)


class PeopleTestCase(TransactionTestCase):
    """People model test cases.

    Parameters
    ----------
    TransactionTestCase : django.test
    """
    # will be added later

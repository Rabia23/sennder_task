"""Views test cases."""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.api.models import Movie, People


class MovieListAPIViewTestCase(TestCase):
    """Movie list api view test cases.

    Parameters
    ----------
    TestCase : django.test
    """

    def setUp(self):
        """Set up the api url for each test case."""
        self.url = reverse("movies-api")

    def prepare_data(self):
        """Add movies and people data in the database."""
        movies_list = [
            {
                "key": "111",
                "title": "fault in our stars",
                "director": "noor khan",
                "producer": "ali saeed",
                "release_date": 1987,
            },
            {
                "key": "222",
                "title": "cindrella",
                "director": "noor khan",
                "producer": "ali saeed",
                "release_date": 2001,
            },
        ]
        people_list = [
            {
                "key": "123",
                "name": "pum pum",
                "gender": "male",
                "age": "32",
            },
            {
                "key": "456",
                "name": "rum rum",
                "gender": "female",
                "age": "28",
            },
        ]
        # insert movies
        for movie in movies_list:
            Movie.objects.create(**movie)
        # get all the movies from db for movie/people relationship
        movies = list(Movie.objects.all())
        # insert people
        for people in people_list:
            p = People.objects.create(**people)
            # assign movie to the given people
            p.movies.add(*movies)

    def test_http_codes(self):
        """Test allowed or disallowed methods on the given url."""
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = self.client.post(self.url)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        res = self.client.put(self.url)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        res = self.client.delete(self.url)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_empty_database_returns_empty_list(self):
        """Test that url returns empty list if there is no data
        in the database.
        """
        res = self.client.get(self.url)
        self.assertEqual(res.json()["results"], [])

    def test_results_with_all_elements(self):
        """Test that url returns all elements from the database."""
        # insert data in the database
        self.prepare_data()
        res = self.client.get(self.url)
        # assert that api returns all the records from the db
        self.assertEqual(res.json()["count"], 2)
        # assert the title of first movie
        self.assertEqual(
            res.json()["results"][0]["title"], "fault in our stars"
        )
        # assert the people of first movie
        self.assertEqual(
            res.json()["results"][0]["people"], ["pum pum", "rum rum"]
        )
        # assert the title of second movie
        self.assertEqual(res.json()["results"][1]["title"], "cindrella")
        # assert the people of second movie
        self.assertEqual(
            res.json()["results"][1]["people"], ["pum pum", "rum rum"]
        )

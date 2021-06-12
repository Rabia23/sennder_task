"""Api tasks file."""
from celery.utils.log import get_task_logger

from apps.api.models import Movie, People
from apps.utils import make_request
from sennder_task.celery import app
from sennder_task.settings import FILMS_URL, PEOPLE_URL, READ_LIMIT

logger = get_task_logger(__name__)


def get_movies_keys_from_urls(movies_list):
    """
    Extract the movies keys from the list of movies urls.

    Parameters
    ----------
    movies_list : list
        list containing of movies urls

    Returns
    -------
    list[str]
        returns list of containing movies keys
        e.g returns "2baf70d1-42bb-4437-b551-e5fed5a87abe" from url
        "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"  # noqa:501
    """
    return [m.split("/")[-1] for m in movies_list]


def get_new_movies_keys(old_keys, current_keys):
    """
    Create a list of new movies keys which needs to be linked with the given
    people in the database.

    Parameters
    ----------
    old_keys : list[str]
        movies keys already exist in the database
    current_keys : list[str]
        movies keys fetch from the current request

    Returns
    -------
    list[str]
        returns list of new movies keys that needs to be linked with people
        in the database
    """
    new_keys = []
    for key in current_keys:
        if key not in old_keys:
            new_keys.append(key)
    return new_keys


def get_existing_movies_per_people():
    """
    Get all the poeple keys along with the movie keys from the database.

    The purpose of this function is to get the people data along with movies
    at once to save the multiple database calls per people with the movies
    attached to it.


    Returns
    -------
    dict
        returns the dict consists of `people_key` as a key with the list of
        `movies_keys` as a value
    """
    existing_ppl_with_movies = {}
    for obj in People.objects.values("key", "movies__key"):
        if obj.get("key") in existing_ppl_with_movies:
            existing_ppl_with_movies[obj.get("key")].append(
                obj.get("movies__key")
            )
        else:
            existing_ppl_with_movies[obj.get("key")] = [obj.get("movies__key")]

    return existing_ppl_with_movies


def assign_movies_to_people(people_obj, movies_keys):
    """
    Assign movies to the given people.

    It establishes the relationship between all the movies in the given
    `movies_keys` list with the given people in the database.

    Parameters
    ----------
    people_obj : apps.api.models.People
    movies_keys : list[str]
    """
    movies = Movie.objects.filter(key__in=movies_keys)
    people_obj.movies.add(*movies)


def fetch_and_save_movies():
    """
    Fetch the movies with the given URL and params and save in the database.

    If the movie doesn't exist, creates a new one otherwise skips it.
    """
    movies_keys = []
    # db is not empty
    if Movie.objects.exists():
        # fetch all the movies keys from the db
        movies_keys = list(Movie.objects.values_list("key", flat=True))

    params = {
        "limit": READ_LIMIT,
        "fields": "id,title,director,producer,release_date",
    }
    # fetch the movies data from the url
    results = make_request(url=FILMS_URL, params=params)

    for obj in results:
        key = obj.pop("id")
        # if movie doesn't exist in db, save it
        if key not in movies_keys:
            try:
                movie = Movie.objects.create(key=key, **obj)
            except Exception:
                logger.exception(f"unable to insert movie: {obj}")
            else:
                logger.info(f"movie inserted: {movie.id}-{obj}")


def fetch_and_save_people():
    """
    Fetch the people with the given URL and params and save in the database.

    If people don't exist, creates a new one and attach movies with it. If
    people already exist, checks whether the new movie is added to it or not.
    If added then attach that movie to the existing people.
    """
    # get the existing people along with movies from the db
    existing_ppl_with_movies = get_existing_movies_per_people()

    params = {"limit": READ_LIMIT, "fields": "id,name,gender,age,films"}
    # fetch the people data from the url
    results = make_request(url=PEOPLE_URL, params=params)

    for obj in results:
        key = obj.pop("id")
        movies_list = obj.pop("films")
        # get the movies keys from the list of movies urls
        current_keys = get_movies_keys_from_urls(movies_list)
        # if people already exist in db
        if key in existing_ppl_with_movies:
            # get the new movies keys that needs to be added in db
            new_movies_keys = get_new_movies_keys(
                old_keys=existing_ppl_with_movies.get(key),
                current_keys=current_keys,
            )
            if new_movies_keys:
                people = People.objects.get(key=key)
                # associate movies to the existing people
                assign_movies_to_people(
                    people_obj=people, movies_keys=new_movies_keys
                )
                logger.info(
                    f"movies: {new_movies_keys} have been assigned to people: {people.key}"  # noqa:501
                )
        else:
            # if people don't exist in db, save it
            try:
                people = People.objects.create(key=key, **obj)
            except Exception:
                logger.exception(f"unable to insert people: {obj}")
            else:
                logger.info(f"people inserted: {people.id}-{obj}")
                # associate movies to the new created people
                assign_movies_to_people(
                    people_obj=people, movies_keys=current_keys
                )
                logger.info(
                    f"movies: {current_keys} have been assigned to people: {people.key}"  # noqa:501
                )


@app.task
def update_db():
    """
    Scheduled task that updates the database after every minute.

    It does the following tasks:
    - fetches the movies with the given URL and params. If the movie doesn't
    exist, creates a new one otherwise skips it.
    - fetches the people with the given URL and params. If people don't exist,
    creates a new one and associates movies with it.
    - If people already exist, it checks whether the new movie is added to it
    or not. If added then associate that movie to the existing people.
    """
    fetch_and_save_movies()
    fetch_and_save_people()

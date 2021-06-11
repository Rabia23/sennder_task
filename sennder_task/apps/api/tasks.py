from celery.utils.log import get_task_logger
from apps.utils import make_request
from sennder_task.settings import FILMS_URL, PEOPLE_URL, READ_LIMIT
from apps.api.models import Movie, People
from sennder_task.celery import app

logger = get_task_logger(__name__)


def get_films_keys(films_list):
    return [f.split("/")[-1] for f in films_list]


def get_new_keys(old_keys, current_keys):
    new_keys = []
    for key in current_keys:
        if key not in old_keys:
            new_keys.append(key)
    return new_keys


def get_existing_films_per_people():
    existing_ppl_with_films = {}
    for obj in People.objects.values("key", "movies__key"):
        if obj.get("key") in existing_ppl_with_films:
            existing_ppl_with_films[obj.get("key")].append(obj.get("movies__key"))
        else:
            existing_ppl_with_films[obj.get("key")] = [obj.get("movies__key")]
    return existing_ppl_with_films


def assign_movies_to_people(people_obj, movies_keys):
    movies = Movie.objects.filter(key__in=movies_keys)
    people_obj.movies.add(*movies)


def fetch_and_save_movies():
    movies_keys = []
    if Movie.objects.exists():  # database is not empty
        # fetch all the movies keys from the database
        movies_keys = list(Movie.objects.values_list("key", flat=True))
    params = {
        "limit": READ_LIMIT,
        "fields": "id,title,director,producer,release_date"
    }
    results = make_request(url=FILMS_URL, params=params)
    for obj in results:
        key = obj.pop("id")
        # if movie doesn't exist in database, save it
        if key not in movies_keys:
            try:
                movie = Movie.objects.create(key=key, **obj)
            except Exception:
                logger.exception(f"unable to insert movie: {obj}")
            else:
                logger.info(f"movie inserted: {movie.id}-{obj}")


def fetch_and_save_people():
    existing_ppl_with_films = get_existing_films_per_people()
    params = {
        "limit": READ_LIMIT,
        "fields": "id,name,gender,age,films"
    }
    results = make_request(url=PEOPLE_URL, params=params)
    for obj in results:
        key = obj.pop("id")
        films_list = obj.pop("films")
        current_keys = get_films_keys(films_list)
        if key in existing_ppl_with_films:
            new_movie_keys = get_new_keys(old_keys=existing_ppl_with_films.get(key), current_keys=current_keys)
            if new_movie_keys:
                people = People.objects.get(key=key)
                assign_movies_to_people(people_obj=people, movies_keys=new_movie_keys)
                logger.info(f"movies: {new_movie_keys} have been assigned to people: {people.key}")
        else:
            # if ppl doesn't exist in database, save it
            try:
                people = People.objects.create(key=key, **obj)
            except Exception:
                logger.exception(f"unable to insert people: {obj}")
            else:
                logger.info(f"people inserted: {people.id}-{obj}")
                assign_movies_to_people(people_obj=people, movies_keys=current_keys)
                logger.info(f"movies: {current_keys} have been assigned to people: {people.key}")


@app.task
def update_db():
    fetch_and_save_movies()
    fetch_and_save_people()

## Task Summary:
The task contains the below mentioned endpoints:
- a GET '/movies'
- a GET '/movies-api'

Both APIs are built in Python Django framework which is capable of returning paginated data from
the Ghibli API. Data is being fetched from API after every minute using scheduled celery task.

The `movies` endpoint returns a simple page containing a plain list of all movies along with the people that
appear in it.

The `movies-api` endpoint is a REST API that uses simple page number based style that helps you manage the paginated data using page numbers in the request query parameters.


## Project Structure (App Based):
```bash
Studio-Ghibli-Nhedwx/
├── README.md
├── .gitignore
└── senndertask
    ├── Makefile
    ├── apps
    │   ├── __init__.py
    │   ├── api
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── migrations
    │   │   │   ├── 0001_initial.py
    │   │   │   ├── 0002_auto_20210610_1605.py
    │   │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   ├── serializers.py
    │   │   ├── tasks.py
    │   │   ├── tests
    │   │   │   ├── __init__.py
    │   │   │   ├── test_models.py
    │   │   │   └── test_views.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── pagination.py
    │   └── utils.py
    ├── conf
    │   └── init.sql
    ├── manage.py
    ├── requirements.txt
    ├── senndertask
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── celery.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── templates
        └── movies_list.html
```

### Python Libraries/Frameworks used:
-  **django** - This is a Python-based open-source web framework that follows the model-template-view
architectural pattern.
-  **djangorestframework** - This is a powerful and flexible toolkit built on top of the Django web framework
for building REST APIs.
-  **mysqlclient** - MySQL database connector for Python.
-  **drf-yasg** - This is a Swagger generation tool provided by Django Rest Framework that allow you
to build API documentation.
- **requests** - This is a python library to make calls to external APIs.
- **celery** - This is a task queue with focus on real-time processing, while also supporting task scheduling.
- **django-celery-beat** - This extension stores the schedule in the Django database, and presents a convenient admin interface to manage periodic tasks at runtime.
- **redis** - This is a message broker. It handles the queue of "messages" between Django and Celery. 
-  **black** - This is Python code formatter that formats code adhering to PEP8 standards.

### Prerequisite
- Make sure you have Python and Mysql installed in your system :)

**Note:** Python 3.6.0 is used for the task.

### How to start application (using Virtual Environment)

- Clone the project using command:
```
git clone http://sennder-jejaun@git.codesubmit.io/sennder/studio-ghibli-nhedwx
```

- Setup mysql database (mac OS):
```
mysql -V (check version)
rabia@Rabias-MacBook-Pro studio-ghibli-nhedwx % mysql -V
mysql  Ver 8.0.19 for osx10.15 on x86_64 (Homebrew)

mysql.server status (check the mysql status)
rabia@Rabias-MacBook-Pro studio-ghibli-nhedwx % mysql.server status
SUCCESS! MySQL running (9963)

mysql.server start (run the mysql server)
rabia@Rabias-MacBook-Pro studio-ghibli-nhedwx % mysql.server start
Starting MySQL
.. SUCCESS!

mysql.server stop (stop the mysql server)
rabia@Rabias-MacBook-Pro studio-ghibli-nhedwx % mysql.server stop
Shutting down MySQL
.. SUCCESS!

mysql -u root -p (login into mysql server)
rabia@Rabias-MacBook-Pro studio-ghibli-nhedwx % mysql -u root -p
Enter password: root

create databases and database user
mysql> source /Users/rabia/Downloads/studio-ghibli-nhedwx/senndertask/conf/init.sql (absolute path to init.sql file)  

mysql> show databases;
mysql> select Host, User from mysql.user;
mysql> use sennderdb;
mysql> show tables; (it doesn't have any tables right now. We will create it later)
mysql> exit
```

- Create and activate the virtual environment:
```
python3 -m venv env
source env/bin/activate
```

- Go into the project directory:
```
cd senndertask
```

- Install project requirements:
```
make install-requirements
```

- Create database tables:
```
make migrate
```

- Show database migrations:
```
make showmigrations
```

- Run the application by the following command:
```
make start-server
```

- Open a new tab and start the redis server:
```
make start-redis
```

- Open a new tab and start the celery worker (make sure virtual env is active):
```
make start-celeryworker
```

- Open another new tab and start the celery beat (make sure virtual env is active):
```
make start-celerybeat
```
**Note**: The `update_db` scheduled task updates the database after every minute.

### How to run django admin

- Create application super user:
```
make create-superuser
```

- Run the django admin by entering following command in the browser:
```
localhost:8080/admin
```

Enter the credentials that you have created above using command and you are good to go.

### How to run application unittests

- Run the command to run the all unittests of the application:
```
make tests
```
**Note:** The tests command uses the --keepdb option. It preserves the test database between test runs. It skips the create and destroy actions which can greatly decrease the time to run tests.

### Different ways to test the API

- How to test APIs using Browser:
    ```
    http://localhost:8080/movies/

    http://localhost:8080/movies-api/

    ```

- How to test `movies-api` endpoint using Swagger UI:
	- Hit the url in the browser:
		```
		localhost:8080/api-docs/
		```

- How to test `movies-api` endpoint using CURL:
    ```
    curl -X GET "http://localhost:8080/movies-api/" -H  "accept: application/json"
    ```

#### Things that are not included in the task due to time constraints and make the task easy to review from reviewer's perspective:
- API authentication is not added. The API endpoints are public.
- Database credentials are directly added in the settings.py file. It should be confidential from a security perspective.
- Python logs are being displayed on the console instead of file for the sake of simplicity.
- Using DEBUG=TRUE for debugging purpose. It shows the whole traceback of the exception. For development purpose it's fine but on production, its value should be FALSE.
- HTML page containing movies is a plain page without any styling.
- For now, reading only 250 records from the Ghibli APIs in one go. I couldn't find any pagination in that APIs. If data is paginated there, then we need to read the records in chunks using iteration.
- Covered most of the test cases but couldn't add people model and API paginated data test cases because of the time issue. People test cases are almost the same as movie model test cases and for API paginated data test cases, we need to add more records in our test to apply the pagination on it.
- Didn't add retry functionality to retry the APIs on failure. As we are mimicking a real-time behaviour by calling our APIs after a min, so it will be fine for now.
- Didn’t include Docker stuff because it requires more time to step up things.
- Didn't add any custom exception handling in our APIs. Exception handling is handled by the built-in classes from which we are inherited our views.
- As we are fetching the records from the external APIs and save them in our database. To save multiple database calls, I fetch the relevant data from the database at the start of the task at once and compares it with current request data. The data we are fetching is properly indexed so retrieval is faster.
We can implement a cache to save this database call as well and compare the current request data with the cached data instead of hitting the database.
- Update movie/people functionality is not implemented which means if anything change in the `movies/people` data in Ghibli APIs, the record will not be updated in the database.

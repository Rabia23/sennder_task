### Objective

Welcome to the sennder Coding Challenge! Studio Ghibli is a Japanese movie company. They offer a ​[REST API](https://ghibliapi.herokuapp.com/) ​where one can query information about movies and people (characters). The task is to write a Python application which serves a page on localhost:8000/movies/.

### Brief

This page should contain a plain list of all movies from the Ghibli API. For each movie the people that appear in it should be listed.

Do not use the ​**people** ​field on the ​**/films​** endpoint, since it’s broken. There is a list field called **films** ​on the ​**/people** ​endpoint which you can use to get the relationship between movies and the people appearing in them. You don’t have to worry about the styling of that page.

Since accessing the API is a time-intensive operation, it should not happen on every page load. But on the other hand, movie fans are a very anxious crowd when it comes to new releases, so **make sure that the information on the page is not older than 1 minute** when the page is loaded.

Write **unit tests** for your business logic. Your tests don’t have to be complete, but you should describe how you would extend them if you had the time.

If you have to skip some important work due to time limitations, feel free to add a short description of what you would improve and how if you had the time for it.

### Evaluation Criteria

-   Python best practices
-   Show us your work through your commit history
-   We're looking for you to produce working code, with enough room to demonstrate how to structure components in a small program
-   Completeness: did you complete the features?
-   Correctness: does the functionality act in sensible, thought-out ways?
-   Maintainability: is it written in a clean, maintainable way?
-   Testing: is the system adequately tested?
-   Formating/Code style: Are you following **PEP8** conventions?

### CodeSubmit

Please organize, design, test and document your code as if it were
going into production - then push your changes to the master branch.

Happy Coding ✌️

The sennder Team


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
will do later

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
mysql> source /Users/rabia/Downloads/sennder_hometask/sennder_task/conf/init.sql (absolute path to init.sql file)

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
cd sennder_task
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
Enter the credentials that you have created above using command and you are good to go.
```

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


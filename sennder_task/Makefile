install-requirements:  ## install application requirements
	pip install -r requirements.txt

start-server: ## run django application on specific port
	python manage.py runserver 8080

tests: ## run all unittests
	python manage.py test --keepdb

showmigrations: ## show database migrations
	python manage.py showmigrations

makemigrations: ## make database migrations
	python manage.py makemigrations

migrate: ## push migrations into the database
	python manage.py migrate

create-superuser: ## create super user for django admin
	python manage.py createsuperuser

start-celeryworker: ## start celery worker to process task
	celery -A sennder_task worker -l info

start-celerybeat: ## start celery beat to run scheduled task
	celery -A sennder_task beat -l info

start-redis: ## start redis server
	redis-server

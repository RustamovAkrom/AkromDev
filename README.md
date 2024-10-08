![img](/logo.png)
# AkromDev
---
~~~txt
Adevanced django project creating on HTML, CSS, JavaScript, Django, Django DRF.
~~~
# Technologies Django Project:
## Gunicorn, Nginx, Celery, Redis, Docker, PostgreSQL, sqlite3, Dj-Database-url, GraphQL, ElasticSearch, Markdown2.


## Start project:
#### create `envs/.env` file and send it is configurations.
~~~sh
#!/bin/bash

#### YOUR SECRET KEY ####
SECRET_KEY = "SECRET_KEY" # your django secret key

#### SETTINGS MODE ####
MODE = "development" # 'development' or 'production' 

#### EMAIL HOST ####
EMAIL_HOST_USER = "EMAIL_HOST_USER" # your email address
EMAIL_HOST_PASSWORD = "EMAIL_HOST_PASSWORD" # your email address password


#### DATABASE POSTGRESQL ####
NAME = "NAME" # database name
USER = "USER" # database user 
PASSWORD = "PASSWORD" # database password
HOST = "localhost" # default
PORT = "5432" # default

~~~

#### Install packages in virutal environment.
Windows:
~~~cmd
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
~~~

Linux:
~~~
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
~~~
Run:
~~~sh
python manage.py collectstatic
python manage.py makemigrations 
python manage.py migrate
python manage.py createadmin # create superuser 
python manage.py runserver
~~~
Runing on host [127.0.0.1:8000](http://127.0.0.1:8000/)

## Activate Celery and Redis

### Redis
Linux or Ubuntu on windows:
~~~sh
sudo systemctl start redis-server
sudo systemctl enable redis-server
sudo systemctl status redis-server
~~~

### Celery
---
Celery worker:
~~~sh
celery -A core worker --loglevel=info
~~~

Celery Beat:
~~~sh
celery -A core beat --loglevel=info
~~~

Celery Flower:
~~~sh
celery -A core flower
~~~
Web-interfays flower on brauzer [http://localhost:5555](http://localhost:5555).
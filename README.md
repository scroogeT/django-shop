# Simple online bookstore
Writen with Django 1.11 and PostgreSQL 9.5.6

![alt text](https://raw.githubusercontent.com/ruthus18/django-shop/master/screenshot.png)
=============================

## Installation:

1. Create virtualenv and install dependencies:

  ```
  pip install -r requirements.txt
  ```

2. Set up database and create in project root file "secrets.json" containing something like:

  ```
  {
    "secret_key": "abc",
    "db_name": "book_shop",
    "db_user": "user",
    "db_password": "password",
    "db_host": "localhost",
    "db_port": "5432"
  }
  ```
  
3. Modify in "django_shop/settings.py" allowed hosts:
  
  ```
  ALLOWED_HOSTS = ['projects', '127.0.0.1']
  ```
  
4. Apply migrations and create superuser:
  
  ```
  python manage.py migrate
  python manage.py createsuperuser
  ```
  
5. Run
  * via development Django Web-server:
  
  ```
  python manage.py renserver
  ```
  
  * or via WSGI HTTP server:
  
  ```
  gunicorn django_shop.wsgi:application --bind 127.0.0.1:8000
  ```
  

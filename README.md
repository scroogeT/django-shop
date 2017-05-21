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
3. 

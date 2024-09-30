# Django Project Structure

A Django project consists of multiple applications and configuration information.

1. Create a new Django project

   ```bash
   django-admin startproject FirstProject
   ```

   Directory structure:

   ```
   FirstProject
   ├── manage.py (to run server, to create application)
   └── FirstProject
       ├── settings.py
       ├── urls.py
       ├── wsgi.py
       ├── asgi.py
       └── __init__.py
   ```

2. Run the Django server

   ```bash
   python manage.py runserver
   ```

   (default port number 8000)

   Access the server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

3. Creation of the first application

   Command:
   ```bash
   python manage.py startapp appname
   ```

   Example:
   ```bash
   python manage.py startapp testapp
   ```

   Directory structure after creating `testapp`:

   ```
   C:.
   ├── db.sqlite3
   ├── manage.py
   └── FirstProject
       ├── asgi.py
       ├── settings.py
       ├── urls.py
       ├── wsgi.py
       └── __init__.py
       └── __pycache__
           ├── settings.cpython-311.pyc
           ├── urls.cpython-311.pyc
           ├── wsgi.cpython-311.pyc
           └── __init__.cpython-311.pyc
   └── testapp
       ├── admin.py
       ├── apps.py
       ├── models.py
       ├── tests.py
       ├── views.py
       └── __init__.py
       └── migrations
           └── __init__.py
   ```

### Components of the `testapp` Directory

```
testapp
├── admin.py       --> Model concept and admin configuration
├── apps.py        --> Application-specific configurations
├── models.py      --> To define model class
├── tests.py       --> To write test cases
```
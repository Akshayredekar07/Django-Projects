# Creating a Django Project and Application

## Step 1: Create a Django Project
Open your terminal and run:
```bash
django-admin startproject FirstProject
```

## Step 2: Create an Application
Navigate to your project directory:
```bash
cd FirstProject
```
Then create your application:
```bash
python manage.py startapp testapp
```

## Step 3: Add Application to settings.py
Open `settings.py` located in the `FirstProject` folder and add your application to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "testapp",  # Add your application here
]
```

## Step 4: Define Views in views.py
Open `views.py` in the `testapp` directory and define your view function:
```python
from django.http import HttpResponse  # Don't forget to import

def greeting(request):
    return HttpResponse('<h1>Welcome to DURGA Django classes, purely nursery-level classes</h1>')
```

## Step 5: Define URL Patterns in urls.py
In the `testapp` directory, create (or modify) a `urls.py` file to define the URL pattern for your view:
```python
from django.urls import path
from testapp import views

urlpatterns = [
    path("hello/", views.greeting),  # Map the URL to the view function
]
```
You also need to include `testapp.urls` in your main project `urls.py` located in the `FirstProject` directory:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls')),  # Include app URLs
]
```

## Step 6: Run the Server
Back in your terminal, run the server with:
```bash
python manage.py runserver
```

## Step 7: Send Request
Open your web browser and enter the URL:
```
http://127.0.0.1:8000/hello
```

### Notes on URL Access
- If the application is **not created** in the project, the default URL works correctly at `http://127.0.0.1:8000`.
- After creating an application, use specific URLs for HTTP requests:
  - Access the admin panel: `http://127.0.0.1:8000/admin`
  - Access your greeting view: `http://127.0.0.1:8000/hello`

If a direct URL is not assigned, you can use:
```python
path("", views.greeting)
```
Access it via:
```
http://127.0.0.1:8000
```

---

## Develop Web Application to Provide Current Server Time

## Step 1: Create Another Django Project
If needed, create a new Django project:
```bash
django-admin startproject secondproject
cd secondproject
```

## Step 2: Create Django Application
Create your application:
```bash
python manage.py startapp demoapp
```

## Step 3: Add Demo Application to settings.py
Open `settings.py` and add:
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "demoapp",  # Add demo application here
]
```

## Step 4: Create View Function
In `views.py` of `demoapp`, define the view function:
```python
from django.http import HttpResponse
import datetime  # Import datetime module

def time_info_view(request):
    current_time = datetime.datetime.now()
    response_content = f'<h1>Hello, current date and time: {current_time}</h1>'
    return HttpResponse(response_content)
```

## Step 5: Define URL Patterns in demoapp's urls.py
In `demoapp`, create (or edit) `urls.py`:
```python
from django.urls import path
from demoapp import views

urlpatterns = [
    path("time/", views.time_info_view),  # URL for time view
]
```
Make sure to include `demoapp.urls` in your main project's `urls.py` at `secondproject`:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demoapp.urls')),  # Include demoapp URLs
]
```

## Step 6: Run Server for the Second Project
Navigate to the `secondproject` directory and run:
```bash
python manage.py runserver
```

## Step 7: Send Request with the Correct URL Pattern
In your browser:
```
http://127.0.0.1:8000/time
```
or
```
http://localhost:8000/time
```

---

### Notes for Application Structure
- You can have a **single application** with **multiple views**.
- You can also have a **single project** with **multiple applications**.
- Consider defining URL patterns at the application level instead of the project level for better organization.

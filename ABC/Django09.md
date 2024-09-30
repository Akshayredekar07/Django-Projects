
## `StaticFilesProject`

#### Project Structure
You will create a new Django project named `StaticFilesProject` and an application named `testapp`. The structure should look like this:

```
C:.
│   db.sqlite3
│   manage.py
│
├───StaticFilesProject
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│
├───static
│   └───images
│           car.jpg
│           raje.jpg
│
├───templates
│   └───testapp
│           index.html
└───testapp
    │   admin.py
    │   apps.py
    │   models.py
    │   tests.py
    │   views.py
    │   __init__.py
```

#### Step 1: Create the Django Project and Application

Open your terminal and run the following commands:

```bash
django-admin startproject StaticFilesProject
cd StaticFilesProject
python manage.py startapp testapp
```

#### Step 2: Add the Application to `settings.py`

Open `settings.py` in `StaticFilesProject` and make the following modifications:

```python
# StaticFilesProject/settings.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    ...,
    'testapp',  # Add the testapp here
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Static files storage path
STATIC_DIR = BASE_DIR / 'static'
STATICFILES_DIRS = [STATIC_DIR, ]
```

#### Step 3: Create Static Directories

Create the `static` folder in the main project directory if it doesn't already exist and then create an `images` folder inside `static` to store your image files (e.g. `car.jpg`, `raje.jpg`).

```plaintext
static
└───images
        car.jpg
        raje.jpg
```

#### Step 4: Create a Template File

Create an `index.html` file inside `templates/testapp` with the following content:

```html
<!-- templates/testapp/index.html -->
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Models</title>
</head>
<body>
    <h1>Hello friends, The shortcut way to see the divine on the earth:</h1>
    <h2>The Available car models are:</h2>
    <ul>
        <li>{{ B1 }}</li>
        <li>{{ B2 }}</li>
        <li>{{ B3 }}</li>
    </ul>
    <img src="{% static 'images/car.jpg' %}" alt="Car Image Not Found!">
</body>
</html>
```

#### Step 5: Create the View Function

In `views.py` of your `testapp`, define the `car_views` function:

```python
# testapp/views.py

from django.shortcuts import render

def car_views(request):
    brands = {'B1': 'Range Rover', 'B2': 'Mustang', 'B3': 'Rolls Royce'}
    return render(request, 'testapp/index.html', context=brands)
```

#### Step 6: Define URL Patterns at the Application Level

Create `urls.py` in the `testapp` directory:

```python
# testapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_views, name='car_views'),
]
```

#### Step 7: Include Application URLs in the Project Level `urls.py`

Open `urls.py` in `StaticFilesProject` and include the `testapp` URLs:

```python
# StaticFilesProject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testapp/', include('testapp.urls')),
]
```

#### Step 8: Run the Development Server

Start your Django server to test everything:

```bash
python manage.py runserver
```

#### Step 9: Access Your View

Open your browser and go to:

```
http://127.0.0.1:8000/testapp/cars/
```

You should see the available car models displayed along with an image of a car. To directly access the static image, you can visit:

```
http://127.0.0.1:8000/static/images/car.jpg
```

### Summary

You have set up a Django project with static files. The basics include:

1. Creating static directories for images.
2. Updating `settings.py` for static files.
3. Using the `{% load static %}` template tag to reference static files in templates.
4. Creating views to render templates with dynamic content.


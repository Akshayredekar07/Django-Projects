Create Django project named `templateProject4` and an application called `cherry`, along with a view function that sends dynamic content from `views.py` to a template using template tags/variables.

### Step-by-Step Guide

#### Step 1: Create a New Django Project
Open your terminal or command prompt and execute the following commands:

```bash
django-admin startproject templateProject4
cd templateProject4
```

#### Step 2: Create a New Application
Now, create a Django application called `cherry`:

```bash
python manage.py startapp cherry
```

#### Step 3: Add the Application to `settings.py`
Open the `settings.py` file located in the `templateProject4` directory and add `'cherry'` to the `INSTALLED_APPS` list:

```python
# templateProject4/settings.py

INSTALLED_APPS = [
    ...,
    'cherry',  # Add the new application
]
```

#### Step 4: Create the Templates Directory
In the main project folder (`templateProject4`), create a directory called `templates` and a subdirectory for your application `cherry`. The structure should look like this:

```plaintext
templateProject4
|-- templates
|   |-- cherry
|       |-- your_template.html  # This is where your HTML templates will go
```

#### Step 5: Create a Template File
Inside the `templates/cherry` directory, create an HTML file (e.g., `your_template.html`):

```html
<!-- templates/cherry/your_template.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cherry App</title>
</head>
<body>
    <h1>Welcome to the Cherry App!</h1>
    <p>The current date and time is: {{ current_time }}</p>
</body>
</html>
```

#### Step 6: Write a View Function
In the `views.py` file of your `cherry` application, create a view function that prepares and sends data to the template:

```python
# cherry/views.py

from django.shortcuts import render
import datetime

def time_view(request):
    # Get the current date and time
    current_time = datetime.datetime.now()
    
    # Prepare a dictionary to pass to the template
    context = {
        'current_time': current_time
    }
    
    # Render the template with the context
    return render(request, 'cherry/your_template.html', context)
```

#### Step 7: Define URL Patterns for the Application
Create a new `urls.py` file inside your `cherry` application directory and define the URL pattern for your view:

```python
# cherry/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.time_view, name='time_view'),
]
```

#### Step 8: Include Application URLs in the Project Level `urls.py`
Open the `urls.py` file in the `templateProject4` directory and include the URLs from the `cherry` app:

```python
# templateProject4/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cherry/', include('cherry.urls')),  # Include cherry app URLs
]
```

#### Step 9: Start the Development Server
Run the Django development server to view your application:

```bash
python manage.py runserver
```

#### Step 10: Access Your View
Open your web browser and navigate to:

```
http://127.0.0.1:8000/cherry/time/
```

You should see the dynamic content rendered in your template, showing the current date and time.

### Summary of Steps
1. Create Django project and app.
2. Add the app to `settings.py`.
3. Organize the template directory structure.
4. Create HTML template with template tags.
5. Write view function to pass dynamic content.
6. Define URLs for accessing the view.
7. Start the server and access the view in a web browser.

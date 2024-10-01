
### Step-by-Step Guide to Set Up `DurgaJobs` Project

#### 1. **Create the Django Project and Application**

```bash
django-admin startproject DurgaJobs
cd DurgaJobs
python manage.py startapp testapp
```

#### 2. **Update `settings.py`**

Add the newly created `testapp` to the `INSTALLED_APPS` in `DurgaJobs/settings.py`:

```python
# DurgaJobs/settings.py

INSTALLED_APPS = [
    ...
    'testapp',
]
```

#### 3. **Define Models**

Define the models for job postings in `testapp/models.py`:

```python
# testapp/models.py

from django.db import models

class Hyderabad_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibilty = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.BigIntegerField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class Bengaluru_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibilty = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.BigIntegerField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class Pune_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibilty = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.BigIntegerField()

    def __str__(self):
        return f"{self.title} at {self.company}"
```

#### 4. **Create the Database Migrations**

To create and apply migrations for your models:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. **Register Models in Admin**

Add the following code to `testapp/admin.py` to register your job models for the admin interface:

```python
# testapp/admin.py

from django.contrib import admin
from .models import Hyderabad_jobs, Bengaluru_jobs, Pune_jobs

class HyderabadJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibilty', 'address', 'email', 'phone_number']

class BengaluruJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibilty', 'address', 'email', 'phone_number']

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibilty', 'address', 'email', 'phone_number']

admin.site.register(Hyderabad_jobs, HyderabadJobsAdmin)
admin.site.register(Bengaluru_jobs, BengaluruJobsAdmin)
admin.site.register(Pune_jobs, PuneJobsAdmin)
```

#### 6. **Create a Superuser**

Create a superuser account to access the Django admin:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

#### 7. **Run the Development Server**

Start your Django development server:

```bash
python manage.py runserver
```

#### 8. **Access the Admin Interface**

Navigate to the admin interface in your web browser:

```
http://127.0.0.1:8000/admin
```

Log in using the superuser credentials you created. You should see the registered job models.

### 9. **Create Views for Job Listings**

You might want to display job listings on a public-facing page. Create a view in `testapp/views.py`:

```python
# testapp/views.py

from django.shortcuts import render
from .models import Hyderabad_jobs, Bengaluru_jobs, Pune_jobs

def job_list(request):
    hyderabad_jobs = Hyderabad_jobs.objects.all()
    bengaluru_jobs = Bengaluru_jobs.objects.all()
    pune_jobs = Pune_jobs.objects.all()
    return render(request, 'testapp/job_list.html', {
        'hyderabad_jobs': hyderabad_jobs,
        'bengaluru_jobs': bengaluru_jobs,
        'pune_jobs': pune_jobs,
    })
```

### 10. **Set Up URL Routing**

Create a `urls.py` file in your `testapp` directory and set up the URLs for your app:

```python
# testapp/urls.py

from django.urls import path
from .views import job_list

urlpatterns = [
    path('jobs/', job_list, name='job_list'),
]
```

And include your app's URLs in the main `DurgaJobs/urls.py`:

```python
# DurgaJobs/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls')),  # Include the testapp URLs
]
```

### 11. **Create HTML Template**

Create a directory for templates in your `testapp`, following the structure `testapp/templates/testapp/`. Inside, create a file named `job_list.html`:

```html
<!-- testapp/templates/testapp/job_list.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Job Listings</title>
</head>
<body>
    <h1>Job Listings</h1>

    <h2>Hyderabad Jobs</h2>
    <ul>
        {% for job in hyderabad_jobs %}
        <li>{{ job.title }} at {{ job.company }} ({{ job.date }})</li>
        {% endfor %}
    </ul>

    <h2>Bengaluru Jobs</h2>
    <ul>
        {% for job in bengaluru_jobs %}
        <li>{{ job.title }} at {{ job.company }} ({{ job.date }})</li>
        {% endfor %}
    </ul>

    <h2>Pune Jobs</h2>
    <ul>
        {% for job in pune_jobs %}
        <li>{{ job.title }} at {{ job.company }} ({{ job.date }})</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### 12. **Access the Job Listings Page**

With everything set up, access your job listings page at:

```
http://127.0.0.1:8000/jobs/
```

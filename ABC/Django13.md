Here’s a comprehensive overview of creating a Django project using SQLite, including model creation, migrations, and admin setup:

---

### Setting Up a Django Project with SQLite

1. **Create a New Django Project:**
   ```bash
   django-admin startproject ModelProject2v
   ```

2. **Create a New App:**
   ```bash
   python manage.py startapp testapp
   ```

### Database Configuration for SQLite

Since SQLite is the default database for Django, no additional configurations are needed besides specifying the database in your `settings.py`. Here’s how to set it up:

```python
# settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # Uses the BASE_DIR variable to create db.sqlite3 in the project base directory
    }
}
```

### Creating the Student Model

Next, we define our model in `models.py` within the `testapp` directory.

```python
# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)  
    marks = models.IntegerField()  
```

### Check Database Connection

To verify the database connection, you can use the Django shell:

```bash
python manage.py shell
```
Then execute the following commands:
```python
from django.db import connection
c = connection.cursor()  # Create a cursor to execute SQL commands
```

### Creating Migrations

After defining the model, create the necessary database migrations:

```bash
python manage.py makemigrations
```

You should see an output similar to this:
```
Migrations for 'testapp':
  testapp\migrations\0001_initial.py
    - Create model Student
```

### Viewing the SQL for Migrations

To view the SQL that will be executed for the migrations, use:

```bash
python manage.py sqlmigrate testapp 0001
```

The output will look like this:
```sql
-- Create model Student
--
CREATE TABLE "testapp_student" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(30) NOT NULL,
    "marks" integer NOT NULL
);
COMMIT;
```

### Applying Migrations

To apply the migrations and create the corresponding tables in the database, run:

```bash
python manage.py migrate
```

**Advantage of Using Migrate Command:**
- It not only creates your table (`testapp_student`), but it also creates default application tables required by Django.

### Viewing Database Tables in Django

To access your tables in the Django admin interface, you need to set up an admin interface for your models.

### Creating a Superuser

First, create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

### Registering the Model in Admin

To make the `Student` model visible in the admin interface, you need to register it in `admin.py`:

```python
# admin.py
from django.contrib import admin
from testapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'marks']  # Specify which fields to display in the admin panel

admin.site.register(Student, StudentAdmin)  # Registering the Student model with the admin site
```

### Summary for New Projects

1. **Create the Django Project and App:**
   ```bash
   django-admin startproject ModelProject3
   django-admin startapp testapp
   ```

2. **Define the Model in `models.py`:**
   ```python
   from django.db import models

   class Students(models.Model):
       name = models.CharField(max_length=30)
       marks = models.IntegerField()
   ```

3. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Register in Admin:**
   ```python
   # admin.py
   from django.contrib import admin
   from testapp.models import Students

   class StudentAdmin(admin.ModelAdmin):
       list_display = ['name', 'marks']

   admin.site.register(Students, StudentAdmin)
   ```

5. **Creating a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

### Conclusion

This guide provides a step-by-step process for setting up a Django project with SQLite, creating models and migrations, and managing the admin interface. If you have any further questions or need clarification, feel free to ask!

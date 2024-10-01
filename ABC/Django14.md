## Modelproject5

1. **Start the Django Project:**
   ```bash
   django-admin startproject ModelPro5
   cd ModelPro5
   ```

2. **Start a New App:**
   ```bash
   django-admin startapp testapp
   ```

3. **Add the App to `settings.py`:**
   Open `ModelPro5/settings.py` and add `testapp` to the `INSTALLED_APPS` list:
   ```python
   INSTALLED_APPS = [
       ...
       'testapp',
   ]
   ```

4. **Add Database Configurations in `settings.py`:**
   Since we are using SQLite, the database configurations should look like this:
   ```python
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.sqlite3",
           "NAME": BASE_DIR / "db.sqlite3",
       }
   }
   ```

5. **Test Database Connection:**
   You can use the Django shell to check the database connection:
   ```bash
   python manage.py shell
   ```
   Then execute:
   ```python
   from django.db import connection
   c = connection.cursor()
   ```

6. **Create Models in `models.py`:**
   Inside `testapp/models.py`, define your employee model. For example:
   ```python
   from django.db import models

   class Employee(models.Model):
       name = models.CharField(max_length=100)
       position = models.CharField(max_length=100)
       salary = models.DecimalField(max_digits=10, decimal_places=2)

       def __str__(self):
           return self.name
   ```

7. **Create Migrations and Migrate:**
   Run the following commands to create and apply the migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Register Model and ModelAdmin inside `admin.py`:**
   To make the `Employee` model available in the Django admin, modify `admin.py` in `testapp`:
   ```python
   from django.contrib import admin
   from testapp.models import Employee

   class EmployeeAdmin(admin.ModelAdmin):
       list_display = ['name', 'position', 'salary']

   admin.site.register(Employee, EmployeeAdmin)
   ```

9. **Create a Superuser:**
   To access the admin interface, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

10. **Log in to Admin Interface:**
    Run the server and log in to the admin interface:
    ```bash
    python manage.py runserver
    ```
    Navigate to `http://127.0.0.1:8000/admin/`, log in, and check if the `Employee` table is created.

11. **Set Up Templates and Static Files:**
    - **Create a `templates` folder:**
      In your app directory (`testapp`), create a folder named `templates/testapp/`.
    - **Create a template file:**
      Create `employee_list.html` inside `templates/testapp/`:
      ```html
      <!DOCTYPE html>
      <html>
      <head>
          <title>Employee List</title>
      </head>
      <body>
          <h1>Employees</h1>
          <table>
              <tr>
                  <th>Name</th>
                  <th>Position</th>
                  <th>Salary</th>
              </tr>
              {% for employee in employees %}
              <tr>
                  <td>{{ employee.name }}</td>
                  <td>{{ employee.position }}</td>
                  <td>{{ employee.salary }}</td>
              </tr>
              {% endfor %}
          </table>
      </body>
      </html>
      ```
    - **Static Files (if needed):**
      You can configure static files in `settings.py` (though not explicitly requested in your steps):
      ```python
      STATIC_URL = '/static/'
      ```

12. **Create a View to Communicate with the Database:**
    In `testapp/views.py`, create a view that fetches data from the `Employee` model:
    ```python
    from django.shortcuts import render
    from .models import Employee

    def employee_list(request):
        employees = Employee.objects.all()  # Fetch all Employee records
        return render(request, 'testapp/employee_list.html', {'employees': employees})
    ```

13. **Set Up URL Routing:**
    To link the view to a URL, modify `testapp/urls.py` (create the file if it doesn't exist):
    ```python
    from django.urls import path
    from .views import employee_list

    urlpatterns = [
        path('employees/', employee_list, name='employee_list'),
    ]
    ```

    Then, include this URL configuration in the project's `urls.py` (inside `ModelPro5/urls.py`):
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('testapp.urls')),  # Include app URLs
    ]
    ```

14. **Run the Server and Test:**
    Finally, run the development server:
    ```bash
    python manage.py runserver
    ```
    Navigate to `http://127.0.0.1:8000/employees/` in your browser to see the list of employees displayed.



### Database Configuration in Django

**MySQL Database Connection:**
You can configure MySQL in your Django application through the `settings.py` file as follows:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "employeedb",
        "USER": 'root',
        "PASSWORD": 'root',  # Note: Corrected 'PASSWARD' to 'PASSWORD'
        "HOST": 'localhost',
        "PORT": 3306
    }
}
```

**Check Configurations:**
To check the connection to the database, utilize the Django shell:

```bash
python manage.py shell
```
Then run:
```python
from django.db import connection
cursor = connection.cursor()
```
This should execute without errors if your configurations are correct.

### Installing Necessary Packages for Oracle

For Oracle database configurations, ensure you have the necessary package:
```bash
pip install cx_Oracle
```

### Working with Models

#### What is a Model?
A model in Django is a Python class that defines the structure of your data, including fields and behaviors. Each model corresponds to a single database table.

#### Creating a Model Class
Create your model in the `models.py` file of your Django app (e.g., `testapp.py`):

```python
from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()  # Employee number
    ename = models.CharField(max_length=30)  # Employee name
    esal = models.FloatField()  # Employee salary
    eaddr = models.CharField(max_length=30)  # Employee address
```

#### Model to Table Mapping
- **Table Name:** By default, the table name is generated as `<app_name>_<model_name>`, so for `Employee`, it will be `testapp_employee`.
- **Fields:**
  - `eno`: Integer field
  - `ename`: Character field with max length of 30
  - `esal`: Float field
  - `eaddr`: Character field with max length of 30
- **ID Field:** Django automatically adds an `id` field as the primary key, which is an `AutoField`.

### Migrations

Migrations are how Django propagates changes you make to your models into the database schema.

1. **Create Migrations:**
   Run the following command to create migration files:
   ```bash
   python manage.py makemigrations
   ```
   This command generates a migration file (e.g., `0001_initial.py`) under `<your_app>/migrations/`.

2. **View SQL Code for Migrations:**
   To see the actual SQL code for the migration, use:
   ```bash
   python manage.py sqlmigrate testapp 0001
   ```

   The output should look like this:
   ```sql
   CREATE TABLE `testapp_employee` (
       `id` BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
       `eno` INTEGER NOT NULL,
       `ename` VARCHAR(30) NOT NULL,
       `esal` DOUBLE PRECISION NOT NULL,
       `eaddr` VARCHAR(30) NOT NULL
   );
   ```

3. **Apply Migrations:**
   To apply these migrations to your database, run:
   ```bash
   python manage.py migrate
   ```

### Summary of Steps to Apply Changes

1. Perform database configurations in `settings.py`.
2. Write your model class in `models.py`.
3. Create migrations with `python manage.py makemigrations`.
4. Review the SQL with `python manage.py sqlmigrate <app_name> <migration_number>`.
5. Apply migrations with `python manage.py migrate`.

### Additional Notes on the `id` Field:
- **Primary Key:** The `id` field serves as the unique identifier for each record and is generated automatically.
- **Field Type:** It is of type `BigAutoField` and increments automatically, so you do not need to provide a value for it when inserting data.
- **Default Behavior:** By default, all fields in Django are `NOT NULL`.


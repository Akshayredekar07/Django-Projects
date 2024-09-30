### Working with Models and Database in Django

Django provides built-in support for database operations through its Object-Relational Mapping (ORM), allowing developers to interact with databases using Python code instead of raw SQL queries.

#### Basic Concepts

1. **Use Cases for Data Storage:**
   - **Gmail:** Stores usernames and passwords.
   - **Bank applications:** Retains transaction information.

2. **CRUD Operations:**
   - **C**: Create (Insert data)
   - **R**: Retrieve (Select data)
   - **U**: Update (Modify existing data)
   - **D**: Delete (Remove data)

3. **SQL Queries:**
   - With Django's ORM, you typically do not need to write SQL queries manually.

#### Database Configuration in Django

1. **Configuration in `settings.py`:**
   - Add your application to `INSTALLED_APPS`.
   - Define template and static file configurations.
   - Set up the database configuration under the `DATABASES` setting.

2. **Default Database (SQLite3):**
   - If using the default SQLite3 database, minimal configuration is required. 
   - Example:
     ```python
     DATABASES = {
         "default": {
             "ENGINE": "django.db.backends.sqlite3",
             "NAME": BASE_DIR / "db.sqlite3",
         }
     }
     ```

3. **Custom Database Configuration:**
   - For databases other than SQLite, you need to specify parameters such as:
     ```python
     DATABASES = {
         "default": {
             "ENGINE": "django.db.backends.mysql",  # For MySQL
             "NAME": "your_db_name",
             "USER": "your_username",
             "PASSWORD": "your_password",
             "HOST": "localhost",  # Optional
             "PORT": "3306",  # MySQL port
         }
     }
     ```

#### Different Database Configurations

- **MySQL Configuration:**
  ```python
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.mysql",
          "NAME": "durgadb",
          "USER": "root",
          "PASSWORD": "root",
          "HOST": "localhost",
          "PORT": "3306"
      }
  }
  ```
  - Ensure you have the MySQL client installed: 
    ```bash
    pip install mysqlclient
    ```

- **Oracle Configuration:**
  ```python
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.oracle",
          "NAME": "XE",  # Example for Oracle Express
          "USER": "system",
          "PASSWORD": "durga",
          "HOST": "localhost",
          "PORT": "1521"
      }
  }
  ```

- **MongoDB Configuration:**
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'djongo',
          'NAME': 'your_database_name',
          'ENFORCE_SCHEMA': False,
          'CLIENT': {
              'host': 'mongodb://localhost:27017',
          }
      }
  }
  ```
  - Ensure you have the required packages:
    ```bash
    pip install djongo pymongo
    ```

#### Checking Database Connection in Django

To verify your database connection, you can use the Django shell:

1. Open the shell:
   ```bash
   python manage.py shell
   ```

2. Check the connection:
   ```python
   from django.db import connection
   cursor = connection.cursor()
   ```

   - If this executes without errors, your database configuration is correct.



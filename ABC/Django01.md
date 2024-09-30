# Overview of Django

### Background
- **Created**: In 2003 as an internal project at Lawrence Journal-World newspaper.
- **Open Source**: Django is maintained by the Django Software Foundation (DSF).
- **Founders**: Adrian Holovaty and Simon Willison.
- **Public Release**: July 21, 2005.
- **Name Origin**: Django is named after the guitarist Django Reinhardt.

### Official Information
- **Website**: [djangoproject.com](https://www.djangoproject.com/)
- **Tagline**: "The web framework for the perfectionist with deadlines."
- **Architecture**: Follows MVT (Model-View-Template) architecture.

### Top Features of Django Framework
1. **Fast Development**:
   - Django streamlines development, handling around 95% of the workload, leaving developers responsible for only 5%.
  
2. **Conciseness**:
   - Requires fewer lines of code compared to other frameworks.

3. **Fully Loaded**:
   - Comes with features like user authentication, content administration, and RSS feed management.

4. **Security**:
   - Protects against SQL Injection, cross-site scripting, and cross-site request forgery.

5. **Scalability**:
   - Can handle significant growth, from 100 requests on Day 1 to 500 million requests on Day 3.

6. **Versatility**:
   - Used in a variety of applications, from YouTube to NASA to educational institutions.

### Benefits of Using Django
- Simplifies developers' lives with clean syntax and clear documentation.

---

# Types of Applications in Python

## 1. Standalone Applications
- Applications run on a single machine without client-server architecture.
  - **Examples**: Calculator applications.
  - **Types**:
    - CUI (Character User Interface)
    - GUI (Graphical User Interface)

## 2. Enterprise Applications / Distributed Applications
- Applications designed with client-server architecture or distributed logic across multiple machines.
  - **Web Applications**: Built using Django, Flask.
  - **Distributed Applications**:
    - Web-based
    - Remote-based
  - **REST APIs**: For distributed applications.

---

# Understanding Django Projects vs. Applications

- **Project**: Comprises one or more applications along with configuration information.
  
### Creating a Django Project
- Command to create a new project:
  ```bash
  django-admin startproject FirstProject
  cd FirstProject
  ```

### Project Structure
```
FirstProject
|- manage.py  # Script to run the server and create applications
|- FirstProject
   |- settings.py
   |- urls.py
   |- wsgi.py
   |- asgi.py
   |- __init__.py
```

### Roles of Web Servers
- Web servers provide the environment to run web applications.
- They receive requests and route them to the appropriate views based on URL patterns.

### Running the Django Server
- Use the following command to run the server:
  ```bash
  python manage.py runserver
  ```
- Default runs on port 8000:
  - Access at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  - Change port with: 
    ```bash
    python manage.py runserver 7777
    ```

### Creating an Application
- Move to the project directory and run:
  ```bash
  python manage.py startapp testapp
  ```

### Application Structure
```
testapp
|- admin.py        # Customizes the admin page
|- apps.py         # Application-specific configurations
|- models.py       # Models specific to the application
|- tests.py        # Tests for application functionality
|- views.py        # View functions providing responses
|- __init__.py     # Treats the folder as a Python package
|- migrations/
   |- __init__.py  # Database-related information
```


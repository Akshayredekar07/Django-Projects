Django project named **DurgaNewsProject** with an app, focusing on static file handling and template rendering.

### Steps to Create DurgaNewsProject

1. **Create a Project and App:**
   ```bash
   django-admin startproject DurgaNewsProject
   cd DurgaNewsProject
   python manage.py startapp newsapp
   ```

2. **Configure the App in `settings.py`:**
   Add `newsapp` to `INSTALLED_APPS` in `DurgaNewsProject/settings.py`:
   ```python
   INSTALLED_APPS = [
       ...,
       'newsapp',  # Add your application here
   ]
   ```

3. **Define URL Patterns:**
   - Create `urls.py` in the `newsapp` directory.
   - In `DurgaNewsProject/urls.py`, include the app’s URLs:
   ```python
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('newsapp.urls')),
   ]
   ```

4. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

5. **Create a Templates Folder:**
   Create a `templates` folder inside `newsapp` to store HTML files.

6. **Configure Template Settings:**
   Ensure `TEMPLATES` in `DurgaNewsProject/settings.py` points to the correct directory:
   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [BASE_DIR / 'templates'],  # Add your templates path here
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   ...,
               ],
           },
       },
   ]
   ```

7. **Render a Template from a View:**
   In `newsapp/views.py`, create a view to render your HTML template:
```python
from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'testapp/index.html') 

def movies_view(request):
    head_msg = 'Durga Movie News'
    m1 = 'OTT is the result of covid'
    m2 = 'RRR is ready to release and will give the left and right'
    m3 = 'Love story movie is trending now'
    m4 = 'Real life screen actors are very horrible'
    m5 = 'Watch the unlimited movies with Durga Productions'
    type = 'Movies'

    my_dict = {'head_msg': head_msg, 'm1': m1, 'm2': m2, 'm3': m3, 'm4': m4, 'm5': m5, 'type': type}
    return render(request, 'testapp/news.html', my_dict)

def sports_view(request):
    head_msg = 'Durga Sports News'
    m1 = 'Olympics 2024 preparations are in full swing'
    m2 = 'IPL 2024: Teams gearing up for the final match'
    m3 = 'FIFA World Cup 2024: Exciting matches ahead'
    m4 = 'Tennis Grand Slam: New champions emerge'
    m5 = 'Formula 1: The race for the championship title'
    type = 'Sports'

    my_dict = {'head_msg': head_msg, 'm1': m1, 'm2': m2, 'm3': m3, 'm4': m4, 'm5': m5, 'type': type}
    return render(request, 'testapp/news.html', my_dict)


def politics_view(request):
    head_msg = 'Durga Politics News'
    m1 = 'Election 2024: Candidates reveal their agendas'
    m2 = 'New policies aimed at boosting the economy'
    m3 = 'Global summit focuses on climate change'
    m4 = 'Political debates heat up as elections approach'
    m5 = 'Government announces new infrastructure projects'
    type = 'Politics'

    my_dict = {'head_msg': head_msg, 'm1': m1, 'm2': m2, 'm3': m3, 'm4': m4, 'm5': m5, 'type': type}
    return render(request, 'testapp/news.html', my_dict)
   ```

8. **Pass Data to the Template (Optional):**
   Modify `home_view` to pass context data:
   ```python
   def home_view(request):
       articles = [{'title': 'News 1'}, {'title': 'News 2'}]
       return render(request, 'newsapp/home.html', {'articles': articles})
   ```

9. **Create a Static Folder:**
   Create a `static` folder inside `newsapp` to hold CSS, images, and other assets.

10. **Configure Static File Settings:**
   In `DurgaNewsProject/settings.py`, configure static files:
   ```python
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [BASE_DIR / 'static', BASE_DIR / 'newsapp/static']
   ```

11. **Load and Use Static Files in Templates:**
   In your HTML template (e.g., `newsapp/home.html`), load static files:
   ```html
   <!DOCTYPE html>
   {% load static %}
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>Durga News</title>
       <link rel="stylesheet" href="{% static 'css/styles.css' %}">
   </head>
   <body>
       <h1>Welcome to Durga News</h1>
       <ul>
           {% for article in articles %}
               <li>{{ article.title }}</li>
           {% endfor %}
       </ul>
   </body>
   </html>
   ```

### Final Note
You can now access your development server at `http://127.0.0.1:8000` 
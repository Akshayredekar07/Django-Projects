
1. **Create a Model for Feedback**

   Inside `testapp/models.py`, define a model to capture user feedback:

   ```python
   from django.db import models

   class Feedback(models.Model):
       name = models.CharField(max_length=100)
       roll_no = models.CharField(max_length=20)
       email = models.EmailField()
       feedback = models.TextField()

       def __str__(self):
           return self.name
   ```

2. **Create a Form for Feedback**

   Create a `forms.py` file inside `testapp` to define a Django form for capturing feedback:

   ```python
   # testapp/forms.py

   from django import forms
   from .models import Feedback

   class FeedbackForm(forms.ModelForm):
       class Meta:
           model = Feedback
           fields = ['name', 'roll_no', 'email', 'feedback']
   ```

3. **Handle Form Submission in Views**

   Define a view in `testapp/views.py` to handle form submission and render your template:

   ```python
   # testapp/views.py

   from django.shortcuts import render, redirect
   from .forms import FeedbackForm

   def feedback_view(request):
       submitted = False

       if request.method == 'POST':
           form = FeedbackForm(request.POST)
           if form.is_valid():
               form.save()  # Save the data to the database
               print('Form Validation Success:')
               print('Name: ', form.cleaned_data['name'])
               print('Roll No: ', form.cleaned_data['roll_no'])
               print('Email: ', form.cleaned_data['email'])
               print('Feedback: ', form.cleaned_data['feedback'])
               submitted = True  # Set the flag to indicate successful submission
               return redirect('feedback_view')  # Redirect after submission to prevent resubmission
       else:
           form = FeedbackForm()  # If not POST, create an empty form

       return render(request, 'testapp/feedback.html', {'form': form, 'submitted': submitted})
   ```

4. **Create a URL Mapping**

   Set up a URL for the feedback view by creating or updating the `urls.py` in `testapp`:

   ```python
   # testapp/urls.py

   from django.urls import path
   from .views import feedback_view

   urlpatterns = [
       path('', feedback_view, name='feedback_view'),
   ]
   ```

   Then, include this URL configuration in the main project’s `urls.py`:

   ```python
   # FeedbackProject/urls.py

   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('feedback/', include('testapp.urls')),  # Include the feedback app URLs
   ]
   ```

5. **Create Your Feedback Template**

   In the `testapp` directory, create a folder `templates/testapp/` and add `feedback.html`. This is where you will design your HTML form.

   ```html
   <!-- templates/testapp/feedback.html -->
   <!DOCTYPE html>
   {% load static %}
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Django Feedback Form</title>
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
           integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
   </head>
   <body>
       <div class="container" align="center">
           {% if submitted %}
               <h1>Thanks for providing your feedback!</h1>
               <h2>Enter feedback for another student</h2>
           {% else %}
               <h1>Student Feedback Form</h1>
           {% endif %}
           <form method="POST">
               {% csrf_token %}
               {{ form.as_p }}  <!-- Display the form fields -->
               <input type="submit" class="btn btn-lg btn-primary" value="Submit Feedback">
           </form>
       </div>
   </body>
   </html>
   ```

6. **Migrate and Run the Server**

   Run the following commands in your terminal to apply migrations and start your server:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

7. **Access the Feedback Form**

   Navigate to `http://127.0.0.1:8000/feedback/` in your web browser to test the feedback form. You should be able to submit feedback which will be saved into your database.

### Important Concepts Explained

- **CSRF Token**: The `{% csrf_token %}` tag generates a hidden input field containing a CSRF token, which protects against cross-site request forgery. This token changes with each session, meaning it can't be easily forged.
  
- **Form Handling**: The logic in `feedback_view` checks if the request method is `POST`. If so, it attempts to create a form instance with the provided data and validates it. If valid, the data is saved using `form.save()`.

- **Redirect After Submit**: After the feedback submission, the user is redirected to the same page to prevent the browser from resubmitting the form if the user refreshes.


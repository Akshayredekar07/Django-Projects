# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm


def home_view(request):
    return render(request, 'testapp/home.html')

@login_required
def java_view(request):
    return render(request, 'testapp/javaexam.html')

@login_required
def python_view(request):
    return render(request, 'testapp/pythonexam.html')

@login_required
def aptitude_view(request):
    return render(request, 'testapp/aptitude.html')

@login_required
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



def logout_view(request):
    return render(request, 'testapp/logout.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            print(form.errors)  # Print validation errors to the console for debugging
    else:
        form = SignUpForm()
    
    return render(request, 'testapp/signup.html', {'form': form})

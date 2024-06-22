from django.shortcuts import render
from testapp.forms import LoginForm
import datetime

def home_view(request):
    form = LoginForm()
    return render(request, 'testapp/index.html', {'form': form})

def date_time_view(request):
    name = request.GET.get('name')
    response = render(request, 'testapp/datetime.html', {'name': name})
    response.set_cookie('name', name)
    return response


def result_view(request):
    name = request.COOKIES.get('name')
    date_time = datetime.datetime.now()
    return render(request, 'testapp/result.html', {'name':name, 'date_time': date_time})


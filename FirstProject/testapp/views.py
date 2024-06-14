from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def display(request):
    s = "<h1>Welcome to DURGA Django classes purely nursey level classes, Don't feel difficult..really django is very easy</h1>"
    return HttpResponse(s)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_view(request):
    return HttpResponse('<h1>First View Response</h1>')

def second_view(request):
    return HttpResponse('<h1>Second View Response</h1>')

def third_view(request):
    return HttpResponse('<h1>First View Response</h1>')

def four_view(request):
    return HttpResponse('<h1>Four View Response</h1>')

def fifith_view(request):
    return HttpResponse('<h1>Fifth View Response</h1>')

def sixth_view(request):
    return HttpResponse('<h1>six View Response</h1>')
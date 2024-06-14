from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyderabad_job_view(request):
    s = "<h1>Hydrabad Jobs Information can find here</h1>"
    return HttpResponse(s)

def banglore_job_view(request):
    s = "<h1>Banglore Jobs Information can find here</h1>"
    return HttpResponse(s)


def pune_job_view(request):
    s = "<h1>Pune Jobs Information can find here</h1>"
    return HttpResponse(s)

  
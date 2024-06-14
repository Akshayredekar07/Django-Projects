from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view2(request):
    s = "<h1>Hello This response is from second and it is amazing!!</h1>"
    return HttpResponse(s)
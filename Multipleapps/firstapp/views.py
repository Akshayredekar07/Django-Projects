from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view1(request):
    s = "<h1>Hello This response is from firstapp and it is too good</h1>"
    return HttpResponse(s)
from django.shortcuts import render, HttpResponse

# Create your views here.
def welcome_view(request):
    print("This line added by view function")
    return HttpResponse('<h1>Custom middleware</h1>')


def homepage_view(request):
    return HttpResponse('<h1>Hello this response form viw page</h1>')


def middleware_view_project3(request):
    # print(10/0)
    return HttpResponse('<h1>Hello this response form view page 3</h1>')

def middleware_view_project4(request):
    print("This line printed by view function")
    return HttpResponse('<h1>Hello this response form view page 4</h1>')
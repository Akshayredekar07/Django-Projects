from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request, 'testapp/base.html')


def movies_page_view(request):
    return render(request, 'testapp/movie.html')

def sports_page_view(request):
    return render(request, 'testapp/sports.html')

def politics_page_view(request):
    return render(request, 'testapp/politics.html')
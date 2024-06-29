from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request, 'testapp/index.html')


def age_view(request):
    print(request.COOKIES)
    username = request.GET.get('name')
    response = render(request, 'testapp/age.html', {'name': username})
    response.set_cookie('name', username, max_age=120)
    return response


def gf_view(request):
    print(request.COOKIES)
    username = request.COOKIES.get('name')
    age = request.GET.get('age')
    response = render(request, 'testapp/gf.html', {'name': username})
    response.set_cookie('age', age, max_age=120)
    return response  


def result_view(request):
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    gf = request.GET.get('gf')
    response = render(request, 'testapp/result.html', {'name': name, 'age': age, 'gf': gf})
    response.set_cookie('gf', gf, max_age=120)
    return response

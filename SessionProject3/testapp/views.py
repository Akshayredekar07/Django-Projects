from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request, 'testapp/index.html')


def age_view(request):
    print(request.COOKIES)
    username=request.GET['name']
    response=render(request, 'testapp/age.html', {'name':username})
    response.set_cookie('name', username)
    return response


def gf_view(request):
    print(request.COOKIES)
    username=request.COOKIES['name']
    age = request.GET['age']
    response=render(request, 'testapp/gf.html', {'name':username})
    response.set_cookie('age', age)
    return response  


def result_view(request):
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    gf=request.GET['gf']
    response=render(request, 'testapp/result.html', {'name':name, 'age':age, 'gf':gf})
    response.set_cookie('gf', gf)
    return response    




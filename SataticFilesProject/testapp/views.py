from django.shortcuts import render

# Create your views here.
def car_views(request):
    brands = {'B1': 'RangeRover', "B2":"Mustang", "B3": "Rolles royals"}
    return render(request, 'testapp/index.html', context=brands)
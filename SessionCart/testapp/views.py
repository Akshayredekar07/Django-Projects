from django.shortcuts import render
from testapp.forms import AddItemform
# Create your views here.
def index_view(request):
    return render(request, 'testapp/home.html')

def additem_view(request):
    form = AddItemform()
    response =  render(request, 'testapp/additems.html', {'form':form})
    if request.method == 'POST':
        form=AddItemform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name, quantity)
    return response


def displayitems_view(request):
    return render(request, 'testapp/display.html')
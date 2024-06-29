from django.shortcuts import render
from testapp.forms import *
# Create your views here.
def additem_view(request):
    form = AddItemform()
    if request.method == 'POST':
        name = request.POST['name']
        qty=request.POST['qty']
        request.session['name']=qty

    return render(request, 'testapp/additem.html', {'form':form })


def displayitems_view(request):
    return render(request, 'testapp/displayitem.html')
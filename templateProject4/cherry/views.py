from django.shortcuts import render
import datetime
# Create your views here.

def info_view(request):
    time = datetime.datetime.now()
    name = "Django"
    prerequsites = "Python"
    my_dict = {'time': time, 'name': name, 'prerequsites':prerequsites}
    return render(request, 'cherry/result.html',context=my_dict)


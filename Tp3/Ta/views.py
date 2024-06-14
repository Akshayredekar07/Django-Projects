from django.shortcuts import render
import datetime

# Create your views here.
def datetime_view(request):
    date=datetime.datetime.now()
    my_dict={"msg":date}
    return render(request, 'Ta/datetime.html', context=my_dict)



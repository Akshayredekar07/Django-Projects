from django.shortcuts import render
import datetime 
from django.http import HttpResponse

# Create your views here.


def datetime_info_view(request):
    dt=datetime.datetime.now()
    h = int(dt.strftime('%H'))
    msg='<h1>Hello Friend,'
    if h<12:
        msg=msg+' Good morning'
    elif h<16:
        msg=msg+' Good afternoon'
    elif h<21:
        msg=msg+' Good evening'
    else :
        msg=msg+' Good Night'
    msg=msg+' </h1><hr>'
    msg=msg+'<h1>Now the server date and time is: '+str(dt)+'</h1>'
    print(msg)
    return HttpResponse(msg)

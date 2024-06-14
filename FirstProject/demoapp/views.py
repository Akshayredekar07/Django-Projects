from django.http import HttpRequest, HttpResponse
import datetime
# Create your views here.
# request is must be passed in the if not passed here then server giver error
def time_info_view(request):
    time=datetime.datetime.now()
    s='<h1>Hello current date and time: '+str(time)+ '</h1>'
    return HttpResponse(s)
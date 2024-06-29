from django.shortcuts import render
from django.http import HttpResponseBadRequest
from testapp.forms import *

# Create your views here.
def name_view(request):
    form = NameForm()
    return render(request, 'testapp/name.html', {'form': form})

def age_view(request):
    name = request.GET.get('name')
    if not name:
        return HttpResponseBadRequest("Missing 'name' parameter.")
    request.session['name'] = name
    form = AgeForm()
    return render(request, 'testapp/age.html', {'form': form, 'name': name})

def friend_view(request):
    age = request.GET.get('age')
    if not age:
        return HttpResponseBadRequest("Missing 'age' parameter.")
    request.session['age'] = age
    name = request.session.get('name')
    if not name:
        return HttpResponseBadRequest("Session 'name' is missing.")
    form = FriendForm()
    return render(request, 'testapp/friend.html', {'form': form, 'name': name})

def result_view(request):
    friend = request.GET.get('friend')
    if not friend:
        return HttpResponseBadRequest("Missing 'friend' parameter.")
    request.session['friend'] = friend 
    return render(request, 'testapp/result.html')

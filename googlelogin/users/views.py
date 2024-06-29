from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.
def home_view(request):
    return render(request, "home.html")

def logout_view(request):
    logout(redirect)
    return redirect("/")

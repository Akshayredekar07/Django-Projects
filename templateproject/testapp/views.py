from django.shortcuts import render

# Create your views here.
def wish_view(request):
    return render(request, 'testapp/wish.html')
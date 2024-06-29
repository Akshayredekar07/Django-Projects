from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello Hitman #45❤️ </h1>")

        
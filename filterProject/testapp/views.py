from django.shortcuts import render
from testapp.models import Student

# Create your views here.


def first_view(request):
    records = Student.objects.all()
    return render(request, 'testapp/first.html', {'records':records})
 
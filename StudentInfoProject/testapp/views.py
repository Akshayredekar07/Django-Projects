from django.shortcuts import render
from testapp.models import Student
from django.http import HttpResponse


def student_view(request):
    # student_list = Student.objects.all()
    # student_list = Student.objects.filter(marks__lt=35)
    # student_list = Student.objects.filter(name__startswith='A')
    # student_list = Student.objects.order_by('marks')
    student_list = Student.objects.order_by('-marks')
    if not student_list:
        return HttpResponse("No students found")
    my_dict = {'student_list': student_list}
    return render(request, 'testapp/data.html', my_dict)
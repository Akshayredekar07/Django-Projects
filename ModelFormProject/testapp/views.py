from django.shortcuts import render
from testapp.models import Student
from testapp.forms import StudentForm
# Create your views here.
def student_view(request):
    form=StudentForm()
    if request.method =='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record inserted in database successfully")

    return render(request, 'testapp/student.html', {'form':form})                 

 
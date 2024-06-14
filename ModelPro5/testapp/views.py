from django.shortcuts import render
#to display the database data to user import model class in views
from testapp.models import Employee

# Create your views here.
def empdata_view(request):
    emp_list=Employee.objects.all()  
    my_dict={"Emp_list": emp_list}
    return render(request, 'testapp/emp.html', context=my_dict)



 
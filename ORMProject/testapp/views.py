from django.shortcuts import render, redirect
from testapp.models import Employee

from django.db.models import Q
from django.db.models import Aggregate, Avg, Min, Sum, Count, Max
from django.db.models.functions import Lower

# Create your views here.
def retrive_view(request):
    # emp_list = Employee.objects.filter(esal__gt=15000)
    # emp_list = Employee.objects.filter(ename__contains="John")
    # emp_list = Employee.objects.filter(ename__icontains="john")
    # emp_list = Employee.objects.filter(id__in=[1,2,3])
    # emp_list = Employee.objects.filter(ename__startswith="D")
    # emp_list = Employee.objects.filter(ename__endswith="t")
    # emp_list = Employee.objects.filter(esal__range=[17000, 21000])
    # emp_list = Employee.objects.filter(esal__range=[17000, 21000]) | Employee.objects.filter(ename__contains="D")

    # emp_list = Employee.objects.filter(Q(esal__range=[17000, 21000]) | Q(ename__contains="D"))
    # emp_list = Employee.objects.filter(Q(esal__range=[17000, 21000]) & Q(ename__contains="D"))

    # emp_list = Employee.objects.filter(ename__contains="d", esal__gt = 15000)
    # emp_list = Employee.objects.values_list('ename', 'esal', 'eaddr')
    # emp_list = Employee.objects.values('ename', 'esal', 'eaddr')
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.all().order_by('eno')
    # emp_list = Employee.objects.all().order_by('-eno')
    # emp_list = Employee.objects.all().order_by('ename')
    # emp_list = Employee.objects.all().order_by(Lower('ename'))
    q1 = Employee.objects.filter(esal__lt=15000)
    q2 = Employee.objects.filter(ename__startswith="J")
    q3 = q1.union(q2)
    emp_list=q3

    # return render(request, 'testapp/index.html', {'emp_list': emp_list})
    return render(request, 'testapp/index.html', {'emp_list': emp_list})


def aggregate_view(request):
    print(request.user)
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))

    my_dict={'avg':avg['esal__avg'], 'max':max['esal__max'], 'min':min['esal__min'], 'sum':sum['esal__sum'], 'count':count['esal__count']}
    return render(request, 'testapp/aggreegate.html', my_dict)


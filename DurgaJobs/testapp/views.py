from django.shortcuts import render
from testapp.models import Hydrabad_jobs, Bengluru_jobs, Pune_jobs

# Create your views here.
def homepage_view(request):
    return render(request, 'testapp/index.html')


def hydjobs_view(request):
    job_list=Hydrabad_jobs.objects.all()
    my_dict={"Job_list":job_list}
    return render(request, 'testapp/hyd.html', context=my_dict)
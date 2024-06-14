from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'testapp/index.html') 

def movies_view(request):
    head_msg = 'Durga Movie News'
    m1 = 'OTT is the result of covid'
    m2 = 'RRR is ready to release and will give the left and right'
    m3 = 'Love story movie is trending now'
    m4 = 'Real life screen actors are very horrible'
    m5 = 'Watch the unlimited movies with Durga Productions'
    type = 'Movies'

    my_dict = {'head_msg': head_msg, 'm1': m1, 'm2': m2, 'm3': m3, 'm4': m4, 'm5': m5, 'type': type}
    return render(request, 'testapp/news.html', my_dict)

def sports_view(request):
    head_msg = 'Durga Sports News'
    m1 = 'Olympics 2024 preparations are in full swing'
    m2 = 'IPL 2024: Teams gearing up for the final match'
    m3 = 'FIFA World Cup 2024: Exciting matches ahead'
    m4 = 'Tennis Grand Slam: New champions emerge'
    m5 = 'Formula 1: The race for the championship title'
    type = 'Sports'

    my_dict = {'head_msg': head_msg, 'm1': m1, 'm2': m2, 'm3': m3, 'm4': m4, 'm5': m5, 'type': type}
    return render(request, 'testapp/news.html', my_dict)


def politics_view(request):
    head_msg = 'Durga Politics News'
    m1 = 'Election 2024: Candidates reveal their agendas'
    m2 = 'New policies aimed at boosting the economy'
    m3 = 'Global summit focuses on climate change'
    m4 = 'Political debates heat up as elections approach'
    m5 = 'Government announces new infrastructure projects'
    type = 'Politics'

    my_dict = {'head_msg': head_msg, 'm1': m1, 'm2': m2, 'm3': m3, 'm4': m4, 'm5': m5, 'type': type}
    return render(request, 'testapp/news.html', my_dict)



from django.shortcuts import render
import datetime
import random

# Create your views here.
def result_view(request):
    msg_list = [
        'Very soon, you are going to get marriage !!!',
        'The golden Days ahead',
        'Better to sleep more time even in office',
        'Tomarrow will be the best day of our life',
        'Very soon you will get job',
        'Tomarrow is the perfect day to propose ur gf'
    ]

    name_list=['Shrushti', 'vaishnavi',] 

    time = datetime.datetime.now()
    h = int(time.strftime('%H'))
    if h<12:
        s = "Good Morning"
    elif h<16:
        s = "Good Afternoon"
    elif h<21:
        s = "Good Evening"
    else:
        s = "Good night" 


    name = random.choice(name_list)
    msg = random.choice(msg_list)

    my_dict={'time':time, 'name':name, 'msg': msg, 'wish':s}

    return render(request, 'astroapp/index.html', my_dict)
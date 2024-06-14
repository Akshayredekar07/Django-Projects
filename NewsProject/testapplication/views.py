from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'testapplication/index.html')  


def movies_view(request):

    head_msg = "movies Information"
    sub_msg1 = "RRR released!"
    sub_msg2 = "Durga sir rocks in the upcoming django movie"
    sub_msg3 = "Background support must be required to get chance"
    sub_msg4 = "I don't like srk movies"
    sub_msg5 = "Biggest benefit of covid for industry: OTT"
    sub_msg6 = "Nitin is my favourite teacher!"

    my_dict = {'head_msg': head_msg, 'sub_msg1': sub_msg1, 'sub_msg2': sub_msg2, 'sub_msg3': sub_msg3, 'sub_msg4': sub_msg4, 'sub_msg5': sub_msg5, 'sub_msg6': sub_msg6,}
    return render(request, 'testapplication/demo.html',my_dict)      

def sports_view(request):
    head_msg = "Sports Information"
    sub_msg1 = "Football: Barcelona wins La Liga!"
    sub_msg2 = "Tennis: Nadal secures another Grand Slam victory"
    sub_msg3 = "Cricket: India defeats Australia in a thrilling match"
    sub_msg4 = "Basketball: Lakers emerge as NBA champions"
    sub_msg5 = "Athletics: New world record set in the 100m sprint"
    sub_msg6 = "Golf: Tiger Woods makes a remarkable comeback"

    my_dict = {
        'head_msg': head_msg,
        'sub_msg1': sub_msg1,
        'sub_msg2': sub_msg2,
        'sub_msg3': sub_msg3,
        'sub_msg4': sub_msg4,
        'sub_msg5': sub_msg5,
        'sub_msg6': sub_msg6,
    }
    return render(request, 'testapplication/demo.html', my_dict)

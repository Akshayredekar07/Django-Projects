from django.shortcuts import render

# Create your views here.
def page_count(request):
    print(request.COOKIES)
    count = request.session.get('count', 0)
    count = count + 1
    request.session['count']=count
    request.session.set_expiry(120)
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request, 'testapp/pagecount.html', {'count':count})


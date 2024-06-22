from django.shortcuts import render
from testapp.forms import FeedbackForm

# Create your views here.
def feedback_view(request):
    form=FeedbackForm()

    submitted =False
    name = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print("form Validation Successful!")
            print("#"*30)
            print('Name: ', form.cleaned_data['name'])
            print('Email: ', form.cleaned_data['email'])
            print('RollNo: ', form.cleaned_data['rollno'])
            print('Feedback: ', form.cleaned_data['feedback'])
            submitted=True
            name=form.cleaned_data['name']

        else:
            print("Some field validation fails")    

    return render(request, 'testapp/feedbackform.html', {'form':form, 'submitted':submitted, "name":name})

 
 
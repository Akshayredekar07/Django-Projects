from django.shortcuts import render
from testapp.froms import StudentForm  

def student_input_view(request):
    submitted = False    
    sname = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and printing data')
            print('Name: ', form.cleaned_data['name'])
            print('Marks: ', form.cleaned_data['marks'])
            print('Age: ', form.cleaned_data['age'])
            sname = form.cleaned_data['name']
            submitted = True
    else:
        form = StudentForm()

    return render(request, 'testapp/input.html', {'form': form, 'submitted': submitted, 'sname': sname})

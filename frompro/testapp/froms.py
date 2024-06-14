from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),
        label="Full Name"
    )
    marks = forms.IntegerField(
        required=True,
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter your marks'}),
        label="Marks"
    )
    age = forms.IntegerField(
        required=True,
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'}),
        label="Age"
    )

from django import forms

class AddItemform(forms.Form):
    name=forms.CharField()
    qty=forms.IntegerField()
    
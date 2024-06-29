from django import forms 

class AddItemform(forms.Form):
    itemname=forms.CharField()
    quantity=forms.IntegerField()


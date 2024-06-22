from django import forms

## import inbulit validators
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from django.core import validators


# #custom validators
# def starts_with_d(value):
#     print("starts_with_d is validated successfully")
#     if value[0].lower() != 'd':
#         raise forms.ValidationError('Name should starts with d')


# def gmail_validator(value):
#     print('Checking gmail validation')
#     if value[-10:] != '@gmail.com':
#         raise forms.ValidationError('mail extension should be gmail.com')

# class FeedbackForm(forms.Form):
#     name=forms.CharField(validators=[starts_with_d])
#     rollno=forms.IntegerField()
#     email=forms.EmailField(validators=[gmail_validator])
#     feedback=forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def clean_name(self):
#     print('Validating name field')
#     inputname=self.cleaned_data['name']
#     if len(inputname)<4:
#         raise forms.ValidationError('The minimum number of characters in the name filed should be 4')
#     return inputname

# def clean_rollno(self):
#     print('Validating rollno field')
#     inputrollno=self.cleaned_data['rollno']
#     return inputrollno

# def clean_email(self):
#     print('Validating email field')
#     inputemail=self.cleaned_data['email']
#     return inputemail

# def clean_feedback(self):
#     print('Validating feedback field')
#     inputfeedback=self.cleaned_data['email']
#     return inputfeedback

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class FeedbackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput, label='Enter Passowrd' ,)
    rpassword=forms.CharField(label='Passowrd(Again)' ,widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea)
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):
        print("Total form validation")
        total_cleaned_data = super().clean()
        print("total cleaned data", total_cleaned_data)

        inputname = total_cleaned_data["name"]
        if inputname[0].lower() != "d":
            raise forms.ValidationError("Name should starts with d")
        print("Checking gmail validation")

        inputemail = total_cleaned_data["email"]
        if inputemail[-10:] != "@gmail.com" and inputemail[-10:] != '@yahoo.com':
            raise forms.ValidationError("mail extension should be gmail.com or yahoo.com")

        pwd = total_cleaned_data['password']
        rpwd = total_cleaned_data['password']
        if pwd != rpwd:
            raise forms.ValidationError("both password must be same")
        
        bot_handler_value = total_cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError("Hello bot how are you")





# class Form:
#     def __init__(self):
#         self.cleaned_data={'name':'durga'}

# class Parent:
#     def __init__(self) -> None:
#         self.x=9999

#     def property(self):
#         print('gold+land+cash')


# class Child(Parent):
#     def education(self):
#         print("B.tech qualifacation")


# c=Child()
# c.education()
# c.property()
# print(c.x)        


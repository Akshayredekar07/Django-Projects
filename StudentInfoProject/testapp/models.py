# from django.db import models

# # Create your models here.
# class Student(models.Model):
#     rollno=models.IntegerField()
#     name=models.CharField(max_length=30)
#     dob=models.DateField()
#     marks=models.IntegerField()
#     email=models.EmailField()
#     # phonenumber=models.IntegerField(15)
#     phonenumber=models.BigIntegerField()
#     address=models.TextField()


from django.db import models

class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=100)
    dob = models.DateField()
    marks = models.IntegerField()
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)  # Use CharField for phone numbers
    address = models.TextField()

        
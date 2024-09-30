from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=64)
    class Meta:
        abstract = True


class Student(ContactInfo):
    rollNo = models.IntegerField()
    marks = models.IntegerField()

class Teacher(ContactInfo):
    subject = models.CharField(max_length=64)
    salary = models.FloatField()    


# mutitable inhetiance
class ContactInfo1(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=64)
    class Meta:
        abstract = True
class Student1(ContactInfo1):
    rollNo = models.IntegerField()
    marks = models.IntegerField()

class Teacher1(ContactInfo1):
    subject = models.CharField(max_length=64)
    salary = models.FloatField()    



# Mutilevel inhertiance
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Employee(Person):
    eno = models.IntegerField()
    esal = models.FloatField()


class Manager(Employee):
    exp = models.IntegerField() 
    team_size = models.IntegerField()


# Multiple inheritance
class Parent1(models.Model):
    f1 =  models.CharField(max_length=64)
    f2 =  models.CharField(max_length=64)

class Parent2(models.Model):
    f3 =  models.CharField(max_length=64, primary_key=True)
    f4 =  models.CharField(max_length=64)    


class Child(Parent1, Parent2):
    f5 =  models.CharField(max_length=64)
    f6 =  models.CharField(max_length=64)    



# SystemCheckError: System check identified some issues:

# ERRORS:
# testapp.Child: (models.E005) The field 'id' from parent model 'testapp.parent1' clashes with the field 'id' from parent model 'testapp.parent2'.

# Note: Parent classes should not contains common fileds, otherwise we will get error 


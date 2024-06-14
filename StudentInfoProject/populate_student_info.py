import os

# Set the Django settings module before importing any Django modules
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudentInfoProject.settings')

import django
django.setup()

from faker import Faker
from random import randint
from testapp.models import Student  # Ensure you are importing the correct model

# Create an instance of the Faker class
fakergen = Faker()

def phone_num_generation():
    d1 = randint(6, 9)
    num = str(d1)
    for i in range(9):
        num = num + str(randint(0, 9))
    return num  # Return as a string

def populate(n):
    for i in range(n):
        frollno = fakergen.random_int(min=1, max=999)
        fname = fakergen.name()
        fdob = fakergen.date()
        fmarks = fakergen.random_int(min=1, max=100)
        femail = fakergen.email()
        fphonenumber = phone_num_generation()
        faddress = fakergen.address()
        
        # Create or get the student record
        student_record, created = Student.objects.get_or_create(
            rollno=frollno,
            defaults={
                'name': fname,
                'dob': fdob,
                'marks': fmarks,
                'email': femail,
                'phonenumber': fphonenumber,
                'address': faddress
            }
        )

n = int(input("Enter the number of records: "))
# Populate the database with 1 student record
populate(n)
print(f"{n} records inserted")

import os

# Set the Django settings module before importing any Django modules
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FBVCrudProject.settings')

import django
django.setup()

from faker import Faker
from random import randint
from testapp.models import Employee

# Create an instance of the Faker class
fakergen = Faker()


def populate(n):
    for i in range(n):
        feno = randint(1001, 9999)
        fename= fakergen.name()
        fesal=randint(10000, 20000)
        feaddr = fakergen.city()

        emp_record=Employee.objects.get_or_create(
            eno = feno,
            ename = fename,
            esal = fesal,
            eaddr = feaddr
        )
   

n = int(input("Enter the number of records: "))
populate(n)
print(f"{n} records inserted")
